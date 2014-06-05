// -*- C++ -*-
//
// Package:    PATreader
// Class:      PATreader
// 
/**\class PATreader PATreader.cc TriggerStudies/PATreader/src/PATreader.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Riccardo Manzoni,42 2-023,+41227662348,
//         Created:  Wed Feb 12 20:46:16 CET 2014
// $Id$
//
//


// system include files
#include <memory>
#include <vector>
#include <TMath.h>
// #include <TH1.h>
#include <TH1F.h>
#include <TH2F.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "TTree.h"

//
// class declaration
//

class PATreader : public edm::EDAnalyzer {
   public:
      explicit PATreader(const edm::ParameterSet&);
      ~PATreader();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      
      // ----------member data ---------------------------
      double lowerThreshold_ ;
      double upperThreshold_ ;
      double maxZDistance_   ;
      double power_          ;
      int    enhanceWeight_  ;
      bool   verbose_        ;

      bool   isfirst_    ;
      bool   ismatched_  ;
      int    ntrk_       ;
      double cl_         ;
      double sumpt2_     ;
      double ltpt_       ;
      int    ntrk5gev_   ;
      int    ntrk10gev_  ;
      int    evt_        ;
      int    onlvtxsize_ ;
      double avesumpt_   ;
      double weigh_      ;
      double sumpt3_     ;
      double sumpt4_     ;
      double subltpt_    ;

      TTree *vertexTree;

      edm::Service<TFileService>  outfile_ ;
      std::map<std::string, TH1*> hists_   ;
      std::map<std::string, TH2*> hists2D_ ;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
PATreader::PATreader(const edm::ParameterSet& iConfig) : 
  lowerThreshold_ (iConfig.getParameter<double>("lowerPtThreshold")),
  upperThreshold_ (iConfig.getParameter<double>("upperPtThreshold")),
  maxZDistance_   (iConfig.getParameter<double>("maxZDistance"    )),
  power_          (iConfig.getParameter<double>("power"           )),
  enhanceWeight_  (iConfig.getParameter<int>   ("enhanceWeight"   )),
  verbose_        (iConfig.getParameter<bool>  ("verbose"         ))
{
   //now do what ever initialization is needed

}


PATreader::~PATreader()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
PATreader::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  Handle<std::vector<reco::Vertex>>            offVtx  ;
  iEvent.getByLabel("selectedPrimaryVertices", offVtx) ;

  Handle<std::vector<reco::Vertex>>            onlPixVtx  ;
  iEvent.getByLabel("hltPixelVertices"       , onlPixVtx) ;

  Handle<std::vector<reco::Track>>             hltPixTrk  ;
  iEvent.getByLabel("hltPixelTracks"         , hltPixTrk) ;

  reco::Vertex offPV = offVtx->front() ;

  unsigned int onlPixVtxIndex = 0    ;
  unsigned int i              = 0    ; 
  double       maxsum         = 0.   ;
  double       leadTrkPt      = 0.   ;
  //double       subleadTrkPt   = 0.   ;
  double       power          = 1.   ;
  double       CL             = -99. ;
  int          nTracks        = 0    ;
  
  if (verbose_) std::cout << "vertex size\t" << onlPixVtx->size() << std::endl ;
  for ( reco::VertexCollection::const_iterator vtx = onlPixVtx->begin() ; vtx != onlPixVtx->end() ; ++vtx , ++i ){
    reco::Vertex vert = *vtx ;
    double sum  = 0. ;
    double sum3 = 0. ;
    double sum4 = 0. ;
    
    // sort vertex track by pt
    std::vector< reco::Track > sortedVertexTracks ;
    for ( reco::Vertex::trackRef_iterator trk = vert.tracks_begin(); trk != vert.tracks_end(); ++trk ) {
      reco::TrackRef trk_now(hltPixTrk, (*trk).key()) ;
      sortedVertexTracks.push_back(*trk_now) ;
    }  
    sort( sortedVertexTracks.begin(), sortedVertexTracks.end(), []( reco::Track a, reco::Track b ){ return a.pt() > b.pt(); } ) ;

    if (verbose_) std::cout << "\ttracks size \t" << sortedVertexTracks.size() << std::endl ;
    
    int j         = 0 ;   
    int nTracks5  = 0 ;
    int nTracks10 = 0 ;
    double sumpt  = 0 ;
    for ( reco::TrackCollection::const_iterator myIter = sortedVertexTracks.begin() ; myIter != sortedVertexTracks.end() ; ++myIter, ++j ) {
      double pt = myIter->pt() ;
      sumpt += pt ;
      if (verbose_) std::cout << "\t\t track#\t" << j << "\t pt\t" << pt << std::endl ;
      //std::cout << "\t\t chi2#\t" << myIter->chi2() << "\t ndof\t" << myIter->ndof() << std::endl ; 
      //std::cout << "\t\t track#\t" << j << "\t pt\t" << pt << std::endl ;
      if (myIter->chi2() > 10.83                       ) continue             ; // always 1 dof, 10.83 equivalent to 0.001 probability, 6.63 equivalent to 0.01 prob 
      pt = pt * TMath::Prob(myIter->chi2(),myIter->ndof()) ;
      if (pt < lowerThreshold_                        ) continue             ; 
      if (pt > upperThreshold_ && upperThreshold_ > 0.) pt = upperThreshold_ ;
      if ( j <= enhanceWeight_                        ) power = power_ + 1   ;
      else                                              power = power_       ;
      sum  += TMath::Power(pt, power) ; 
      sum3 += TMath::Power(pt, 3) ; 
      sum4 += TMath::Power(pt, 4) ; 
      if (myIter->pt() > 5. ) nTracks5 ++ ;
      if (myIter->pt() > 10.) nTracks10++ ;
    }    
    if ( sum > maxsum ){
      CL             = TMath::Prob(vert.chi2(),vert.ndof()) ;
      maxsum         = sum                                  ;
      onlPixVtxIndex = i                                    ;
      nTracks        = sortedVertexTracks.size()            ;
      leadTrkPt      = sortedVertexTracks.front().pt()      ;
      //subleadTrkPt   = sortedVertexTracks.at(1).pt()        ;
    } 

    evt_           = iEvent.id().event()               ;
    onlvtxsize_    = onlPixVtx->size()                 ;
    ntrk_          = sortedVertexTracks.size()         ;     
    ntrk5gev_      = nTracks5                          ;
    ntrk10gev_     = nTracks10                         ;
    cl_            = CL                                ;
    sumpt2_        = sum                               ;
    sumpt3_        = sum3                              ;
    sumpt4_        = sum4                              ;
    ltpt_          = sortedVertexTracks.front().pt()   ;
    subltpt_       = sortedVertexTracks.at(1).pt()     ;
    avesumpt_      = sumpt / sortedVertexTracks.size() ;
    weigh_         = 1. / onlPixVtx->size()            ;
    if ( fabs( vert.z() - offPV.z() ) <  maxZDistance_ ) ismatched_ = true  ; 
    if ( fabs( vert.z() - offPV.z() ) >= maxZDistance_ ) ismatched_ = false ; 
    if ( fabs( (*onlPixVtx->begin()).z() - offPV.z() ) <  maxZDistance_ ) isfirst_ = true  ; 
    if ( fabs( (*onlPixVtx->begin()).z() - offPV.z() ) >= maxZDistance_ ) isfirst_ = false ; 
    vertexTree -> Fill() ;

  }
  
  reco::Vertex onlPV ;
  
  if   ( onlPixVtxIndex <= onlPixVtx->size() ) onlPV = onlPixVtx->at(onlPixVtxIndex) ;
  else {
    //std::cout << "fuck\t" << iEvent.id().event() << std::endl ;
    return ;
  }
  
  unsigned int k          = 0             ;
  unsigned int myPosition = 0             ; 
  double       myDistance = maxZDistance_ ;
  if (verbose_) std::cout << "size " << onlPixVtx->size() << std::endl ;

  for ( reco::VertexCollection::const_iterator vtx = onlPixVtx->begin() ; vtx != onlPixVtx->end() ; ++vtx , ++k ){
    reco::Vertex onlvert = *vtx ; 
    if ( fabs( offPV.z() - onlvert.z() ) < myDistance ) {
      myDistance = fabs( offPV.z() - onlvert.z() ) ;
      myPosition = k ; 
    }
  }

  if (verbose_) std::cout << "myPosition " << myPosition << std::endl ;
  hists_["position"] -> Fill(myPosition) ;
  
  if ( fabs( onlPV.z() - offPV.z() ) < maxZDistance_ ) {
    if (verbose_) std::cout << "matched" << std::endl ;
    hists_  ["matched"  ] -> Fill(1)         ;
    hists2D_["matched2D"] -> Fill(nTracks,1) ;

    hists_  ["matched_maxsumpt"   ] -> Fill(maxsum)    ;
    hists_  ["matched_ntracks"    ] -> Fill(nTracks)   ;
    hists_  ["matched_CL"         ] -> Fill(CL)        ;
    hists_  ["matched_leadTrackpt"] -> Fill(leadTrkPt) ;
  }
  else {
    ismatched_ = false ; // online vtx does not match with offline
    if (verbose_) std::cout << "failed"  << std::endl ;
    hists_  ["matched"  ] -> Fill(0)         ;
    hists2D_["matched2D"] -> Fill(nTracks,0) ;

    hists_  ["failed_maxsumpt"    ] -> Fill(maxsum)    ;
    hists_  ["failed_ntracks"     ] -> Fill(nTracks)   ;
    hists_  ["failed_CL"          ] -> Fill(CL)        ;
    hists_  ["failed_leadTrackpt" ] -> Fill(leadTrkPt) ;
  }
      
}

// ------------ method called once each job just before starting event loop  ------------
void 
PATreader::beginJob()
{
  TH1::SetDefaultSumw2() ;
  TH2::SetDefaultSumw2() ;

  hists_  ["position"           ] = outfile_ -> make<TH1F>("position"           , "position"           ,  50  , 0., 50.     ) ;

  hists_  ["matched_maxsumpt"   ] = outfile_ -> make<TH1F>("matched_maxsumpt"   , "matched_maxsumpt"   , 100  , 0., 10000.  ) ;
  hists_  ["matched_ntracks"    ] = outfile_ -> make<TH1F>("matched_ntracks"    , "matched_ntracks"    , 30   , 0 , 30      ) ;
  hists_  ["matched_CL"         ] = outfile_ -> make<TH1F>("matched_CL"         , "matched_CL"         , 10000, 0., 1.      ) ;
  hists_  ["matched_leadTrackpt"] = outfile_ -> make<TH1F>("matched_leadTrackpt", "matched_leadTrackpt", 100  , 0., 500.    ) ;
 
  hists_  ["failed_maxsumpt"    ] = outfile_ -> make<TH1F>("failed_maxsumpt"    , "failed_maxsumpt"    , 100  , 0., 10000.  ) ;
  hists_  ["failed_ntracks"     ] = outfile_ -> make<TH1F>("failed_ntracks"     , "failed_ntracks"     , 30   , 0 , 30      ) ;
  hists_  ["failed_CL"          ] = outfile_ -> make<TH1F>("failed_CL"          , "failed_CL"          , 10000, 0., 1.      ) ;
  hists_  ["failed_leadTrackpt" ] = outfile_ -> make<TH1F>("failed_leadTrackpt" , "failed_leadTrackpt" , 100  , 0., 500.    ) ;

  hists_  ["matched"  ] = outfile_ -> make<TH1F>("matched"  , "matched"  , 2 , 0., 2.) ;
  hists2D_["matched2D"] = outfile_ -> make<TH2F>("matched2D", "matched2D", 20, 0 ,20 , 2, 0., 2.) ;

  vertexTree = new TTree("vertexTree", "vertexTree");
  vertexTree -> Branch("ismatched" , &ismatched_ ) ;
  vertexTree -> Branch("ntrk"      , &ntrk_      ) ;
  vertexTree -> Branch("cl"        , &cl_        ) ;
  vertexTree -> Branch("sumpt2"    , &sumpt2_    ) ;
  vertexTree -> Branch("ltpt"      , &ltpt_      ) ;
  vertexTree -> Branch("ntrk5gev"  , &ntrk5gev_  ) ;
  vertexTree -> Branch("ntrk10gev" , &ntrk10gev_ ) ;
  vertexTree -> Branch("isfirst"   , &isfirst_   ) ;
  vertexTree -> Branch("evt"       , &evt_       ) ;
  vertexTree -> Branch("onlvtxsize", &onlvtxsize_) ;
  vertexTree -> Branch("avesumpt"  , &avesumpt_  ) ;
  vertexTree -> Branch("weigh"     , &weigh_     ) ;
  vertexTree -> Branch("sumpt3"    , &sumpt3_    ) ;
  vertexTree -> Branch("sumpt4"    , &sumpt4_    ) ;
  vertexTree -> Branch("subltpt"   , &subltpt_   ) ;
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PATreader::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
PATreader::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
PATreader::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
PATreader::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
PATreader::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PATreader::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PATreader);
