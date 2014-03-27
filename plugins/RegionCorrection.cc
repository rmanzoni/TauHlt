// system include files
#include <memory>
#include <math.h>
#include <vector>
#include <list>
#include <TTree.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/L1CaloTrigger/interface/L1CaloCollections.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloMipQuietRegion.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloRegionDetId.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloRegion.h"
#include "DataFormats/L1CaloTrigger/interface/L1CaloEmCand.h"

#include "L1Trigger/UCT2015/interface/UCTCandidate.h"
#include "L1Trigger/UCT2015/interface/helpers.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

using namespace std;
using namespace edm;

class RegionCorrection : public edm::EDProducer {
	public:

		// Concrete collection of output objects (with extra tuning information)
		typedef vector<UCTCandidate> UCTCandidateCollection;
		typedef std::auto_ptr<UCTCandidateCollection> UCTCandidateCollectionPtr;

		explicit RegionCorrection(const edm::ParameterSet&);

	private:
		virtual void produce(edm::Event&, const edm::EventSetup&);

		//Note the physical definitions are here but not used in calculation
                double egPhysicalEt(const L1CaloEmCand& cand) const {
                        return egLSB_*cand.rank();
                }

		//Note the physical definitions are here but not used in calculation
		double regionPhysicalEt(const L1CaloRegion& cand) const {
			return regionLSB_*cand.et();
		}

		//These are the definitions used in calculation below
                double egEt(const L1CaloEmCand& cand) const {
                        return cand.rank();
                }

		//These are the definitions used in calculation below
		double regionEt(const L1CaloRegion& cand) const {
			return cand.et();
		}


		// Helper methods

		// ----------member data ---------------------------

		bool debug;

		unsigned int puMult;
		bool puMultCorrect;

		//egLSB and regionLSB no longer used
                double egLSB_;
		double regionLSB_;

		L1CaloRegionCollection CorrectedRegionList;
		vector<double> m_regionSF;
		vector<double> m_regionSubtraction;
};


RegionCorrection::RegionCorrection(const edm::ParameterSet& iConfig) :
	puMultCorrect(iConfig.getParameter<bool>("puMultCorrect")),
        egLSB_(iConfig.getParameter<double>("egammaLSB")),
	regionLSB_(iConfig.getParameter<double>("regionLSB"))
{
	m_regionSF=iConfig.getParameter<vector<double> >("regionSF");
	m_regionSubtraction=iConfig.getParameter<vector<double> >("regionSubtraction");
	produces<L1CaloRegionCollection>("CorrectedRegions");
}


	void
RegionCorrection::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	if(!puMultCorrect) return;
	std::auto_ptr<L1CaloRegionCollection> CorrectedRegions(new L1CaloRegionCollection);

	Handle<L1CaloRegionCollection> notCorrectedRegions;
        Handle<L1CaloEmCollection> EMCands;

	iEvent.getByLabel("uctDigis", notCorrectedRegions);
        iEvent.getByLabel("uctDigis", EMCands);

	//-------- does something with the notCorrectedRegions
	puMult = 0;
	//This calulates PUM0
	for(L1CaloRegionCollection::const_iterator notCorrectedRegion =
			notCorrectedRegions->begin();
			notCorrectedRegion != notCorrectedRegions->end(); notCorrectedRegion++){
		double regionET =  regionEt(*notCorrectedRegion);
		// cout << "regionET: " << regionET <<endl; 
		if (regionET > 0) {puMult++;}
	}


	CorrectedRegionList.clear();
	for(L1CaloRegionCollection::const_iterator notCorrectedRegion =
			notCorrectedRegions->begin();
			notCorrectedRegion != notCorrectedRegions->end(); notCorrectedRegion++){
		double regionET =  regionEt(*notCorrectedRegion);
		unsigned int regionEta = notCorrectedRegion->gctEta();

                double regionEtCorr=0;

                // Only non-empty regions are corrected
                if(regionET!=0) {


                double energyECAL2x1=0;
                // Find associated 2x1 ECAL energy (EG are calibrated, we should not scale them up, it affects the isolation routines)
                // 2x1 regions have the MAX tower contained in the 4x4 region that its position points to.
                // This is to not break isolation.
                for(L1CaloEmCollection::const_iterator egtCand =EMCands->begin(); egtCand != EMCands->end(); egtCand++){
                        double et = egEt(*egtCand);
                        if(egtCand->regionId().iphi() == notCorrectedRegion->gctPhi() &&  egtCand->regionId().ieta() == notCorrectedRegion->gctEta()) {
                                energyECAL2x1=et;
                                break;  // I do not really like "breaks"
                        }
                }


		double alpha = m_regionSF[2*regionEta + 0]; //Region Scale factor (See regionSF_cfi.py)
		double gamma = 2*((m_regionSF[2*regionEta + 1])/9); //Region Offset. It needs to be divided by nine from the jet derived value in the lookup table. (See regionSF_cfi.py) Multiplied by 2 because gamma is given in regionPhysicalET (=regionEt*regionLSB), and we want regionEt= physicalEt/LSB and LSB=.5.


		int pumbin = (int) puMult/22; //396 Regions. Bins are 22 wide. Dividing by 22 gives which bin# of the 18 bins. 

		double puSub = m_regionSubtraction[18*regionEta+pumbin]*2;
	//The values in m_regionSubtraction are MULTIPLIED by RegionLSB=.5 (physicalRegionEt), so to get back unmultiplied regionSubtraction we want to multiply the number by 2 (aka divide by LSB).


		double pum0pt =  (regionET - puSub-energyECAL2x1); //subtract ECAl energy 

		double corrpum0pt = pum0pt*alpha+gamma+energyECAL2x1; //add back in ECAL energy, calibrate regions(not including the ECAL2x1).
                        //if(energyECAL2x1>20) std::cout<<energyECAL2x1<<"  "<<regionET<<"   "<<puSub<<"   -->"<<pum0pt<<"     "<<corrpum0pt<<"   "<<std::endl;
		if (corrpum0pt <0 || pum0pt<0) {corrpum0pt=0;} //zero floor

		regionEtCorr = (corrpum0pt);	
                }


		if(regionEta<18 && regionEta>3) //if !hf
		{		

			bool overflow=notCorrectedRegion->overFlow();
			bool tau=notCorrectedRegion->tauVeto();
			bool mip=notCorrectedRegion->mip();
			bool quiet= notCorrectedRegion->quiet();
			unsigned crate=notCorrectedRegion->rctCrate();
			unsigned card=notCorrectedRegion->rctCard();
			unsigned rgn=notCorrectedRegion->rctRegionIndex();
			CorrectedRegionList.push_back(L1CaloRegion(regionEtCorr, overflow, tau,mip,quiet,crate,card,rgn));
		}
		else //if hf
		{
			bool fineGrain= notCorrectedRegion->fineGrain();
			unsigned crate= notCorrectedRegion->rctCrate();
			unsigned hfRgn=notCorrectedRegion->rctRegionIndex();
			CorrectedRegionList.push_back(L1CaloRegion(regionEtCorr,fineGrain,crate, hfRgn));
		}
	}
	for(L1CaloRegionCollection::const_iterator CorrectedNewRegion = CorrectedRegionList.begin();
			CorrectedNewRegion != CorrectedRegionList.end(); ++CorrectedNewRegion) {
		CorrectedRegions->push_back(*CorrectedNewRegion);
	}


	iEvent.put(CorrectedRegions, "CorrectedRegions");
}
DEFINE_FWK_MODULE(RegionCorrection);
