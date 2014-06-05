import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/onlinePt17_PVconstraint/patTuple_10_2_XaQ.root',
    'file:/afs/cern.ch/work/m/manzoni/TauHLT/700/CMSSW_7_0_0/src/TriggerStudies/Tau/test/patTuple.root',
  )
)

process.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  EdgeClusterErrorX = cms.double( 50.0 ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  UseErrorsFromTemplates = cms.bool( True ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  IrradiationBiasCorrection = cms.bool( False ),
  TanLorentzAnglePerTesla = cms.double( 0.106 ),
  inflate_errors = cms.bool( False ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  Alpha2Order = cms.bool( True )
)

process.fastPrimaryVertices = cms.EDProducer( "FastPrimaryVertexWithWeightsProducer",
    maxZ                      = cms.double( 19.0 ),
    clusters                  = cms.InputTag( "hltSiPixelClusters" ),
    pixelCPE                  = cms.string( "hltESPPixelCPEGeneric" ),
    beamSpot                  = cms.InputTag( "hltOnlineBeamSpot" ),
    jets                      = cms.InputTag( "hltCaloJetL1FastJetCorrected" ),
  
    njets                     = cms.int32( 999  ),
    maxJetEta                 = cms.double( 2.6 ), 
    minJetPt                  = cms.double( 0.  ),

    barrel                    = cms.bool(True),  
    maxSizeX                  = cms.double( 2.1 ),
    maxDeltaPhi               = cms.double( 0.21 ),
    PixelCellHeightOverWidth  = cms.double( 1.8 ),
    weight_charge_down        = cms.double(11*1000),
    weight_charge_up          = cms.double(190*1000),
    maxSizeY_q                = cms.double( 2 ),  
    minSizeY_q                = cms.double( -0.6 ), 
 
    weight_dPhi               = cms.double( 0.13888888 ), 
    weight_SizeX1             = cms.double(0.88),
    weight_rho_up             = cms.double( 22),
    weight_charge_peak        = cms.double(22*1000),
    peakSizeY_q               = cms.double( 1.0 ), 

    endCap                    = cms.bool(True),  
    minJetEta_EC              = cms.double( 1.3 ),  
    maxJetEta_EC              = cms.double( 2.6 ),  
    maxDeltaPhi_EC            = cms.double( 0.14 ),
    EC_weight                 = cms.double( 0.008 ),
    weight_dPhi_EC            = cms.double( 0.064516129 ), 
    
    zClusterWidth_step1       = cms.double( 2.0),

    zClusterWidth_step2       = cms.double( 0.65), 
    zClusterSearchArea_step   = cms.double( 3.0),
    weightCut_step2           = cms.double( 0.05),

    zClusterWidth_step3       = cms.double( 0.3), 
    zClusterSearchArea_step3  = cms.double( 0.55),
    weightCut_step3           = cms.double( 0.1),

)

process.p = cms.Path(
  process.fastPrimaryVertices 
  )

process.TFileService = cms.Service(
  "TFileService"                          ,
  fileName      = cms.string("test_FPV.root") ,
  closeFileFast = cms.untracked.bool(False)
)

