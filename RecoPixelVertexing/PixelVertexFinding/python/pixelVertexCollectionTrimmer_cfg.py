import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:myfile.root'
        '/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_noPVconstraint/patTuple_3_1_Cyy.root'
    )
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
