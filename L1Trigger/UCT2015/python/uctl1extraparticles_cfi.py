import FWCore.ParameterSet.Config as cms

from L1Trigger.GlobalTrigger.gtDigis_cfi import gtDigis
from Configuration.StandardSequences.RawToDigi_Data_cff import *
from L1Trigger.L1ExtraFromDigis.l1extraParticles_cfi import *

gctUCTDigis =cms.EDProducer("UCT2015GctCandsProducer",
    egRelaxed = cms.InputTag("UCT2015Producer","RelaxedEGUnpacked"),
    egIsolated  = cms.InputTag("UCT2015Producer","IsolatedEGUnpacked"),
    tauRelaxed = cms.InputTag("UCT2015Producer","RelaxedTauUnpacked"), # this collection is ignored in the final output, GT constraints 
    tauIsolated  = cms.InputTag("UCT2015Producer","RelaxedTauUnpacked"), # to switch to iso taus, do it here
    jetSource  = cms.InputTag("UCT2015Producer","CorrJetUnpacked"),
    setSource  = cms.InputTag("UCT2015Producer","SETUnpacked"),
    metSource  = cms.InputTag("UCT2015Producer","METUnpacked"),
    shtSource  = cms.InputTag("UCT2015Producer","SHTUnpacked"),
    mhtSource  = cms.InputTag("UCT2015Producer","MHTUnpacked")
)

l1extraParticlesUCT = cms.EDProducer("L1ExtraParticlesProd",
    muonSource = cms.InputTag("gtDigis"),
    etTotalSource = cms.InputTag("gctUCTDigis"),
    nonIsolatedEmSource = cms.InputTag("gctUCTDigis","nonIsoEm"),
    etMissSource = cms.InputTag("gctUCTDigis"),
    htMissSource = cms.InputTag("gctUCTDigis"),
    produceMuonParticles = cms.bool(True),
    forwardJetSource = cms.InputTag("gctUCTDigis","forJets"),
    centralJetSource = cms.InputTag("gctUCTDigis","cenJets"),
    produceCaloParticles = cms.bool(True),
    tauJetSource = cms.InputTag("gctUCTDigis","tauJets"),
    isolatedEmSource = cms.InputTag("gctUCTDigis","isoEm"),
    etHadSource = cms.InputTag("gctUCTDigis"),
    hfRingEtSumsSource = cms.InputTag("gctUCTDigis"), # these are empty
    hfRingBitCountsSource = cms.InputTag("gctUCTDigis"), # these are empty
    centralBxOnly = cms.bool(True),
    ignoreHtMiss = cms.bool(False)
)

gtUCTDigis   = gtDigis.clone()

gtUCTDigis.GmtInputTag  = cms.InputTag("gtDigis") # this is original GMT info from DATA (GMT is read out by GT FED)
gtUCTDigis.GctInputTag  = cms.InputTag("gctUCTDigis")
gtUCTDigis.EmulateBxInEvent = cms.int32(1)

uct2015L1Extra = cms.Sequence(
    gtEvmDigis
    *dttfDigis
    *csctfDigis
    *gctUCTDigis
    *gtUCTDigis
    *scalersRawToDigi*
    l1extraParticles*
    l1extraParticlesUCT  
)

