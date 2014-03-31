import FWCore.ParameterSet.Config as cms

process = cms.Process("COPY")

# this inputs the input files
process.source = cms.Source (
  "PoolSource",
  fileNames=cms.untracked.vstring(
    'file:test.root',
    'file:anotherTest.root'
    )
  )

# talk to output module
process.out = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("patTuple.root")
  )

# A list of analyzers or output modules to be run after all paths have been run.
process.outpath = cms.EndPath(process.out)

