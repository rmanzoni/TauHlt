import FWCore.ParameterSet.Config as cms

pixelVertexCollectionTrimmer = cms.EDProducer(
  'PixelVertexCollectionTrimmer'   ,
  src            = cms.InputTag(''),
  maxVtx         = cms.int32(2)    ,
  fractionSumPt2 = cms.double(0.5) ,
  minSumPt2      = cms.double(100.),
)
