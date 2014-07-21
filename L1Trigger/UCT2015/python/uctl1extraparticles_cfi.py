import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.RawToDigi_Data_cff import *
from L1Trigger.L1ExtraFromDigis.l1extraParticles_cfi import *

uctGctDigis =cms.EDProducer("UCT2015GctCandsProducer",
    egRelaxed = cms.InputTag("UCT2015Producer","RelaxedEGUnpacked"),
    egIsolated  = cms.InputTag("UCT2015Producer","IsolatedEGUnpacked"),
    tauIsolated  = cms.InputTag("UCT2015Producer","IsolatedTauUnpacked"), # to switch to iso taus, do it here
    jetSource  = cms.InputTag("UCT2015Producer","CorrJetUnpacked"),
    setSource  = cms.InputTag("UCT2015Producer","SETUnpacked"),
    metSource  = cms.InputTag("UCT2015Producer","METUnpacked"),
    shtSource  = cms.InputTag("UCT2015Producer","SHTUnpacked"),
    mhtSource  = cms.InputTag("UCT2015Producer","MHTUnpacked")
)

l1extraParticlesUCT = cms.EDProducer("L1ExtraParticlesProd",
    muonSource = cms.InputTag("gtDigis"),
    etTotalSource = cms.InputTag("uctGctDigis"),
    nonIsolatedEmSource = cms.InputTag("uctGctDigis","nonIsoEm"),
    etMissSource = cms.InputTag("uctGctDigis"),
    htMissSource = cms.InputTag("uctGctDigis"),
    produceMuonParticles = cms.bool(True),
    forwardJetSource = cms.InputTag("uctGctDigis","forJets"),
    centralJetSource = cms.InputTag("uctGctDigis","cenJets"),
    produceCaloParticles = cms.bool(True),
    tauJetSource = cms.InputTag("uctGctDigis","tauJets"),
    isolatedEmSource = cms.InputTag("uctGctDigis","isoEm"),
    etHadSource = cms.InputTag("uctGctDigis"),
    hfRingEtSumsSource = cms.InputTag("uctGctDigis"), # these are empty
    hfRingBitCountsSource = cms.InputTag("uctGctDigis"), # these are empty
    centralBxOnly = cms.bool(True),
    ignoreHtMiss = cms.bool(False)
)

import L1Trigger.GlobalTrigger.gtDigis_cfi
gtUCTDigis   = L1Trigger.GlobalTrigger.gtDigis_cfi.gtDigis.clone()

gtUCTDigis.GmtInputTag  = cms.InputTag("gtDigis") # this is original GMT info from DATA (GMT is read out by GT FED)
gtUCTDigis.GctInputTag  = cms.InputTag("uctGctDigis")
gtUCTDigis.EmulateBxInEvent = cms.int32(1)

uct2015L1Extra = cms.Sequence(
    gtEvmDigis
    *dttfDigis
    *csctfDigis
    *uctGctDigis
    *gtUCTDigis
    *scalersRawToDigi*
    l1extraParticles*
    l1extraParticlesUCT  
)

