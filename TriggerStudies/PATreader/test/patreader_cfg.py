import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_10_2_XaQ.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_11_1_cnm.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_12_1_ZUs.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_1_1_hEq.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_2_1_UBR.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_3_1_dft.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_4_1_5RS.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_5_1_4Ly.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_6_1_cKk.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_7_1_Zoy.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_8_1_0pt.root',
    'root://eoscms//eos/cms//store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_9_2_eqP.root',
  )
)

process.sorter = cms.EDAnalyzer(
  'PATreader'                         ,
  lowerPtThreshold = cms.double(0.1  ) ,
  upperPtThreshold = cms.double(20.  ) ,
  maxZDistance     = cms.double(0.1  ) ,
  power            = cms.double(2.   ) ,
  enhanceWeight    = cms.int32 (-1   ) ,
  verbose          = cms.bool  (False) ,
)

process.p = cms.Path(
  process.sorter 
  )

process.TFileService = cms.Service(
  "TFileService"                          ,
  fileName      = cms.string("test_chi2_0p1_20.root") ,
  closeFileFast = cms.untracked.bool(False)
)

