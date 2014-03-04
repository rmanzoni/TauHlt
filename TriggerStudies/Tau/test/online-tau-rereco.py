## DA vertices at online
process.hltOnlinePrimaryVertices = cms.EDProducer( "PrimaryVertexProducer",
    vertexCollections = cms.VPSet( 
      cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
        useBeamConstraint = cms.bool( False ),
        minNdof = cms.double( 0.0 ),
        algorithm = cms.string( "AdaptiveVertexFitter" ),
        label = cms.string( "" )
      )#,
      #MB do not reproduce "WithBS" collection which is not used by tau
      #cms.PSet(  maxDistanceToBeam = cms.double( 1.0 ),
      #  useBeamConstraint = cms.bool( True ),
      #  minNdof = cms.double( 2.0 ),
      #  algorithm = cms.string( "AdaptiveVertexFitter" ),
      #  label = cms.string( "WithBS" )
      #)
    ),
    verbose = cms.untracked.bool( False ),
    TkFilterParameters = cms.PSet( 
      maxNormalizedChi2 = cms.double( 20.0 ),
      minPt = cms.double( 0.0 ),
      algorithm = cms.string( "filter" ),
      maxD0Significance = cms.double( 5.0 ),
      trackQuality = cms.string( "any" ),
      minPixelLayersWithHits = cms.int32( 2 ),
      minSiliconLayersWithHits = cms.int32( 5 )
    ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    TrackLabel = cms.InputTag( "hltPFMuonMerging" ),
    TkClusParameters = cms.PSet( 
      TkDAClusParameters = cms.PSet( 
        d0CutOff = cms.double( 3.0 ),
        Tmin = cms.double( 4.0 ),
        dzCutOff = cms.double( 4.0 ),
        coolingFactor = cms.double( 0.6 ),
        use_vdt = cms.untracked.bool( True ),
        vertexSize = cms.double( 0.01 )
      ),
      algorithm = cms.string( "DA_vect" ) #MB DA->DA_vec (faster algorithm)
    )
)

