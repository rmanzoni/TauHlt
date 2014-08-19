
process.load("L1Trigger.UCT2015.emulation_cfi")
#process.load("L1Trigger.UCT2015.emulationMC_cfi")
  
# Determine which calibration to use
#from L1Trigger.UCT2015.emulation_cfi import \
#        eg_calib_v1, eg_calib_v3, eg_calib_v4

#ecal_calibration = eg_calib_v4 #eg_calib_v1 eg_calib_v3
#process.RCTConfigProducers.eGammaECalScaleFactors = ecal_calibration
#process.RCTConfigProducers.jetMETECalScaleFactors = ecal_calibration
#process.UCT2015EClusterProducer.ecalCalibration = ecal_calibration

#process.RCTConfigProducers.eicIsolationThreshold = 3
#process.RCTConfigProducers.hActivityCut = 0.5

process.UCT2015Producer.do4x4Taus = False # 4x8 L1Taus

#process.load("L1Trigger.UCT2015.uct2015L1ExtraParticles_cfi")
process.load("L1Trigger.UCT2015.uctl1extraparticles_cfi")
#clone UCT gt stuff to have isoTau version in parallel
process.uctGctDigis.tauIsolated  = cms.InputTag("UCT2015Producer","RelaxedTauUnpacked")
process.uctGctDigis2 = process.uctGctDigis.clone(
    tauIsolated  = cms.InputTag("UCT2015Producer","IsolatedTauUnpacked")
)
process.l1extraParticlesUCT2 = process.l1extraParticlesUCT.clone(
    etTotalSource = cms.InputTag("uctGctDigis2"),
    nonIsolatedEmSource = cms.InputTag("uctGctDigis2","nonIsoEm"),
    etMissSource = cms.InputTag("uctGctDigis2"),
    htMissSource = cms.InputTag("uctGctDigis2"),
    forwardJetSource = cms.InputTag("uctGctDigis2","forJets"),
    centralJetSource = cms.InputTag("uctGctDigis2","cenJets"),
    tauJetSource = cms.InputTag("uctGctDigis2","tauJets"),
    isolatedEmSource = cms.InputTag("uctGctDigis2","isoEm"),
    etHadSource = cms.InputTag("uctGctDigis2"),
    hfRingEtSumsSource = cms.InputTag("uctGctDigis2"),
    hfRingBitCountsSource = cms.InputTag("uctGctDigis2")
)
process.gtUCTDigis2 = process.gtUCTDigis.clone(
    GctInputTag  = cms.InputTag("uctGctDigis2")
)
process.uct2015L1Extra.replace(process.uctGctDigis,
                               process.uctGctDigis*process.uctGctDigis2)
process.uct2015L1Extra.replace(process.gtUCTDigis,
                               process.gtUCTDigis*process.gtUCTDigis2)
process.uct2015L1Extra.replace(process.l1extraParticlesUCT,
                               process.l1extraParticlesUCT*process.l1extraParticlesUCT2)

####
process.uct2015Sequence = cms.Sequence(
   process.emulationSequence +
   #process.uct2015L1ExtraParticles
   process.uct2015L1Extra
)

#to keep
# *_uct2015L1ExtraParticles_*_*
# *_l1extraParticlesUCT*_*_*
# *_UCT2015Producer_*_*
