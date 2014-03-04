#import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.coreTools import *

#runOnMC = False
runOnMC = True


if runOnMC:
    print "Running on MC"
else:
    print "Running on Data"

process = cms.Process("TestRejection")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.default.limit = -1
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.options   = cms.untracked.PSet( 
    wantSummary = cms.untracked.bool(True),
    SkipEvent = cms.untracked.vstring('ProductNotFound'), #MB potentailly danger
)


#-- Calibration tag -----------------------------------------------------------
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

if runOnMC:
    #process.GlobalTag.globaltag = cms.string('START53_V7F::All')
    process.GlobalTag.globaltag = cms.string('START53_V19D::All')
else:
    process.GlobalTag.globaltag = cms.string('GR_P_V43D::All')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

#-- PAT standard config -------------------------------------------------------
#process.load("PhysicsTools.PatAlgos.patSequences_cff")
#process.load("RecoVertex.Configuration.RecoVertex_cff")


#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

## Dummy output for PAT. Not used in the analysis ##
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName       = cms.untracked.string('dummy.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    dropMetaData   = cms.untracked.string('DROPPED'),
    outputCommands = cms.untracked.vstring('keep *')
    )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:./patTuple.root',
    ),
#    eventsToSkip = cms.untracked.VEventRange('203912:253:308838634',
#                                             '203912:260:316528485',
#                                             '203912:792:880340063',
#                                             '203912:1214:1244871082',
#                                             ),                           
###
#   eventsToProcess = cms.untracked.VEventRange('1:57494144',
#                                               ),
)
#if runOnMC:
#    process.source.fileNames = ['file:./patTuple_MC.root']

#process.load("PhysicsTools/PatAlgos/patSequences_cff")

#from PhysicsTools.PatAlgos.tools.tauTools import *
#switchToPFTauHPS(process) #create HPS Taus from the pat default sequence


# switch on PAT trigger
#from PhysicsTools.PatAlgos.tools.trigTools import switchOnTrigger
#switchOnTrigger(process) #create pat trigger objects

#process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")

process.isolatedOfflineMuons = cms.EDFilter(
    "PATMuonSelector",
    src = cms.InputTag("isolatedMuonsLoose"),
    cut = cms.string("pt>17 && abs(eta)<2.1 && isGlobalMuon && userFloat('PFRelIsoDB04v2')<0.15"),
    filter = cms.bool(False)
    )
process.isolatedOfflineMuonsCounter = cms.EDFilter(
    #"CandViewCountFilter",
    "PATCandViewCountFilter",
    src = cms.InputTag("isolatedOfflineMuons"),
    minNumber = cms.uint32(1),
    maxNumber = cms.uint32(12345),
)
process.isolatedOnlineMuons = cms.EDProducer(
    "ChargedCandidateFromTrigRefConverter",
    triggerFilterMuonsSrc = cms.InputTag("hltL3crIsoL1sMu14erORMu16erL1f0L2f14QL3f17QL3crIsoRhoFiltered0p15")
)
process.isolatedOnlineMuonsCounter = cms.EDFilter(
        "CandViewCountFilter",
        #"PATCandViewCountFilter",
        src = cms.InputTag("isolatedOnlineMuons"),
        minNumber = cms.uint32(1),
        maxNumber = cms.uint32(12345),
)

process.onlineTaus20  = cms.EDFilter(
    "PATTauSelector",
    src = cms.InputTag("selectedHltPatTausPxl2NP"),
    cut = cms.string("pt>20"),
    filter = cms.bool(False)
    )

process.onlineTausLTrk20 = process.onlineTaus20.clone()
process.onlineTausLTrk20.cut = "pt>20 && tauID('decayModeFinding')>0.5"

process.onlineTausLTrkLooseIso20 = process.onlineTaus20.clone()
process.onlineTausLTrkLooseIso20.cut = "pt>20 && tauID('decayModeFinding')>0.5 && tauID('byIsolation')>0.5"

process.onlineTausLTrkLooseIso3Hits20 = process.onlineTaus20.clone()
process.onlineTausLTrkLooseIso3Hits20.cut = "pt>20 && tauID('decayModeFinding')>0.5 && tauID('byIsolation3hits')>0.5"

process.onlineTausLTrkLooseIso3HitsAntiMuL20 = process.onlineTaus20.clone()
process.onlineTausLTrkLooseIso3HitsAntiMuL20.cut = "pt>20 && tauID('decayModeFinding')>0.5 && tauID('byIsolation3hits')>0.5 && tauID('againstMuonLoose')>0.5"
#process.onlineTausLTrkLooseIso3HitsAntiMuL20.cut = "pt>20 && tauID('decayModeFinding')>0.5 && tauID('byIsolation3hits')>0.5 && tauID('againstMuonHoP')>0.5"
#process.onlineTausLTrkLooseIso3HitsAntiMuL20.cut = "pt>20 && tauID('decayModeFinding')>0.5 && tauID('byIsolation3hits')>0.5 && tauID('againstMuonLoose')>0.5 && tauID('againstMuonHoP')>0.5"