# Jets for rho
process.hltKT6PFJetsForTaus = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 1 ),
    doAreaFastjet = cms.bool( False ),
    voronoiRfact = cms.double( 0.9 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    jetType = cms.string( "PFJet" ),
    minSeed = cms.uint32( 14327 ),
    Ghost_EtaMax = cms.double( 5.0 ),
    doRhoFastjet = cms.bool( True ),
    jetAlgorithm = cms.string( "Kt" ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 2.5 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    rParam = cms.double( 0.6 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doOutputJets = cms.bool( True ),
    src = cms.InputTag( "hltParticleFlowForTaus" ),
    inputEtMin = cms.double( 0.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    jetPtMin = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    doPUOffsetCorr = cms.bool( False ),
    inputEMin = cms.double( 0.0 ),
    subtractorName = cms.string( "" ),
    MinVtxNdof = cms.int32( 0 ),
    MaxVtxZ = cms.double( 15.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    sumRecHits = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 )
)

## PFTaus
####
# Discriminators for cloning
process.hltPFTauTrackFindingDiscriminatorOffVtx = cms.EDProducer(
    "PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double( 0.0 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    UseOnlyChargedHadrons = cms.bool( True ),
    PFTauProducer = cms.InputTag( "hltPFTausOffVtx" )
    )
process.hltPFTauLooseIsolationDiscriminatorOffVtx = cms.EDProducer(
    "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( "hltPFTausOffVtx" ),
    qualityCuts = cms.PSet(
       isolationQualityCuts = cms.PSet(
          minTrackHits = cms.uint32( 8 ),
          minTrackPt = cms.double( 1.5 ),
          maxTrackChi2 = cms.double( 100.0 ),
          minTrackPixelHits = cms.uint32( 3 ),
          minGammaEt = cms.double( 1.5 ),
          useTracksInsteadOfPFHadrons = cms.bool( False ),
          maxDeltaZ = cms.double( 0.2 ),
          maxTransverseImpactParameter = cms.double( 0.05 )
          ),
       signalQualityCuts = cms.PSet(
          minTrackPt = cms.double( 0.0 ),
          maxTrackChi2 = cms.double( 1000.0 ),
          useTracksInsteadOfPFHadrons = cms.bool( False ),
          minGammaEt = cms.double( 0.5 ),
          minTrackPixelHits = cms.uint32( 0 ),
          minTrackHits = cms.uint32( 3 ),
          maxDeltaZ = cms.double( 0.4 ),
          maxTransverseImpactParameter = cms.double( 0.2 )
          ),
       primaryVertexSrc = cms.InputTag( "offlinePrimaryVertices" ),
       pvFindingAlgo = cms.string( "highestPtInEvent" )
       ),
    maximumSumPtCut = cms.double( 6.0 ),
    deltaBetaPUTrackPtCutOverride = cms.double( 0.5 ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( False ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    rhoProducer = cms.InputTag( 'hltKT6PFJetsForTaus','rho' ),
    deltaBetaFactor = cms.string( "0.38" ),
    relativeSumPtCut = cms.double( 0.0 ),
    Prediscriminants = cms.PSet(
    BooleanOperator = cms.string( "and" ),
    leadTrack = cms.PSet(
       Producer = cms.InputTag( "hltPFTauTrackFindingDiscriminatorOffVtx" ),
       cut = cms.double( 0.5 )
       )
    ),
    applyOccupancyCut = cms.bool( True ),
    applyDeltaBetaCorrection = cms.bool( False ),
    applyRelativeSumPtCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    storeRawSumPt = cms.bool( False ),
    applyRhoCorrection = cms.bool( False ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" )
    )

process.hltPFTauECalIsolationDiscriminatorOffVtx = cms.EDProducer(
    "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( "hltPFTausOffVtx" ),
    qualityCuts = cms.PSet(
       isolationQualityCuts = cms.PSet(
          minTrackHits = cms.uint32( 8 ),
          minTrackPt = cms.double( 1.5 ),
          maxTrackChi2 = cms.double( 100.0 ),
          minTrackPixelHits = cms.uint32( 3 ),
          minGammaEt = cms.double( 1.5 ),
          useTracksInsteadOfPFHadrons = cms.bool( False ),
          maxDeltaZ = cms.double( 0.2 ),
          maxTransverseImpactParameter = cms.double( 0.05 )
          ),
       signalQualityCuts = cms.PSet(
          minTrackPt = cms.double( 0.0 ),
          maxTrackChi2 = cms.double( 1000.0 ),
          useTracksInsteadOfPFHadrons = cms.bool( False ),
          minGammaEt = cms.double( 0.5 ),
          minTrackPixelHits = cms.uint32( 0 ),
          minTrackHits = cms.uint32( 3 ),
          maxDeltaZ = cms.double( 0.4 ),
          maxTransverseImpactParameter = cms.double( 0.2 )
          ),
       primaryVertexSrc = cms.InputTag( "offlinePrimaryVertices" ),
       pvFindingAlgo = cms.string( "highestPtInEvent" )
       ),
    maximumSumPtCut = cms.double( 6.0 ),
    deltaBetaPUTrackPtCutOverride = cms.double( 0.5 ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( False ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( False ),
    rhoProducer = cms.InputTag( 'hltKT6PFJetsForTaus','rho' ),
    deltaBetaFactor = cms.string( "0.38" ),
    relativeSumPtCut = cms.double( 0.0 ),
    Prediscriminants = cms.PSet(
    BooleanOperator = cms.string( "and" ),
    leadTrack = cms.PSet(
       Producer = cms.InputTag( "hltPFTauTrackFindingDiscriminatorOffVtx" ),
       cut = cms.double( 0.5 )
       )
    ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    applyRelativeSumPtCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( True ),
    storeRawSumPt = cms.bool( True ),
    applyRhoCorrection = cms.bool( False ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" )
    )
process.hltPFTauTrkIsolationDiscriminatorOffVtx = cms.EDProducer(
    "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( "hltPFTausOffVtx" ),
    qualityCuts = cms.PSet(
       isolationQualityCuts = cms.PSet(
          minTrackHits = cms.uint32( 8 ),
          minTrackPt = cms.double( 0.5 ),
          maxTrackChi2 = cms.double( 100.0 ),
          minTrackPixelHits = cms.uint32( 3 ),
          minGammaEt = cms.double( 1.5 ),
          useTracksInsteadOfPFHadrons = cms.bool( False ),
          maxDeltaZ = cms.double( 0.2 ),
          maxTransverseImpactParameter = cms.double( 0.05 )
          ),
       signalQualityCuts = cms.PSet(
          minTrackPt = cms.double( 0.0 ),
          maxTrackChi2 = cms.double( 1000.0 ),
          useTracksInsteadOfPFHadrons = cms.bool( False ),
          minGammaEt = cms.double( 0.5 ),
          minTrackPixelHits = cms.uint32( 0 ),
          minTrackHits = cms.uint32( 3 ),
          maxDeltaZ = cms.double( 0.4 ),
          maxTransverseImpactParameter = cms.double( 0.2 )
          ),
       primaryVertexSrc = cms.InputTag( "offlinePrimaryVertices" ),
       pvFindingAlgo = cms.string( "highestPtInEvent" )
       ),
    maximumSumPtCut = cms.double( 6.0 ),
    deltaBetaPUTrackPtCutOverride = cms.double( 0.5 ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( False ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    rhoProducer = cms.InputTag( 'hltKT6PFJetsForTaus','rho' ),
    deltaBetaFactor = cms.string( "0.38" ),
    relativeSumPtCut = cms.double( 0.0 ),
    Prediscriminants = cms.PSet(
    BooleanOperator = cms.string( "and" ),
    leadTrack = cms.PSet(
       Producer = cms.InputTag( "hltPFTauTrackFindingDiscriminatorOffVtx" ),
       cut = cms.double( 0.5 )
       )
    ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    applyRelativeSumPtCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    storeRawSumPt = cms.bool( True ),
    applyRhoCorrection = cms.bool( False ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" )
    )
process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx = process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackHits = 5
process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackPixelHits = 2
process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackHits = 5
process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackPixelHits = 2
process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx = process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackHits = 3
process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackPixelHits = 1
process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackHits = 3
process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.qualityCuts.isolationQualityCuts.minTrackPixelHits = 1

#anti-mu discr
process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx = cms.EDProducer(
    "PFRecoTauDiscriminationAgainstMuon2",
    PFTauProducer = cms.InputTag('hltPFTausOffVtx'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string("and"),
    ),
    discriminatorOption = cms.string('custom'),
    HoPMin = cms.double(-1),
    maxNumberOfMatches = cms.int32(1),
    doCaloMuonVeto = cms.bool(False),
    maxNumberOfHitsLast2Stations = cms.int32(-1),
    # optional collection of muons to check for overlap with taus
    srcMuons = cms.InputTag(''), #cms.InputTag('hltMuons')
    dRmuonMatch = cms.double(0.3),
    verbosity = cms.int32(0)
    )
process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx = process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.maxNumberOfMatches = -1
process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.doCaloMuonVeto = True
process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.HoPMin = 0.2

## New producer
process.hltTauPFJets08Region = cms.EDProducer("RecoTauJetRegionProducer",
    src = cms.InputTag( "hltAntiKT5PFJetsForTaus" ),
    deltaR = cms.double(0.8),
    pfSrc = cms.InputTag( "hltParticleFlowForTaus" )
)
process.hltPFTauPiZeros = cms.EDProducer( "RecoTauPiZeroProducer",
    massHypothesis = cms.double( 0.136 ),
    ranking = cms.VPSet( 
      cms.PSet(  selectionPassFunction = cms.string( "abs(mass() - 0.13579)" ),
        selectionFailValue = cms.double( 1000.0 ),
        selection = cms.string( "algoIs(\"kStrips\")" ),
        name = cms.string( "InStrip" ),
        plugin = cms.string( "RecoTauPiZeroStringQuality" )
      ),
      cms.PSet(  selectionPassFunction = cms.string( "abs(mass() - 0.13579)" ),
        selectionFailValue = cms.double( 1000.0 ),
        selection = cms.string( "abs(eta()) < 1.5 & abs(mass() - 0.13579) < 0.05" ),
        name = cms.string( "nearPiZeroMass" ),
        plugin = cms.string( "RecoTauPiZeroStringQuality" )
      ),
      cms.PSet(  selectionPassFunction = cms.string( "abs(mass() - 0.13579)" ),
        selectionFailValue = cms.double( 1000.0 ),
        selection = cms.string( "abs(eta()) > 1.5 & mass() < 0.2" ),
        name = cms.string( "nearPiZeroMass" ),
        plugin = cms.string( "RecoTauPiZeroStringQuality" )
      )
    ),
    jetRegionSrc = cms.InputTag( "hltTauPFJets08Region" ),
    outputSelection = cms.string( "pt > 1.5" ),
    jetSrc = cms.InputTag( "hltAntiKT5PFJetsForTaus" ),
    builders = cms.VPSet( 
      cms.PSet(  maxMass = cms.double( -1.0 ),
        plugin = cms.string( "RecoTauPiZeroCombinatoricPlugin" ),
        minMass = cms.double( 0.0 ),
        qualityCuts = cms.PSet(
          isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double( 0.2 ),
            minTrackPt = cms.double( 1.5 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            maxTrackChi2 = cms.double( 100.0 ),
            minTrackPixelHits = cms.uint32( 3 ),
            minGammaEt = cms.double( 1.5 ),
            minTrackHits = cms.uint32( 8 ),
            maxTransverseImpactParameter = cms.double( 0.05 )
          ),
          pvFindingAlgo = cms.string( "highestPtInEvent" ),
          primaryVertexSrc = cms.InputTag( "hltIsoMuonVertex" ),
          signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double( 0.4 ),
            minTrackPt = cms.double( 0.0 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            maxTrackChi2 = cms.double( 1000.0 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            maxTransverseImpactParameter = cms.double( 0.2 )
          )
        ),
        choose = cms.uint32( 2 ),
        maxInputGammas = cms.uint32( 10 ),
        name = cms.string( "2" )
      ), 
      cms.PSet(  name = cms.string( "s" ),
        stripPhiAssociationDistance = cms.double( 0.2 ),
        plugin = cms.string( "RecoTauPiZeroStripPlugin2" ),
        minGammaEtStripAdd = cms.double( 0.0 ),
        minGammaEtStripSeed = cms.double( 0.5 ),
        qualityCuts = cms.PSet(
          isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double( 0.2 ),
            minTrackPt = cms.double( 1.5 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            maxTrackChi2 = cms.double( 100.0 ),
            minTrackPixelHits = cms.uint32( 3 ),
            minGammaEt = cms.double( 1.5 ),
            minTrackHits = cms.uint32( 8 ),
            maxTransverseImpactParameter = cms.double( 0.05 )
          ),
          pvFindingAlgo = cms.string( "highestPtInEvent" ),
          primaryVertexSrc = cms.InputTag( "hltIsoMuonVertex" ),
          signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double( 0.4 ),
            minTrackPt = cms.double( 0.0 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            maxTrackChi2 = cms.double( 1000.0 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            maxTransverseImpactParameter = cms.double( 0.2 )
          )
        ),
        maxStripBuildIterations = cms.int32( -1 ),
        updateStripAfterEachDaughter = cms.bool( False ),
        makeCombinatoricStrips = cms.bool(False),
        applyElecTrackQcuts = cms.bool(False),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        minStripEt = cms.double(1.0),
        stripEtaAssociationDistance = cms.double(0.05)
      ) 
    )
)
process.hltPFTausNPSansRef = cms.EDProducer( "RecoTauProducer",
    piZeroSrc = cms.InputTag( "hltPFTauPiZeros" ),
    modifiers = cms.VPSet( 
      cms.PSet(  ElectronPreIDProducer = cms.InputTag( "elecpreid" ),
        name = cms.string( "fixedConeElectronRej" ),
        plugin = cms.string( "RecoTauElectronRejectionPlugin" ),
        DataType = cms.string( "AOD" ),
        maximumForElectrionPreIDOutput = cms.double( -0.1 ),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double( -0.1 ),
        ElecPreIDLeadTkMatch_maxDR = cms.double( 0.01 ),
        EcalStripSumE_minClusEnergy = cms.double( 0.1 ),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double( 0.5 ),
        EcalStripSumE_deltaEta = cms.double( 0.03 )
      )
    ),
    jetRegionSrc = cms.InputTag( "hltTauPFJets08Region" ),
    jetSrc = cms.InputTag( "hltAntiKT5PFJetsForTaus" ),
    builders = cms.VPSet( 
      cms.PSet(  usePFLeptons = cms.bool( True ),
        name = cms.string( "fixedCone" ),
        pfCandSrc = cms.InputTag( "hltParticleFlowForTaus" ),
        plugin = cms.string( "RecoTauBuilderConePlugin" ),
        signalConeNeutralHadrons = cms.string( "0.1" ),
        isoConeNeutralHadrons = cms.string( "0.5" ),
        isoConeChargedHadrons = cms.string( "0.45" ),
        isoConePiZeros = cms.string( "0.5" ),
        matchingCone = cms.string( "0.2" ),
        signalConeChargedHadrons = cms.string( "0.18" ),
        leadObjectPt = cms.double( 0.0 ),
        signalConePiZeros = cms.string( "0.18" ),
        qualityCuts = cms.PSet( 
          pvFindingAlgo = cms.string( "highestPtInEvent" ),
          primaryVertexSrc = cms.InputTag( "hltIsoMuonVertex" ),
          signalQualityCuts = cms.PSet( 
            minTrackPt = cms.double( 0.0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            minGammaEt = cms.double( 0.5 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackHits = cms.uint32( 3 ),
            maxDeltaZ = cms.double( 0.4 ),
            maxTransverseImpactParameter = cms.double( 0.2 )
          ),
          isolationQualityCuts = cms.PSet( 
            minTrackHits = cms.uint32( 8 ),
            minTrackPt = cms.double( 1.5 ),
            maxTrackChi2 = cms.double( 100.0 ),
            minTrackPixelHits = cms.uint32( 3 ),
            useTracksInsteadOfPFHadrons = cms.bool( False ),
            maxDeltaZ = cms.double( 0.2 ),
            maxTransverseImpactParameter = cms.double( 0.05 ),
            minGammaEt = cms.double( 0.5 )
          )
        )
      )
    ),
    buildNullTaus = cms.bool( True )
)
process.hltPFTausNP = cms.EDProducer( "RecoTauPiZeroUnembedder",
    src = cms.InputTag( "hltPFTausNPSansRef" )
)
process.hltPFTauTrackFindingDiscriminatorNP = process.hltPFTauTrackFindingDiscriminatorOffVtx.clone()
process.hltPFTauTrackFindingDiscriminatorNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauLooseIsolationDiscriminatorNP =  process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminatorNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauLooseIsolationDiscriminatorNP.qualityCuts.primaryVertexSrc = "hltIsoMuonVertex"
process.hltPFTauLooseIsolationDiscriminatorNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorNP"
process.hltPFTauLooseIsolationDiscriminator5hitsNP = process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator5hitsNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauLooseIsolationDiscriminator5hitsNP.qualityCuts.primaryVertexSrc = "hltIsoMuonVertex"
process.hltPFTauLooseIsolationDiscriminator5hitsNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorNP"
process.hltPFTauLooseIsolationDiscriminator3hitsNP = process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator3hitsNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauLooseIsolationDiscriminator3hitsNP.qualityCuts.primaryVertexSrc = "hltIsoMuonVertex"
process.hltPFTauLooseIsolationDiscriminator3hitsNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorNP"
process.hltPFTauECalIsolationDiscriminatorNP = process.hltPFTauECalIsolationDiscriminatorOffVtx.clone()
process.hltPFTauECalIsolationDiscriminatorNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauECalIsolationDiscriminatorNP.qualityCuts.primaryVertexSrc = "hltIsoMuonVertex"
process.hltPFTauECalIsolationDiscriminatorNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorNP"
process.hltPFTauTrkIsolationDiscriminatorNP = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminatorNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauTrkIsolationDiscriminatorNP.qualityCuts.primaryVertexSrc = "hltIsoMuonVertex"
process.hltPFTauTrkIsolationDiscriminatorNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorNP"
process.hltPFTauTrkIsolationDiscriminator5hitsNP = process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator5hitsNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauTrkIsolationDiscriminator5hitsNP.qualityCuts.primaryVertexSrc = "hltIsoMuonVertex"
process.hltPFTauTrkIsolationDiscriminator5hitsNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorNP"
process.hltPFTauTrkIsolationDiscriminator3hitsNP = process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator3hitsNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauTrkIsolationDiscriminator3hitsNP.qualityCuts.primaryVertexSrc = "hltIsoMuonVertex"
process.hltPFTauTrkIsolationDiscriminator3hitsNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorNP"
process.hltPFTauAgainstMuonDiscriminatorLooseNP = process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorLooseNP.PFTauProducer = "hltPFTausNP"
process.hltPFTauAgainstMuonDiscriminatorHoPNP = process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorHoPNP.PFTauProducer = "hltPFTausNP"

process.hltPFTauSequnceNP = cms.Sequence(
    process.hltTauPFJets08Region +
    process.hltPFTauPiZeros +
    process.hltPFTausNPSansRef +
    process.hltPFTausNP +
    process.hltPFTauTrackFindingDiscriminatorNP +
    process.hltPFTauLooseIsolationDiscriminatorNP + 
    process.hltPFTauLooseIsolationDiscriminator5hitsNP + 
    process.hltPFTauLooseIsolationDiscriminator3hitsNP + 
    process.hltPFTauECalIsolationDiscriminatorNP +
    process.hltPFTauTrkIsolationDiscriminatorNP +
    process.hltPFTauTrkIsolationDiscriminator5hitsNP +
    process.hltPFTauTrkIsolationDiscriminator3hitsNP
    + process.hltPFTauAgainstMuonDiscriminatorLooseNP
    + process.hltPFTauAgainstMuonDiscriminatorHoPNP
    )

#####
## New producer with online vertices
process.hltPFTauPiZerosOnl = process.hltPFTauPiZeros.clone()
process.hltPFTauPiZerosOnl.builders[0].qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauPiZerosOnl.builders[1].qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTausOnlNPSansRef = process.hltPFTausNPSansRef.clone()
process.hltPFTausOnlNPSansRef.piZeroSrc = "hltPFTauPiZerosOnl"
process.hltPFTausOnlNPSansRef.builders[0].qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTausOnlNP = process.hltPFTausNP.clone()
process.hltPFTausOnlNP.src = "hltPFTausOnlNPSansRef"
process.hltPFTauTrackFindingDiscriminatorOnlNP = process.hltPFTauTrackFindingDiscriminatorOffVtx.clone()
process.hltPFTauTrackFindingDiscriminatorOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauLooseIsolationDiscriminatorOnlNP =  process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminatorOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauLooseIsolationDiscriminatorOnlNP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminatorOnlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnlNP"
process.hltPFTauLooseIsolationDiscriminator5hitsOnlNP = process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator5hitsOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauLooseIsolationDiscriminator5hitsOnlNP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminator5hitsOnlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnlNP"
process.hltPFTauLooseIsolationDiscriminator3hitsOnlNP = process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator3hitsOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauLooseIsolationDiscriminator3hitsOnlNP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminator3hitsOnlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnlNP"
process.hltPFTauECalIsolationDiscriminatorOnlNP = process.hltPFTauECalIsolationDiscriminatorOffVtx.clone()
process.hltPFTauECalIsolationDiscriminatorOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauECalIsolationDiscriminatorOnlNP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauECalIsolationDiscriminatorOnlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnlNP"
process.hltPFTauTrkIsolationDiscriminatorOnlNP = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminatorOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauTrkIsolationDiscriminatorOnlNP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminatorOnlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnlNP"
process.hltPFTauTrkIsolationDiscriminator5hitsOnlNP = process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator5hitsOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauTrkIsolationDiscriminator5hitsOnlNP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminator5hitsOnlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnlNP"
process.hltPFTauTrkIsolationDiscriminator3hitsOnlNP = process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator3hitsOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauTrkIsolationDiscriminator3hitsOnlNP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminator3hitsOnlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnlNP"
process.hltPFTauAgainstMuonDiscriminatorLooseOnlNP = process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorLooseOnlNP.PFTauProducer = "hltPFTausOnlNP"
process.hltPFTauAgainstMuonDiscriminatorHoPOnlNP = process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorHoPOnlNP.PFTauProducer = "hltPFTausOnlNP"

process.hltPFTauSequnceOnlNP = cms.Sequence(
    process.hltTauPFJets08Region +
    process.hltPFTauPiZerosOnl +
    process.hltPFTausOnlNPSansRef +
    process.hltPFTausOnlNP +
    process.hltPFTauTrackFindingDiscriminatorOnlNP +
    process.hltPFTauLooseIsolationDiscriminatorOnlNP + 
    process.hltPFTauLooseIsolationDiscriminator5hitsOnlNP + 
    process.hltPFTauLooseIsolationDiscriminator3hitsOnlNP + 
    process.hltPFTauECalIsolationDiscriminatorOnlNP +
    process.hltPFTauTrkIsolationDiscriminatorOnlNP +
    process.hltPFTauTrkIsolationDiscriminator5hitsOnlNP +
    process.hltPFTauTrkIsolationDiscriminator3hitsOnlNP
    +process.hltPFTauAgainstMuonDiscriminatorLooseOnlNP
    +process.hltPFTauAgainstMuonDiscriminatorHoPOnlNP
    )
#####
## New producer with online vertices comb sorting
process.hltPFTauPiZerosOnl2 = process.hltPFTauPiZeros.clone()
process.hltPFTauPiZerosOnl2.builders[0].qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauPiZerosOnl2.builders[0].qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauPiZerosOnl2.builders[1].qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauPiZerosOnl2.builders[0].qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTausOnl2NPSansRef = process.hltPFTausNPSansRef.clone()
process.hltPFTausOnl2NPSansRef.piZeroSrc = "hltPFTauPiZerosOnl2"
process.hltPFTausOnl2NPSansRef.builders[0].qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTausOnl2NPSansRef.builders[0].qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTausOnl2NP = process.hltPFTausNP.clone()
process.hltPFTausOnl2NP.src = "hltPFTausOnl2NPSansRef"
process.hltPFTauTrackFindingDiscriminatorOnl2NP = process.hltPFTauTrackFindingDiscriminatorOffVtx.clone()
process.hltPFTauTrackFindingDiscriminatorOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauLooseIsolationDiscriminatorOnl2NP =  process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminatorOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauLooseIsolationDiscriminatorOnl2NP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminatorOnl2NP.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauLooseIsolationDiscriminatorOnl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnl2NP"
process.hltPFTauLooseIsolationDiscriminator5hitsOnl2NP = process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator5hitsOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauLooseIsolationDiscriminator5hitsOnl2NP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminator5hitsOnl2NP.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauLooseIsolationDiscriminator5hitsOnl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnl2NP"
process.hltPFTauLooseIsolationDiscriminator3hitsOnl2NP = process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator3hitsOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauLooseIsolationDiscriminator3hitsOnl2NP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminator3hitsOnl2NP.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauLooseIsolationDiscriminator3hitsOnl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnl2NP"
process.hltPFTauECalIsolationDiscriminatorOnl2NP = process.hltPFTauECalIsolationDiscriminatorOffVtx.clone()
process.hltPFTauECalIsolationDiscriminatorOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauECalIsolationDiscriminatorOnl2NP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauECalIsolationDiscriminatorOnl2NP.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauECalIsolationDiscriminatorOnl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnl2NP"
process.hltPFTauTrkIsolationDiscriminatorOnl2NP = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminatorOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauTrkIsolationDiscriminatorOnl2NP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminatorOnl2NP.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauTrkIsolationDiscriminatorOnl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnl2NP"
process.hltPFTauTrkIsolationDiscriminator5hitsOnl2NP = process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator5hitsOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauTrkIsolationDiscriminator5hitsOnl2NP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminator5hitsOnl2NP.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauTrkIsolationDiscriminator5hitsOnl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnl2NP"
process.hltPFTauTrkIsolationDiscriminator3hitsOnl2NP = process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator3hitsOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauTrkIsolationDiscriminator3hitsOnl2NP.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminator3hitsOnl2NP.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauTrkIsolationDiscriminator3hitsOnl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorOnl2NP"
process.hltPFTauAgainstMuonDiscriminatorLooseOnl2NP = process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorLooseOnl2NP.PFTauProducer = "hltPFTausOnl2NP"
process.hltPFTauAgainstMuonDiscriminatorHoPOnl2NP = process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorHoPOnl2NP.PFTauProducer = "hltPFTausOnl2NP"

process.hltPFTauSequnceOnl2NP = cms.Sequence(
    process.hltTauPFJets08Region +
    process.hltPFTauPiZerosOnl2 +
    process.hltPFTausOnl2NPSansRef +
    process.hltPFTausOnl2NP +
    process.hltPFTauTrackFindingDiscriminatorOnl2NP +
    process.hltPFTauLooseIsolationDiscriminatorOnl2NP + 
    process.hltPFTauLooseIsolationDiscriminator5hitsOnl2NP + 
    process.hltPFTauLooseIsolationDiscriminator3hitsOnl2NP + 
    process.hltPFTauECalIsolationDiscriminatorOnl2NP +
    process.hltPFTauTrkIsolationDiscriminatorOnl2NP +
    process.hltPFTauTrkIsolationDiscriminator5hitsOnl2NP +
    process.hltPFTauTrkIsolationDiscriminator3hitsOnl2NP
    + process.hltPFTauAgainstMuonDiscriminatorLooseOnl2NP
    + process.hltPFTauAgainstMuonDiscriminatorHoPOnl2NP
    )
#####
## New producer with pixel vertices
process.hltPFTauPiZerosPxl = process.hltPFTauPiZeros.clone()
process.hltPFTauPiZerosPxl.builders[0].qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauPiZerosPxl.builders[1].qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTausPxlNPSansRef = process.hltPFTausNPSansRef.clone()
process.hltPFTausPxlNPSansRef.piZeroSrc = "hltPFTauPiZerosPxl"
process.hltPFTausPxlNPSansRef.builders[0].qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTausPxlNP = process.hltPFTausNP.clone()
process.hltPFTausPxlNP.src = "hltPFTausPxlNPSansRef"
process.hltPFTauTrackFindingDiscriminatorPxlNP = process.hltPFTauTrackFindingDiscriminatorOffVtx.clone()
process.hltPFTauTrackFindingDiscriminatorPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauLooseIsolationDiscriminatorPxlNP =  process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminatorPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauLooseIsolationDiscriminatorPxlNP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauLooseIsolationDiscriminatorPxlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxlNP"
process.hltPFTauLooseIsolationDiscriminator5hitsPxlNP = process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator5hitsPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauLooseIsolationDiscriminator5hitsPxlNP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauLooseIsolationDiscriminator5hitsPxlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxlNP"
process.hltPFTauLooseIsolationDiscriminator3hitsPxlNP = process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator3hitsPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauLooseIsolationDiscriminator3hitsPxlNP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauLooseIsolationDiscriminator3hitsPxlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxlNP"
process.hltPFTauECalIsolationDiscriminatorPxlNP = process.hltPFTauECalIsolationDiscriminatorOffVtx.clone()
process.hltPFTauECalIsolationDiscriminatorPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauECalIsolationDiscriminatorPxlNP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauECalIsolationDiscriminatorPxlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxlNP"
process.hltPFTauTrkIsolationDiscriminatorPxlNP = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminatorPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauTrkIsolationDiscriminatorPxlNP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauTrkIsolationDiscriminatorPxlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxlNP"
process.hltPFTauTrkIsolationDiscriminator5hitsPxlNP = process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator5hitsPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauTrkIsolationDiscriminator5hitsPxlNP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauTrkIsolationDiscriminator5hitsPxlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxlNP"
process.hltPFTauTrkIsolationDiscriminator3hitsPxlNP = process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator3hitsPxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauTrkIsolationDiscriminator3hitsPxlNP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauTrkIsolationDiscriminator3hitsPxlNP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxlNP"
process.hltPFTauAgainstMuonDiscriminatorLoosePxlNP = process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorLoosePxlNP.PFTauProducer = "hltPFTausPxlNP"
process.hltPFTauAgainstMuonDiscriminatorHoPPxlNP = process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorHoPPxlNP.PFTauProducer = "hltPFTausPxlNP"


process.hltPFTauSequncePxlNP = cms.Sequence(
    process.hltTauPFJets08Region +
    process.hltPFTauPiZerosPxl +
    process.hltPFTausPxlNPSansRef +
    process.hltPFTausPxlNP +
    process.hltPFTauTrackFindingDiscriminatorPxlNP +
    process.hltPFTauLooseIsolationDiscriminatorPxlNP + 
    process.hltPFTauLooseIsolationDiscriminator5hitsPxlNP + 
    process.hltPFTauLooseIsolationDiscriminator3hitsPxlNP + 
    process.hltPFTauECalIsolationDiscriminatorPxlNP +
    process.hltPFTauTrkIsolationDiscriminatorPxlNP +
    process.hltPFTauTrkIsolationDiscriminator5hitsPxlNP +
    process.hltPFTauTrkIsolationDiscriminator3hitsPxlNP
    +process.hltPFTauAgainstMuonDiscriminatorLoosePxlNP
    +process.hltPFTauAgainstMuonDiscriminatorHoPPxlNP
    )

####### New producer with pixel vertices
process.hltPFTauPiZerosPxl2 = process.hltPFTauPiZeros.clone()
process.hltPFTauPiZerosPxl2.builders[0].qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauPiZerosPxl2.builders[0].qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauPiZerosPxl2.builders[1].qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauPiZerosPxl2.builders[1].qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTausPxl2NPSansRef = process.hltPFTausNPSansRef.clone()
process.hltPFTausPxl2NPSansRef.piZeroSrc = "hltPFTauPiZerosPxl2"
process.hltPFTausPxl2NPSansRef.builders[0].qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTausPxl2NPSansRef.builders[0].qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTausPxl2NP = process.hltPFTausNP.clone()
process.hltPFTausPxl2NP.src = "hltPFTausPxl2NPSansRef"
process.hltPFTauTrackFindingDiscriminatorPxl2NP = process.hltPFTauTrackFindingDiscriminatorOffVtx.clone()
process.hltPFTauTrackFindingDiscriminatorPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauLooseIsolationDiscriminatorPxl2NP =  process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminatorPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauLooseIsolationDiscriminatorPxl2NP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauLooseIsolationDiscriminatorPxl2NP.qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauLooseIsolationDiscriminatorPxl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxl2NP"
process.hltPFTauLooseIsolationDiscriminator5hitsPxl2NP = process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator5hitsPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauLooseIsolationDiscriminator5hitsPxl2NP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauLooseIsolationDiscriminator5hitsPxl2NP.qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauLooseIsolationDiscriminator5hitsPxl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxl2NP"
process.hltPFTauLooseIsolationDiscriminator3hitsPxl2NP = process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator3hitsPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauLooseIsolationDiscriminator3hitsPxl2NP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauLooseIsolationDiscriminator3hitsPxl2NP.qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauLooseIsolationDiscriminator3hitsPxl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxl2NP"
process.hltPFTauECalIsolationDiscriminatorPxl2NP = process.hltPFTauECalIsolationDiscriminatorOffVtx.clone()
process.hltPFTauECalIsolationDiscriminatorPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauECalIsolationDiscriminatorPxl2NP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauECalIsolationDiscriminatorPxl2NP.qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauECalIsolationDiscriminatorPxl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxl2NP"
process.hltPFTauTrkIsolationDiscriminatorPxl2NP = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminatorPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauTrkIsolationDiscriminatorPxl2NP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauTrkIsolationDiscriminatorPxl2NP.qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauTrkIsolationDiscriminatorPxl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxl2NP"
process.hltPFTauTrkIsolationDiscriminator5hitsPxl2NP = process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator5hitsPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauTrkIsolationDiscriminator5hitsPxl2NP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauTrkIsolationDiscriminator5hitsPxl2NP.qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauTrkIsolationDiscriminator5hitsPxl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxl2NP"
process.hltPFTauTrkIsolationDiscriminator3hitsPxl2NP = process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator3hitsPxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauTrkIsolationDiscriminator3hitsPxl2NP.qualityCuts.primaryVertexSrc = "hltPixelVertices"
process.hltPFTauTrkIsolationDiscriminator3hitsPxl2NP.qualityCuts.pvFindingAlgo = "closestInDeltaZ" #MB: "combined" does not exist with tags in the release, replaxed by pixelVtx un-friendly one. To be rechecked with "closestInDeltaZ". Also quality cuts for track for vtx finding to be reconsidered
process.hltPFTauTrkIsolationDiscriminator3hitsPxl2NP.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorPxl2NP"
process.hltPFTauAgainstMuonDiscriminatorLoosePxl2NP = process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorLoosePxl2NP.PFTauProducer = "hltPFTausPxl2NP"
process.hltPFTauAgainstMuonDiscriminatorHoPPxl2NP = process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorHoPPxl2NP.PFTauProducer = "hltPFTausPxl2NP"

process.hltPFTauSequncePxl2NP = cms.Sequence(
    process.hltTauPFJets08Region +
    process.hltPFTauPiZerosPxl2 +
    process.hltPFTausPxl2NPSansRef +
    process.hltPFTausPxl2NP +
    process.hltPFTauTrackFindingDiscriminatorPxl2NP +
    process.hltPFTauLooseIsolationDiscriminatorPxl2NP + 
    process.hltPFTauLooseIsolationDiscriminator5hitsPxl2NP + 
    process.hltPFTauLooseIsolationDiscriminator3hitsPxl2NP + 
    process.hltPFTauECalIsolationDiscriminatorPxl2NP +
    process.hltPFTauTrkIsolationDiscriminatorPxl2NP +
    process.hltPFTauTrkIsolationDiscriminator5hitsPxl2NP +
    process.hltPFTauTrkIsolationDiscriminator3hitsPxl2NP
    +process.hltPFTauAgainstMuonDiscriminatorLoosePxl2NP
    +process.hltPFTauAgainstMuonDiscriminatorHoPPxl2NP
    )

#####
## New producer with online vertices, HPS
process.hltCombinatoricRecoTaus = cms.EDProducer(
    "RecoTauProducer",
    piZeroSrc = cms.InputTag("hltPFTauPiZerosOnl2"),
    modifiers = cms.VPSet(
       cms.PSet(
          plugin = cms.string('RecoTauImpactParameterSignificancePlugin'),
          name = cms.string('sipt'),
          qualityCuts = process.hltPFTauPiZerosOnl2.builders[0].qualityCuts
       ),
       cms.PSet(
          ElectronPreIDProducer = cms.InputTag("elecpreid"),
          name = cms.string('elec_rej'),
          plugin = cms.string('RecoTauElectronRejectionPlugin'),
          DataType = cms.string('AOD'),
          maximumForElectrionPreIDOutput = cms.double(-0.1),
          EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
          EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
          EcalStripSumE_minClusEnergy = cms.double(0.1),
          ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
          EcalStripSumE_deltaEta = cms.double(0.03)
       ),
       cms.PSet(
          dRcone = cms.double(0.12),
          name = cms.string('tau_en_recovery'),
          plugin = cms.string('RecoTauEnergyRecoveryPlugin2')
          ),
       #cms.PSet( #MB assume that TauTagInfo not mandatory for HPS
       #   pfTauTagInfoSrc = cms.InputTag("pfRecoTauTagInfoProducer"),
       #   name = cms.string('TTIworkaround'),
       #   plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
       #)
    ),
    jetRegionSrc = cms.InputTag("hltTauPFJets08Region"),
    jetSrc = cms.InputTag("hltAntiKT5PFJetsForTaus"),
    builders = cms.VPSet(
       cms.PSet(
           usePFLeptons = cms.bool(True),
           name = cms.string('combinatoric'),
           plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
           qualityCuts = process.hltPFTauPiZerosOnl2.builders[0].qualityCuts,
           decayModes = cms.VPSet(
              cms.PSet(
                 nPiZeros = cms.uint32(0),
                 nCharged = cms.uint32(1),
                 maxPiZeros = cms.uint32(0),
                 maxTracks = cms.uint32(6)
              ),
              cms.PSet(
                 nPiZeros = cms.uint32(1),
                 nCharged = cms.uint32(1),
                 maxPiZeros = cms.uint32(6),
                 maxTracks = cms.uint32(6)
              ),
              cms.PSet(
                 nPiZeros = cms.uint32(2),
                 nCharged = cms.uint32(1),
                 maxPiZeros = cms.uint32(5),
                 maxTracks = cms.uint32(6)
              ),
              cms.PSet(
                 nPiZeros = cms.uint32(0),
                 nCharged = cms.uint32(3),
                 maxPiZeros = cms.uint32(0),
                 maxTracks = cms.uint32(6)
              )
           ),
           isolationConeSize = cms.double(0.5),
           pfCandSrc = cms.InputTag("hltParticleFlowForTaus")
       )
    ),
    buildNullTaus = cms.bool(True)
)
process.hltHpsSelectionDiscriminator = cms.EDProducer(
    "PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hltCombinatoricRecoTaus"),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and')
    ),
    minTauPt = cms.double(0.0),
    coneSizeFormula = cms.string('max(min(0.1, 2.8/pt()),0.05)'),
    matchingCone = cms.double(0.1),
    decayModes = cms.VPSet(
       cms.PSet(
          nPiZeros = cms.uint32(0),
          minMass = cms.double(-1000.0),
          maxMass = cms.string('1.'),
          nCharged = cms.uint32(1)
       ),
       cms.PSet(
          nPiZeros = cms.uint32(1),
          assumeStripMass = cms.double(0.1349),
          minMass = cms.double(0.3),
          maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/200.), 2.1))'),
          nCharged = cms.uint32(1)
       ),
       cms.PSet(
          minPi0Mass = cms.double(0.05),
          maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/200.), 2.0))'),
          maxPi0Mass = cms.double(0.2),
          nPiZeros = cms.uint32(2),
          minMass = cms.double(0.4),
          nCharged = cms.uint32(1),
          assumeStripMass = cms.double(0.0)
       ),
       cms.PSet(
          nPiZeros = cms.uint32(0),
          minMass = cms.double(0.8),
          maxMass = cms.string('1.5'),
          nCharged = cms.uint32(3)
       )
    )
)                              
process.hltPFTausHPSSansRef = cms.EDProducer(
    "RecoTauCleaner",
    cleaners = cms.VPSet(
       cms.PSet(
          selectionPassFunction = cms.string('abs(charge())-1'),
          selection = cms.string('signalPFChargedHadrCands().size() = 3'),
          name = cms.string('UnitCharge'),
          plugin = cms.string('RecoTauStringCleanerPlugin'),
          selectionFailValue = cms.double(0)
       ),
       cms.PSet(
          selectionPassFunction = cms.string('0'),
          selection = cms.string('signalPiZeroCandidates().size() = 0 | signalPiZeroCandidates()[0].pt > 2.5'),
          name = cms.string('leadStripPtLt2_5'),
          plugin = cms.string('RecoTauStringCleanerPlugin'),
          selectionFailValue = cms.double(1000.0)
       ),
       cms.PSet(
          src = cms.InputTag("hltHpsSelectionDiscriminator"),
          name = cms.string('HPS_Select'),
          plugin = cms.string('RecoTauDiscriminantCleanerPlugin')
          ),
       cms.PSet(
          selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum()+isolationPFGammaCandsEtSum()'),
          selection = cms.string('leadPFCand().isNonnull()'),
          name = cms.string('CombinedIsolation'),
          plugin = cms.string('RecoTauStringCleanerPlugin'),
          selectionFailValue = cms.double(1000.0)
       )
    ),
    src = cms.InputTag("hltCombinatoricRecoTaus")
)
process.hltPFTausHPS = cms.EDProducer(
    "RecoTauPiZeroUnembedder",
    src = cms.InputTag("hltPFTausHPSSansRef")
)
process.hltPFTauTrackFindingDiscriminatorHPS = cms.EDProducer(
    "PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hltPFTausHPS"),
    Prediscriminants = cms.PSet(
       BooleanOperator = cms.string('and')
    ),
    minTauPt = cms.double(0.0),
    coneSizeFormula = cms.string('max(min(0.1, 2.8/pt()),0.05)'),
    decayModes = cms.VPSet(
       cms.PSet(
          nPiZeros = cms.uint32(0),
          minMass = cms.double(-1000.0),
          maxMass = cms.string('1.'),
          nCharged = cms.uint32(1)
       ),
       cms.PSet(
          nPiZeros = cms.uint32(1),
          assumeStripMass = cms.double(0.1349),
          minMass = cms.double(0.3),
          maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/200.), 2.1))'),
          nCharged = cms.uint32(1)
       ),
       cms.PSet(
          minPi0Mass = cms.double(0.05),
          maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/200.), 2.0))'),
          maxPi0Mass = cms.double(0.2),
          nPiZeros = cms.uint32(2),
          minMass = cms.double(0.4),
          nCharged = cms.uint32(1),
          assumeStripMass = cms.double(0.0)
          ),
       cms.PSet(
          nPiZeros = cms.uint32(0),
          minMass = cms.double(0.8),
          maxMass = cms.string('1.5'),
          nCharged = cms.uint32(3)
       )
    ),
    matchingCone = cms.double(0.1)
)
process.hltPFTauLooseIsolationDiscriminatorHPS =  process.hltPFTauLooseIsolationDiscriminatorOffVtx.clone()
process.hltPFTauLooseIsolationDiscriminatorHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauLooseIsolationDiscriminatorHPS.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminatorHPS.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack"
process.hltPFTauLooseIsolationDiscriminatorHPS.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorHPS"
process.hltPFTauLooseIsolationDiscriminator5hitsHPS = process.hltPFTauLooseIsolationDiscriminator5hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator5hitsHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauLooseIsolationDiscriminator5hitsHPS.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminator5hitsHPS.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack"
process.hltPFTauLooseIsolationDiscriminator5hitsHPS.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorHPS"
process.hltPFTauLooseIsolationDiscriminator3hitsHPS = process.hltPFTauLooseIsolationDiscriminator3hitsOffVtx.clone() 
process.hltPFTauLooseIsolationDiscriminator3hitsHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauLooseIsolationDiscriminator3hitsHPS.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauLooseIsolationDiscriminator3hitsHPS.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack"
process.hltPFTauLooseIsolationDiscriminator3hitsHPS.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorHPS"
process.hltPFTauECalIsolationDiscriminatorHPS = process.hltPFTauECalIsolationDiscriminatorOffVtx.clone()
process.hltPFTauECalIsolationDiscriminatorHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauECalIsolationDiscriminatorHPS.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauECalIsolationDiscriminatorHPS.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack"
process.hltPFTauECalIsolationDiscriminatorHPS.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorHPS"
process.hltPFTauTrkIsolationDiscriminatorHPS = process.hltPFTauTrkIsolationDiscriminatorOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminatorHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauTrkIsolationDiscriminatorHPS.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminatorHPS.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack"
process.hltPFTauTrkIsolationDiscriminatorHPS.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorHPS"
process.hltPFTauTrkIsolationDiscriminator5hitsHPS = process.hltPFTauTrkIsolationDiscriminator5hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator5hitsHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauTrkIsolationDiscriminator5hitsHPS.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminator5hitsHPS.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack"
process.hltPFTauTrkIsolationDiscriminator5hitsHPS.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorHPS"
process.hltPFTauTrkIsolationDiscriminator3hitsHPS = process.hltPFTauTrkIsolationDiscriminator3hitsOffVtx.clone()
process.hltPFTauTrkIsolationDiscriminator3hitsHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauTrkIsolationDiscriminator3hitsHPS.qualityCuts.primaryVertexSrc = "hltOnlinePrimaryVertices"
process.hltPFTauTrkIsolationDiscriminator3hitsHPS.qualityCuts.pvFindingAlgo = "highestWeightForLeadTrack"
process.hltPFTauTrkIsolationDiscriminator3hitsHPS.Prediscriminants.leadTrack.Producer = "hltPFTauTrackFindingDiscriminatorHPS"
process.hltPFTauAgainstMuonDiscriminatorLooseHPS = process.hltPFTauAgainstMuonDiscriminatorLooseOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorLooseHPS.PFTauProducer = "hltPFTausHPS"
process.hltPFTauAgainstMuonDiscriminatorHoPHPS = process.hltPFTauAgainstMuonDiscriminatorHoPOffVtx.clone()
process.hltPFTauAgainstMuonDiscriminatorHoPHPS.PFTauProducer = "hltPFTausHPS"

process.hltPFTauSequnceHPS = cms.Sequence(
    process.hltTauPFJets08Region +
    process.hltPFTauPiZerosOnl +
    process.hltCombinatoricRecoTaus +
    process.hltHpsSelectionDiscriminator +
    process.hltPFTausHPSSansRef +
    process.hltPFTausHPS +
    process.hltPFTauTrackFindingDiscriminatorHPS +
    process.hltPFTauLooseIsolationDiscriminatorHPS + 
    process.hltPFTauLooseIsolationDiscriminator5hitsHPS + 
    process.hltPFTauLooseIsolationDiscriminator3hitsHPS + 
    process.hltPFTauECalIsolationDiscriminatorHPS +
    process.hltPFTauTrkIsolationDiscriminatorHPS +
    process.hltPFTauTrkIsolationDiscriminator5hitsHPS +
    process.hltPFTauTrkIsolationDiscriminator3hitsHPS
    +process.hltPFTauAgainstMuonDiscriminatorLooseHPS
    +process.hltPFTauAgainstMuonDiscriminatorHoPHPS
    )

#########################
## PAT taus from HLT taus

#generic configuration for tauId
tauIdGeneric = cms.PSet(
        # configure many IDs as InputTag <someName> = <someTag>
        # you can comment out those you don't want to save some
        # disk space
        decayModeFinding = cms.InputTag("hltPFTauTrackFindingDiscriminatorGeneric"),
        byIsolation = cms.InputTag("hltPFTauLooseIsolationDiscriminatorGeneric"),
        byECalIsolation = cms.InputTag("hltPFTauECalIsolationDiscriminatorGeneric"),
        byTrkIsolation = cms.InputTag("hltPFTauTrkIsolationDiscriminatorGeneric"),
)

hltPatTausGeneric = cms.EDProducer(
    "PATTauProducer",
    # input
    tauSource = cms.InputTag("hltPFTausGeneric"),
    # add user data
    userData = cms.PSet(
      # add custom classes here
      userClasses = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add doubles here
      userFloats = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add ints here
      userInts = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add candidate ptrs here
      userCands = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add "inline" functions here
      userFunctions = cms.vstring(),
      userFunctionLabels = cms.vstring()
    ),
    # jet energy corrections
    addTauJetCorrFactors = cms.bool(False),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    # embedding objects (for Calo- and PFTaus)
    embedLeadTrack = cms.bool(False), ## embed in AOD externally stored leading track
    embedSignalTracks = cms.bool(False), ## embed in AOD externally stored signal tracks
    embedIsolationTracks = cms.bool(False), ## embed in AOD externally stored isolation tracks
    # embedding objects (for PFTaus only)
    embedLeadPFCand = cms.bool(False), ## embed in AOD externally stored leading PFCandidate
    embedLeadPFChargedHadrCand = cms.bool(False), ## embed in AOD externally stored leading PFChargedHadron candidate
    embedLeadPFNeutralCand = cms.bool(False), ## embed in AOD externally stored leading PFNeutral Candidate
    embedSignalPFCands = cms.bool(False), ## embed in AOD externally stored signal PFCandidates
    embedSignalPFChargedHadrCands = cms.bool(False), ## embed in AOD externally stored signal PFChargedHadronCandidates
    embedSignalPFNeutralHadrCands = cms.bool(False), ## embed in AOD externally stored signal PFNeutralHadronCandidates
    embedSignalPFGammaCands = cms.bool(False), ## embed in AOD externally stored signal PFGammaCandidates
    embedIsolationPFCands = cms.bool(False), ## embed in AOD externally stored isolation PFCandidates
    embedIsolationPFChargedHadrCands = cms.bool(False), ## embed in AOD externally stored isolation PFChargedHadronCandidates
    embedIsolationPFNeutralHadrCands = cms.bool(False), ## embed in AOD externally stored isolation PFNeutralHadronCandidates
    embedIsolationPFGammaCands = cms.bool(False), ## embed in AOD externally stored isolation PFGammaCandidates

    # embed IsoDeposits
    isoDeposits = cms.PSet(),
    # user defined isolation variables the variables defined here will be accessible
    # via pat::Tau::userIsolation(IsolationKeys key) with the key as defined in
    # DataFormats/PatCandidates/interface/Isolation.h
    #
    # (set Pt thresholds for PFChargedHadrons (PFGammas) to 1.0 (1.5) GeV,
    # matching the thresholds used when computing the tau iso. discriminators
    # in RecoTauTag/RecoTau/python/PFRecoTauDiscriminationByIsolation_cfi.py)
    userIsolation = cms.PSet(),
    # tau ID (for efficiency studies)
    addTauID     = cms.bool(True),
    tauIDSources = tauIdGeneric,
    # mc matching configurables
    addGenMatch      = cms.bool(False),
    embedGenMatch    = cms.bool(False),
    genParticleMatch = cms.InputTag(""),
    addGenJetMatch   = cms.bool(False),
    embedGenJetMatch = cms.bool(False),
    genJetMatch      = cms.InputTag(""),
    # efficiencies
    addEfficiencies = cms.bool(False),
    efficiencies    = cms.PSet(),
    # resolution
    addResolutions  = cms.bool(False),
    resolutions     = cms.PSet()
)
###
process.selectedHltPatTaus = cms.EDFilter(
    "PATTauSelector",
    src = cms.InputTag("hltPatTaus"),
    cut = cms.string("pt>17"),
    filter = cms.bool(False)
    )
###
process.hltPatTausNP = hltPatTausGeneric.clone(tauSource = 'hltPFTausNP')
process.hltPatTausNP.tauIDSources = cms.PSet(
        decayModeFinding = cms.InputTag("hltPFTauTrackFindingDiscriminatorNP"),
        byIsolation = cms.InputTag("hltPFTauLooseIsolationDiscriminatorNP"),
        byIsolation5hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator5hitsNP"),
        byIsolation3hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator3hitsNP"),
        byECalIsolation = cms.InputTag("hltPFTauECalIsolationDiscriminatorNP"),
        byTrkIsolation = cms.InputTag("hltPFTauTrkIsolationDiscriminatorNP"),
        byTrkIsolation5hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator5hitsNP"),
        byTrkIsolation3hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator3hitsNP"),
        againstMuonLoose = cms.InputTag("hltPFTauAgainstMuonDiscriminatorLooseNP"),
        againstMuonHoP = cms.InputTag("hltPFTauAgainstMuonDiscriminatorHoPNP"),
        )
process.selectedHltPatTausNP = process.selectedHltPatTaus.clone(src='hltPatTausNP')

###
process.hltPatTausOnlNP = hltPatTausGeneric.clone(tauSource = 'hltPFTausOnlNP')
process.hltPatTausOnlNP.tauIDSources = cms.PSet(
        decayModeFinding = cms.InputTag("hltPFTauTrackFindingDiscriminatorOnlNP"),
        byIsolation = cms.InputTag("hltPFTauLooseIsolationDiscriminatorOnlNP"),
        byIsolation5hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator5hitsOnlNP"),
        byIsolation3hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator3hitsOnlNP"),
        byECalIsolation = cms.InputTag("hltPFTauECalIsolationDiscriminatorOnlNP"),
        byTrkIsolation = cms.InputTag("hltPFTauTrkIsolationDiscriminatorOnlNP"),
        byTrkIsolation5hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator5hitsOnlNP"),
        byTrkIsolation3hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator3hitsOnlNP"),
        againstMuonLoose = cms.InputTag("hltPFTauAgainstMuonDiscriminatorLooseOnlNP"),
        againstMuonHoP = cms.InputTag("hltPFTauAgainstMuonDiscriminatorHoPOnlNP"),
        )
process.selectedHltPatTausOnlNP = process.selectedHltPatTaus.clone(src='hltPatTausOnlNP')

######
process.hltPatTausOnl2NP = hltPatTausGeneric.clone(tauSource = 'hltPFTausOnl2NP')
process.hltPatTausOnl2NP.tauIDSources = cms.PSet(
        decayModeFinding = cms.InputTag("hltPFTauTrackFindingDiscriminatorOnl2NP"),
        byIsolation = cms.InputTag("hltPFTauLooseIsolationDiscriminatorOnl2NP"),
        byIsolation5hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator5hitsOnl2NP"),
        byIsolation3hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator3hitsOnl2NP"),
        byECalIsolation = cms.InputTag("hltPFTauECalIsolationDiscriminatorOnl2NP"),
        byTrkIsolation = cms.InputTag("hltPFTauTrkIsolationDiscriminatorOnl2NP"),
        byTrkIsolation5hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator5hitsOnl2NP"),
        byTrkIsolation3hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator3hitsOnl2NP"),
        againstMuonLoose = cms.InputTag("hltPFTauAgainstMuonDiscriminatorLooseOnl2NP"),
        againstMuonHoP = cms.InputTag("hltPFTauAgainstMuonDiscriminatorHoPOnl2NP"),
        )
process.selectedHltPatTausOnl2NP = process.selectedHltPatTaus.clone(src='hltPatTausOnl2NP')

###
process.hltPatTausPxlNP = hltPatTausGeneric.clone(tauSource = 'hltPFTausPxlNP')
process.hltPatTausPxlNP.tauIDSources = cms.PSet(
        decayModeFinding = cms.InputTag("hltPFTauTrackFindingDiscriminatorPxlNP"),
        byIsolation = cms.InputTag("hltPFTauLooseIsolationDiscriminatorPxlNP"),
        byIsolation5hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator5hitsPxlNP"),
        byIsolation3hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator3hitsPxlNP"),
        byECalIsolation = cms.InputTag("hltPFTauECalIsolationDiscriminatorPxlNP"),
        byTrkIsolation = cms.InputTag("hltPFTauTrkIsolationDiscriminatorPxlNP"),
        byTrkIsolation5hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator5hitsPxlNP"),
        byTrkIsolation3hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator3hitsPxlNP"),
        againstMuonLoose = cms.InputTag("hltPFTauAgainstMuonDiscriminatorLoosePxlNP"),
        againstMuonHoP = cms.InputTag("hltPFTauAgainstMuonDiscriminatorHoPPxlNP"),
        )
process.selectedHltPatTausPxlNP = process.selectedHltPatTaus.clone(src='hltPatTausPxlNP')

###
process.hltPatTausPxl2NP = hltPatTausGeneric.clone(tauSource = 'hltPFTausPxl2NP')
process.hltPatTausPxl2NP.tauIDSources = cms.PSet(
        decayModeFinding = cms.InputTag("hltPFTauTrackFindingDiscriminatorPxl2NP"),
        byIsolation = cms.InputTag("hltPFTauLooseIsolationDiscriminatorPxl2NP"),
        byIsolation5hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator5hitsPxl2NP"),
        byIsolation3hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator3hitsPxl2NP"),
        byECalIsolation = cms.InputTag("hltPFTauECalIsolationDiscriminatorPxl2NP"),
        byTrkIsolation = cms.InputTag("hltPFTauTrkIsolationDiscriminatorPxl2NP"),
        byTrkIsolation5hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator5hitsPxl2NP"),
        byTrkIsolation3hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator3hitsPxl2NP"),
        againstMuonLoose = cms.InputTag("hltPFTauAgainstMuonDiscriminatorLoosePxl2NP"),
        againstMuonHoP = cms.InputTag("hltPFTauAgainstMuonDiscriminatorHoPPxl2NP"),
        )
process.selectedHltPatTausPxl2NP = process.selectedHltPatTaus.clone(src='hltPatTausPxl2NP')

###
process.hltPatTausHPS = hltPatTausGeneric.clone(tauSource = 'hltPFTausHPS')
process.hltPatTausHPS.tauIDSources = cms.PSet(
        decayModeFinding = cms.InputTag("hltPFTauTrackFindingDiscriminatorHPS"),
        byIsolation = cms.InputTag("hltPFTauLooseIsolationDiscriminatorHPS"),
        byIsolation5hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator5hitsHPS"),
        byIsolation3hits = cms.InputTag("hltPFTauLooseIsolationDiscriminator3hitsHPS"),
        byECalIsolation = cms.InputTag("hltPFTauECalIsolationDiscriminatorHPS"),
        byTrkIsolation = cms.InputTag("hltPFTauTrkIsolationDiscriminatorHPS"),
        byTrkIsolation5hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator5hitsHPS"),
        byTrkIsolation3hits = cms.InputTag("hltPFTauTrkIsolationDiscriminator3hitsHPS"),
        againstMuonLoose = cms.InputTag("hltPFTauAgainstMuonDiscriminatorLooseHPS"),
        againstMuonHoP = cms.InputTag("hltPFTauAgainstMuonDiscriminatorHoPHPS"),
        )
process.selectedHltPatTausHPS = process.selectedHltPatTaus.clone(src='hltPatTausHPS')


process.hltTauSequence = cms.Sequence(
    process.hltKT6PFJetsForTaus + process.hltOnlinePrimaryVertices +

    process.hltPFTauSequnceNP +
    process.hltPatTausNP + process.selectedHltPatTausNP+
    process.hltPFTauSequnceOnlNP +
    process.hltPatTausOnlNP + process.selectedHltPatTausOnlNP +
    process.hltPFTauSequnceOnl2NP +
    process.hltPatTausOnl2NP + process.selectedHltPatTausOnl2NP +
    process.hltPFTauSequncePxlNP +
    process.hltPatTausPxlNP + process.selectedHltPatTausPxlNP +
    process.hltPFTauSequncePxl2NP +
    process.hltPatTausPxl2NP + process.selectedHltPatTausPxl2NP

    + process.hltPFTauSequnceHPS +
    process.hltPatTausHPS + process.selectedHltPatTausHPS
    )

