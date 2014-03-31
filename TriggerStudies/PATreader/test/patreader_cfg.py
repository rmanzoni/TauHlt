import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(



    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_10_3_t6Y.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_11_3_5fN.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_12_3_24S.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_13_3_9lG.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_14_3_4vO.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_15_3_2YP.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_16_3_hZv.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_17_3_cco.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_18_3_W6F.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_19_3_Jfa.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_1_3_gkX.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_20_3_6sH.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_21_3_Wos.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_22_3_jYa.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_23_3_8aY.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_24_3_Rqi.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_25_3_He8.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_26_3_AEt.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_27_3_rPW.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_28_3_F6K.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_29_3_9r5.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_2_3_XyZ.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_30_3_LxP.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_31_3_vyj.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_32_3_kiu.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_33_3_cdx.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_34_3_6nw.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_35_3_ZPv.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_36_3_wu7.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_37_3_Pix.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_38_3_AWQ.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_39_3_Fiz.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_3_3_gLm.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_40_3_aZi.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_41_3_q0C.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_42_3_E3F.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_43_3_VcM.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_44_3_pVJ.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_45_3_Hat.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_46_3_jKQ.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_47_3_daV.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_48_3_Mi0.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_49_3_LVL.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_4_3_JsS.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_50_3_0So.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_51_3_Ocx.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_52_3_h4G.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_53_3_zTb.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_54_3_D4e.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_55_3_TvT.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_56_3_rlp.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_57_3_DgC.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_58_3_iCG.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_59_3_p3i.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_5_3_Egv.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_60_3_GWr.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_61_3_Jx2.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_62_3_Ql5.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_63_3_11J.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_64_3_26X.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_65_3_scE.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_66_3_HRo.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_67_3_wkr.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_68_3_gGV.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_69_3_WQD.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_6_3_mBd.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_70_3_NaB.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_71_3_8Al.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_72_3_odm.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_7_3_vrk.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_8_3_gd0.root',
    'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/mt/13TeV/VBF_HToTauTau_M-125_13TeV-powheg-pythia6/patTuple_9_3_pA4.root',











#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_10_1_sFh.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_11_1_ebQ.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_12_1_uks.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_13_1_LEO.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_14_1_puW.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_15_1_c90.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_16_1_FZq.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_17_1_7Lr.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_18_1_uoA.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_19_1_4VM.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_1_1_we1.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_20_1_GF7.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_2_1_ym8.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_3_1_xWa.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_4_1_TKW.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_5_1_kpG.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_6_1_bFE.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_7_1_FgY.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_8_1_YG3.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_9_1_h3h.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_10_1_GSv.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_11_1_0iH.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_12_1_HCO.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_13_1_eJd.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_14_1_TQF.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_15_1_Ry8.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_16_1_8sv.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_17_1_TRc.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_18_1_yfO.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_1_1_jgu.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_2_1_mgR.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_3_1_jnu.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_4_1_ZU5.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_5_1_fWq.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_6_1_Djv.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_7_1_jSQ.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_8_1_ZOv.root',
#     'root://eoscms//eos/cms/store/cmst3/user/manzoni/TauPOG/11feb/ZPrimeTauTau_first4PixelVtx_sorted4power_threshold25gev/patTuple_9_1_5F8.root',
  )
)

process.sorter = cms.EDAnalyzer(
  'PATreader'                         ,
  lowerPtThreshold = cms.double(2.5  ) ,
  upperPtThreshold = cms.double(10.  ) ,
  maxZDistance     = cms.double(0.1  ) ,
  power            = cms.double(2.   ) ,
  enhanceWeight    = cms.int32 (-1   ) ,
  verbose          = cms.bool  (False) ,
)

process.p = cms.Path(
  process.sorter 
  )

process.TFileService = cms.Service(
  "TFileService"                          ,
  fileName      = cms.string("test.root") ,
  closeFileFast = cms.untracked.bool(False)
)