process.isolatedTausCounter = cms.EDFilter(
    #"CandViewCountFilter",
    "PATCandViewCountFilter",
    src = cms.InputTag("isolatedTaus"),
    minNumber = cms.uint32(1),
    maxNumber = cms.uint32(12345),
)

process.isoMuTau20Pairs = cms.EDProducer(
    "CandViewShallowCloneCombiner",
    decay = cms.string("isolatedOfflineMuons onlineTaus20"),
    cut = cms.string("sqrt((daughter(0).eta-daughter(1).eta)*(daughter(0).eta-daughter(1).eta)+  min( abs(daughter(0).phi-daughter(1).phi), 2*3.1415926 - abs(daughter(0).phi-daughter(1).phi)  ) *  min( abs(daughter(0).phi-daughter(1).phi), 2*3.1415926 - abs(daughter(0).phi-daughter(1).phi)  )  )>0.5"),
    checkCharge = cms.bool(False)
    )
process.isoMuTau20PairsCounter = cms.EDFilter(
        "CandViewCountFilter",
        #"PATCandViewCountFilter",
        src = cms.InputTag("isoMuTau20Pairs"),
            minNumber = cms.uint32(1),
            maxNumber = cms.uint32(12345),
        )

process.isoMuTauLTrk20Pairs = process.isoMuTau20Pairs.clone()
process.isoMuTauLTrk20Pairs.decay = "isolatedOfflineMuons onlineTausLTrk20" 
process.isoMuTauLTrk20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoMuTauLTrk20PairsCounter.src = "isoMuTauLTrk20Pairs"

process.isoMuTauLTrkIso20Pairs = process.isoMuTau20Pairs.clone()
process.isoMuTauLTrkIso20Pairs.decay = "isolatedOfflineMuons onlineTausLTrkLooseIso20" 
process.isoMuTauLTrkIso20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoMuTauLTrkIso20PairsCounter.src = "isoMuTauLTrkIso20Pairs"

process.isoMuTauLTrkIso3Hits20Pairs = process.isoMuTau20Pairs.clone()
process.isoMuTauLTrkIso3Hits20Pairs.decay = "isolatedOfflineMuons onlineTausLTrkLooseIso3Hits20" 
process.isoMuTauLTrkIso3Hits20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoMuTauLTrkIso3Hits20PairsCounter.src = "isoMuTauLTrkIso3Hits20Pairs"

process.isoMuTauLTrkIso3HitsAntiMuL20Pairs = process.isoMuTau20Pairs.clone()
process.isoMuTauLTrkIso3HitsAntiMuL20Pairs.decay = "isolatedOfflineMuons onlineTausLTrkLooseIso3HitsAntiMuL20" 
process.isoMuTauLTrkIso3HitsAntiMuL20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoMuTauLTrkIso3HitsAntiMuL20PairsCounter.src = "isoMuTauLTrkIso3HitsAntiMuL20Pairs"

process.isoMuTauLTrkIso3Hits20PairsNoZ = process.isoMuTauLTrkIso3HitsAntiMuL20Pairs.clone()
process.isoMuTauLTrkIso3Hits20PairsNoZ.cut = process.isoMuTauLTrkIso3HitsAntiMuL20Pairs.cut.value()+"&& (mass > 95 || mass < 85)"
process.isoMuTauLTrkIso3Hits20PairsNoZCounter = process.isoMuTau20PairsCounter.clone()
process.isoMuTauLTrkIso3Hits20PairsNoZCounter.src = "isoMuTauLTrkIso3Hits20PairsNoZ"

###
process.isoOnlineMuTau20Pairs = process.isoMuTau20Pairs.clone()
process.isoOnlineMuTau20Pairs.decay = "isolatedOnlineMuons onlineTaus20"
process.isoOnlineMuTau20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoOnlineMuTau20PairsCounter.src = "isoOnlineMuTau20Pairs"

process.isoOnlineMuTauLTrk20Pairs = process.isoMuTau20Pairs.clone()
process.isoOnlineMuTauLTrk20Pairs.decay = "isolatedOnlineMuons onlineTausLTrk20" 
process.isoOnlineMuTauLTrk20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoOnlineMuTauLTrk20PairsCounter.src = "isoOnlineMuTauLTrk20Pairs"

process.isoOnlineMuTauLTrkIso20Pairs = process.isoMuTau20Pairs.clone()
process.isoOnlineMuTauLTrkIso20Pairs.decay = "isolatedOnlineMuons onlineTausLTrkLooseIso20" 
process.isoOnlineMuTauLTrkIso20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoOnlineMuTauLTrkIso20PairsCounter.src = "isoOnlineMuTauLTrkIso20Pairs"

