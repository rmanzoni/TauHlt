import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_10_2_XaQ.root',
  )
)

process.vertex = cms.EDAnalyzer(
  'VertexInspector' ,
)

process.p = cms.Path(
  process.vertex 
  )

process.TFileService = cms.Service(
  "TFileService"                          ,
  fileName      = cms.string("test_vertex.root") ,
  closeFileFast = cms.untracked.bool(False)
)

