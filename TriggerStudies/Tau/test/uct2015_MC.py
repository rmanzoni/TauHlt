
#process.load("L1Trigger.UCT2015.emulation_cfi")
process.load("L1Trigger.UCT2015.emulationMC_cfi") #MB wrong config for 53X MC, use standard one with reruning hcal digis, should be fine for 62X/70X?

#to re-emulate HCal digis
#process.load("SimCalorimetry.HcalSimProducers.hcalUnsuppressedDigis_cfi")
#process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")

#process.hcalReEmulDigis = process.simHcalTriggerPrimitiveDigis.clone()
#process.hcalReEmulDigis.inputLabel = cms.VInputTag(cms.InputTag('hcalDigis'), cms.InputTag('hcalDigis'))
#process.HcalTPGCoderULUT.LUTGenerationMode = cms.bool(True)
#process.hackHCALMIPs.src = cms.InputTag("hcalReEmulDigis")
#
#process.emulationSequence.replace(process.hcalDigis,
#                                  process.hcalDigis+process.hcalReEmulDigis) #Reproduce HCal digis 

# Determine which calibration to use
#from L1Trigger.UCT2015.emulation_cfi import \
#        eg_calib_v1, eg_calib_v3, eg_calib_v4

#ecal_calibration = eg_calib_v4 #eg_calib_v1 eg_calib_v3
#process.RCTConfigProducers.eGammaECalScaleFactors = ecal_calibration
#process.RCTConfigProducers.jetMETECalScaleFactors = ecal_calibration
#process.UCT2015EClusterProducer.ecalCalibration = ecal_calibration

#process.RCTConfigProducers.eicIsolationThreshold = 3
#process.RCTConfigProducers.hActivityCut = 0.5

process.UCT2015Producer.do4x4Taus = True # 'standard' 4x4 L1Taus
process.UCT2015Producer4x8 = process.UCT2015Producer.clone(do4x4Taus = False) # 4x8 L1Taus
process.uctEmulatorStep.replace(process.UCT2015Producer,
                                process.UCT2015Producer+process.UCT2015Producer4x8)
# for 2x1 Taus (EG with tau-like settings)
process.RCTConfigProducers.eMinForFGCut = 999.
process.RCTConfigProducers.eMaxForFGCut = -999.
process.RCTConfigProducers.hOeCut = 0.05
process.RCTConfigProducers.eMinForHoECut = 999.
process.RCTConfigProducers.eMaxForHoECut = -999.
process.RCTConfigProducers.hMinForHoECut = 999.
process.RCTConfigProducers.eGammaHCalScaleFactors = [1., 1., 1., 1., 1.,
                                                     1., 1., 1., 1., 1.,
                                                     1., 1., 1., 1., 1.,
                                                     1., 1., 1., 1., 1.,
                                                     1., 1., 1., 1., 1.,
                                                     1., 1., 1.]

#process.load("L1Trigger.UCT2015.uct2015L1ExtraParticles_cfi")
process.load("L1Trigger.UCT2015.uctl1extraparticles_cfi")
#clone UCT gt stuff to have isoTau version in parallel (4x4)
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
# now 4x8
process.uctGctDigis4x8 = process.uctGctDigis.clone(
    egRelaxed = cms.InputTag("UCT2015Producer4x8","RelaxedEGUnpacked"),
    egIsolated  = cms.InputTag("UCT2015Producer4x8","IsolatedEGUnpacked"),
    tauIsolated  = cms.InputTag("UCT2015Producer4x8","RelaxedTauUnpacked"),
    jetSource  = cms.InputTag("UCT2015Producer4x8","CorrJetUnpacked"),
    setSource  = cms.InputTag("UCT2015Producer4x8","SETUnpacked"),
    metSource  = cms.InputTag("UCT2015Producer4x8","METUnpacked"),
    shtSource  = cms.InputTag("UCT2015Producer4x8","SHTUnpacked"),
    mhtSource  = cms.InputTag("UCT2015Producer4x8","MHTUnpacked") )
process.uctGctDigis4x8iso = process.uctGctDigis4x8.clone(
    tauIsolated  = cms.InputTag("UCT2015Producer4x8","IsolatedTauUnpacked") )
process.gtUCTDigis4x8 = process.gtUCTDigis.clone(
    GctInputTag  = cms.InputTag("uctGctDigis4x8") )
process.gtUCTDigis4x8iso = process.gtUCTDigis.clone(
    GctInputTag  = cms.InputTag("uctGctDigis4x8iso") )
process.l1extraParticlesUCT4x8 = process.l1extraParticlesUCT.clone(
    etTotalSource = cms.InputTag("uctGctDigis4x8"),
    nonIsolatedEmSource = cms.InputTag("uctGctDigis4x8","nonIsoEm"),
    etMissSource = cms.InputTag("uctGctDigis4x8"),
    htMissSource = cms.InputTag("uctGctDigis4x8"),
    forwardJetSource = cms.InputTag("uctGctDigis4x8","forJets"),
    centralJetSource = cms.InputTag("uctGctDigis4x8","cenJets"),
    tauJetSource = cms.InputTag("uctGctDigis4x8","tauJets"),
    isolatedEmSource = cms.InputTag("uctGctDigis4x8","isoEm"),
    etHadSource = cms.InputTag("uctGctDigis4x8"),
    hfRingEtSumsSource = cms.InputTag("uctGctDigis4x8"),
    hfRingBitCountsSource = cms.InputTag("uctGctDigis4x8")
)
process.l1extraParticlesUCT4x8iso = process.l1extraParticlesUCT.clone(
    etTotalSource = cms.InputTag("uctGctDigis4x8iso"),
    nonIsolatedEmSource = cms.InputTag("uctGctDigis4x8iso","nonIsoEm"),
    etMissSource = cms.InputTag("uctGctDigis4x8iso"),
    htMissSource = cms.InputTag("uctGctDigis4x8iso"),
    forwardJetSource = cms.InputTag("uctGctDigis4x8iso","forJets"),
    centralJetSource = cms.InputTag("uctGctDigis4x8iso","cenJets"),
    tauJetSource = cms.InputTag("uctGctDigis4x8iso","tauJets"),
    isolatedEmSource = cms.InputTag("uctGctDigis4x8iso","isoEm"),
    etHadSource = cms.InputTag("uctGctDigis4x8iso"),
    hfRingEtSumsSource = cms.InputTag("uctGctDigis4x8iso"),
    hfRingBitCountsSource = cms.InputTag("uctGctDigis4x8iso")
)
process.uct2015L1Extra.replace(
    process.uctGctDigis,
    process.uctGctDigis*process.uctGctDigis4x8*process.uctGctDigis4x8iso)
process.uct2015L1Extra.replace(
    process.gtUCTDigis,
    process.gtUCTDigis*process.gtUCTDigis4x8*process.gtUCTDigis4x8iso)
process.uct2015L1Extra.replace(
    process.l1extraParticlesUCT,
    process.l1extraParticlesUCT*process.l1extraParticlesUCT4x8*process.l1extraParticlesUCT4x8iso)

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