process.isoOnlineMuTauLTrkIso3Hits20Pairs = process.isoMuTau20Pairs.clone()
process.isoOnlineMuTauLTrkIso3Hits20Pairs.decay = "isolatedOnlineMuons onlineTausLTrkLooseIso3Hits20" 
process.isoOnlineMuTauLTrkIso3Hits20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoOnlineMuTauLTrkIso3Hits20PairsCounter.src = "isoOnlineMuTauLTrkIso3Hits20Pairs"

process.isoOnlineMuTauLTrkIso3HitsAntiMuL20Pairs = process.isoMuTau20Pairs.clone()
process.isoOnlineMuTauLTrkIso3HitsAntiMuL20Pairs.decay = "isolatedOnlineMuons onlineTausLTrkLooseIso3HitsAntiMuL20" 
process.isoOnlineMuTauLTrkIso3HitsAntiMuL20PairsCounter = process.isoMuTau20PairsCounter.clone()
process.isoOnlineMuTauLTrkIso3HitsAntiMuL20PairsCounter.src = "isoOnlineMuTauLTrkIso3HitsAntiMuL20Pairs"

process.isoOnlineMuTauLTrkIso3Hits20PairsNoZ = process.isoOnlineMuTauLTrkIso3HitsAntiMuL20Pairs.clone()
process.isoOnlineMuTauLTrkIso3Hits20PairsNoZ.cut = process.isoOnlineMuTauLTrkIso3HitsAntiMuL20Pairs.cut.value()+"&& (mass > 95 || mass < 85)"
process.isoOnlineMuTauLTrkIso3Hits20PairsNoZCounter = process.isoMuTau20PairsCounter.clone()
process.isoOnlineMuTauLTrkIso3Hits20PairsNoZCounter.src = "isoOnlineMuTauLTrkIso3Hits20PairsNoZ"

#########
execfile('jetsForHltTaus.py')
execfile('online-tau-rereco.py')

process.isolatedMuonsLoose = cms.EDFilter(
    "PATMuonSelector",
    src = cms.InputTag("selectedMuons"),
    cut = cms.string("pt>15 && abs(eta)<2.4 && isGlobalMuon && userFloat('PFRelIsoDB04v2')<0.3"),
    filter = cms.bool(False)
    )

process.offP = cms.Path(
    process.hltAntiKT5PFJetsForTaus+process.hltTauSequence + #to reco various hltTau collections
    process.isolatedMuonsLoose + #loose muons (needed only when run on non-_final tuples)
    process.isolatedOfflineMuons+process.isolatedOfflineMuonsCounter+
    process.onlineTaus20+process.isoMuTau20Pairs+process.isoMuTau20PairsCounter+
    process.onlineTausLTrk20+process.isoMuTauLTrk20Pairs+process.isoMuTauLTrk20PairsCounter+
    process.onlineTausLTrkLooseIso20+process.isoMuTauLTrkIso20Pairs+process.isoMuTauLTrkIso20PairsCounter+
    process.onlineTausLTrkLooseIso3Hits20+process.isoMuTauLTrkIso3Hits20Pairs+process.isoMuTauLTrkIso3Hits20PairsCounter
    +process.onlineTausLTrkLooseIso3HitsAntiMuL20+process.isoMuTauLTrkIso3HitsAntiMuL20Pairs+process.isoMuTauLTrkIso3HitsAntiMuL20PairsCounter
    +process.isoMuTauLTrkIso3Hits20PairsNoZ+process.isoMuTauLTrkIso3Hits20PairsNoZCounter
    )

process.onP = cms.Path(
    process.hltAntiKT5PFJetsForTaus+process.hltTauSequence + #to reco various hltTau collections
    process.isolatedOnlineMuons+process.isolatedOnlineMuonsCounter+
    process.onlineTaus20+process.isoOnlineMuTau20Pairs+process.isoOnlineMuTau20PairsCounter+
    process.onlineTausLTrk20+process.isoOnlineMuTauLTrk20Pairs+process.isoOnlineMuTauLTrk20PairsCounter+
    process.onlineTausLTrkLooseIso20+process.isoOnlineMuTauLTrkIso20Pairs+process.isoOnlineMuTauLTrkIso20PairsCounter+
    process.onlineTausLTrkLooseIso3Hits20+process.isoOnlineMuTauLTrkIso3Hits20Pairs+process.isoOnlineMuTauLTrkIso3Hits20PairsCounter
    +process.onlineTausLTrkLooseIso3HitsAntiMuL20+process.isoOnlineMuTauLTrkIso3HitsAntiMuL20Pairs+process.isoOnlineMuTauLTrkIso3HitsAntiMuL20PairsCounter
    +process.isoOnlineMuTauLTrkIso3Hits20PairsNoZ+process.isoOnlineMuTauLTrkIso3Hits20PairsNoZCounter
    )


process.end = cms.EndPath(
    #process.out
    )
