import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:myfile.root'
        #'/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_3_1_Cyy.root'
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_10_1_1MX.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_11_1_kFJ.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_12_1_e3T.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_1_1_pQI.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_2_1_W3w.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_3_1_Cyy.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_4_1_N9H.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_5_1_nja.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_6_1_pvV.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_7_1_ZMP.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_8_1_T1n.root',
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_9_1_xjm.root',
    ),
    eventsToProcess = cms.untracked.VEventRange(
    '1:353:35277',      
    ),
)

process.myProducerLabel = cms.EDProducer(
  'PixelVertexCollectionTrimmer'                   ,
  src            = cms.InputTag('hltPixelVertices'),
  maxVtx         = cms.int32(2)                    ,
  fractionSumPt2 = cms.double(0.5)                 ,
  minSumPt2      = cms.double(100.)                ,
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)
# process.out.outputCommands.append("keep *_*_*_*")

  
process.p = cms.Path(process.myProducerLabel)

process.e = cms.EndPath(process.out)
