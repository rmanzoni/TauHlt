import ROOT
import PATreader
from array import array
from files import *

bins = array('d',[0.,17.5,20.,22.5,25.,30.,40.,50.,60.,80.,120.,250.,500,])
# bins = array('d',[0.,17.5,20.,22.5,25.,30.,40.,50.,60.,80.,120.])


tauCollections = [
                 #'onlTausHPS'         ,
                 #'onlTausMuVtx'       ,
                 #'onlTausDAVtx'       ,
                 #'onlTausDAVtx2'      ,
                 #'onlTausPixVtx'      ,
                 'onlTausPixVtx2'     ,
                 #'onlTausPixVtx2S12N3',
                 #'onlTausPixVtx2S12N5',
                 #'onlTausPixVtx2S12NN',
                 #'onlTausPixVtx2S15N3',
                 #'onlTausPixVtx2S15N5',
                 #'onlTausPixVtx2S15NN',
                 #'onlTausPixVtx2S18N3',
                 #'onlTausPixVtx2S18N5',
                 #'onlTausPixVtx2S18NN',
                 ]

basic_histos = {}
names = ['offTaus']
for tauCollection in tauCollections :
  names.extend([tauCollection+'_recoHLT',
                tauCollection+'_passDM' , 
                tauCollection+'_failDM' , 
                tauCollection+'_failDM' ,
                tauCollection+'_failRecoHLT_noOnlTrack' , 
                tauCollection+'_failRecoHLT_hasOnlTrack' , 
                tauCollection+'_passIso'])
for name in names :
  basic_histos.update({name:{}})
  basic_histos[name].update({'pt'            : ROOT.TH1F( name+'_pt'            , '' , len(bins)-1, bins )} )
  basic_histos[name].update({'gen_pt'        : ROOT.TH1F( name+'_gen_pt'        , '' , len(bins)-1, bins )} )
  basic_histos[name].update({'eta'           : ROOT.TH1F( name+'_eta'           , '' , 25   , -2.5,  2.5 )} )
  basic_histos[name].update({'phi'           : ROOT.TH1F( name+'_phi'           , '' , 25   , -2.5,  2.5 )} )
  basic_histos[name].update({'charge'        : ROOT.TH1F( name+'_charge'        , '' , 25   , -2.5,  2.5 )} )
  basic_histos[name].update({'recoDM'        : ROOT.TH1F( name+'_recoDM'        , '' , 15   ,    0,   15 )} )
  basic_histos[name].update({'genDM'         : ROOT.TH1F( name+'_genDM'         , '' , 10   ,    0,    0 )} )
  basic_histos[name].update({'pixVtxSumPt2'  : ROOT.TH1F( name+'_pixVtxSumPt2'  , '' , 200  ,    0,10000 )} )
  basic_histos[name].update({'offVtxSumPt2'  : ROOT.TH1F( name+'_offVtxSumPt2'  , '' , 200  ,    0,10000 )} )
  basic_histos[name].update({'pixVtxTrkMult' : ROOT.TH1F( name+'_pixVtxTrkMult' , '' , 200  ,    0,  200 )} )
  basic_histos[name].update({'offVtxTrkMult' : ROOT.TH1F( name+'_offVtxTrkMult' , '' , 200  ,    0,  200 )} )
  basic_histos[name].update({'HLTPtRes'      : ROOT.TH1F( name+'_HLTPtRes'      , '' , 400  ,   -2,    2 )} )
  basic_histos[name].update({'HLTPtPull'     : ROOT.TH1F( name+'_HLTPtPull'     , '' , 500  ,  -50,   50 )} )

track_histos = {}
names = []
for tauCollection in tauCollections :
  names.extend([tauCollection+'_offTrk_failDM_hasOnlTrk' ,
                tauCollection+'_onlTrk_failDM_hasOnlTrk' , 
                tauCollection+'_onlTrk_failDM_hasOnlTrk' , 
                tauCollection+'_onlTrk_failDM_hasOnlTrk' , 
                tauCollection+'_failRecoHLT_noOnlTrack_offTrk' , 
                tauCollection+'_failRecoHLT_hasOnlTrack_offTrk' , 
                tauCollection+'_offTrk_failDM_noOnlTrk'  ])
for name in names :
  track_histos.update({name:{}})
  track_histos[name].update({'pt'                         : ROOT.TH1F( name+'_pt'                        , '' , 24, 0   , 120 )} )
  track_histos[name].update({'errPtOverPt'                : ROOT.TH1F( name+'_errPtOverPt'               , '' , 20, 0   , 100 )} )
  track_histos[name].update({'eta'                        : ROOT.TH1F( name+'_eta'                       , '' , 25, -2.5, 2.5 )} )
  track_histos[name].update({'phi'                        : ROOT.TH1F( name+'_phi'                       , '' , 25, -2.5, 2.5 )} )
  track_histos[name].update({'charge'                     : ROOT.TH1F( name+'_charge'                    , '' , 5 , -2  , 2   )} )
  track_histos[name].update({'chi2'                       : ROOT.TH1F( name+'_chi2'                      , '' , 40, 0   , 20  )} )
  track_histos[name].update({'ndof'                       : ROOT.TH1F( name+'_ndof'                      , '' , 40, 0   , 40  )} )
  track_histos[name].update({'normalizedChi2'             : ROOT.TH1F( name+'_normalizedChi2'            , '' , 20, 0   , 20  )} )
  track_histos[name].update({'numberOfLostHits'           : ROOT.TH1F( name+'_numberOfLostHits'          , '' , 20, 0   , 20  )} )
  track_histos[name].update({'numberOfValidHits'          : ROOT.TH1F( name+'_numberOfValidHits'         , '' , 20, 0   , 20  )} )
  track_histos[name].update({'highPurity'                 : ROOT.TH1F( name+'_highPurity'                , '' , 5 , 0   , 5   )} )
  track_histos[name].update({'numberOfValidPixelHits'     : ROOT.TH1F( name+'_numberOfValidPixelHits'    , '' , 20, 0   , 20  )} )
  track_histos[name].update({'pixelLayersWithMeasurement' : ROOT.TH1F( name+'_pixelLayersWithMeasurement', '' , 20, 0   , 20  )} )
  track_histos[name].update({'numberOfValidTrackerHits'   : ROOT.TH1F( name+'_numberOfValidTrackerHits'  , '' , 20, 0   , 20  )} )
  track_histos[name].update({'dxy(offlineVtx)'            : ROOT.TH1F( name+'_dxy(offlineVtx)'           , '' , 40, 0   , 2   )} )
  track_histos[name].update({'dz(offlineVtx)'             : ROOT.TH1F( name+'_dz(offlineVtx)'            , '' , 40, 0   , 20  )} )
  track_histos[name].update({'dxy(hltPixVtx)'             : ROOT.TH1F( name+'_dxy(hltPixVtx)'            , '' , 40, 0   , 2   )} )
  track_histos[name].update({'dz(hltPixVtx)'              : ROOT.TH1F( name+'_dz(hltPixVtx)'             , '' , 40, 0   , 20  )} )
  track_histos[name].update({'dxy(hltMuVtx)'              : ROOT.TH1F( name+'_dxy(hltMuVtx)'             , '' , 40, 0   , 2   )} )
  track_histos[name].update({'dz(hltMuVtx)'               : ROOT.TH1F( name+'_dz(hltMuVtx)'              , '' , 40, 0   , 20  )} )
  track_histos[name].update({'algo'                       : ROOT.TH1F( name+'_algo'                      , '' , 8 , 0   , 8   )} )
  track_histos[name].update({'dRoffline'                  : ROOT.TH1F( name+'_dRoffline'                 , '' , 40, 0   , 4   )} )
  track_histos[name].update({'dRonline'                   : ROOT.TH1F( name+'_dRonline'                  , '' , 40, 0   , 4   )} )

vertex_histos = {}
names = []
for tauCollection in tauCollections :
  names.extend([tauCollection+'_MuVtx_failDM_noOnlTrk'   ,
                tauCollection+'_MuVtx_failDM_hasOnlTrk'  , 
                tauCollection+'_MuVtx_passDM_hasOnlTrk'  ,
                tauCollection+'_PixVtx_failDM_noOnlTrk'  ,
                tauCollection+'_PixVtx_failDM_hasOnlTrk' , 
                tauCollection+'_failRecoHLT_noOnlTrack_onlVtx0' , 
                tauCollection+'_failRecoHLT_noOnlTrack_onlVtx1' , 
                tauCollection+'_failRecoHLT_noOnlTrack_onlVtx2' , 
                tauCollection+'_failRecoHLT_noOnlTrack_onlVtx3' , 
                tauCollection+'_failRecoHLT_hasOnlTrack_onlVtx0' , 
                tauCollection+'_failRecoHLT_hasOnlTrack_onlVtx1' , 
                tauCollection+'_failRecoHLT_hasOnlTrack_onlVtx2' , 
                tauCollection+'_failRecoHLT_hasOnlTrack_onlVtx3' , 
                tauCollection+'_PixVtx_passDM_hasOnlTrk' ,])
                #tauCollection+'_PixVtx2_failDM_noOnlTrk' ,
                #tauCollection+'_PixVtx2_failDM_hasOnlTrk', 
                #tauCollection+'_PixVtx2_passDM_hasOnlTrk',
                #tauCollection+'_DAVtx_failDM_noOnlTrk'   ,
                #tauCollection+'_DAVtx_failDM_hasOnlTrk'  , 
                #tauCollection+'_DAVtx_passDM_hasOnlTrk'  ,
                #tauCollection+'_DAVtx2_failDM_noOnlTrk'  ,
                #tauCollection+'_DAVtx2_failDM_hasOnlTrk' , 
                #tauCollection+'_DAVtx2_passDM_hasOnlTrk' ])
for name in names :
  vertex_histos.update({name:{}})
  vertex_histos[name].update({'dxy(offlineVtx)': ROOT.TH1F( name+'_dxy(offlineVtx)' , '' , 50 , -2 , 2 )} )
  vertex_histos[name].update({'dz(offlineVtx)' : ROOT.TH1F( name+'_dz(offlineVtx)'  , '' , 100, -20, 20)} )


sorting_histos = {}
names  = []
for tauCollection in tauCollections :
  names.extend([tauCollection+'_2passDM'])
for name in names :
  sorting_histos.update({name:{}})
  sorting_histos[name].update({'differenceInverse': ROOT.TH1F( name+'_differenceInverse', '' , 200, -0.5, 0.5 )} )
  sorting_histos[name].update({'pull'             : ROOT.TH1F( name+'_pull'             , '' , 100, -20 , 20  )} )



index = {}
index.update({'position'  :ROOT.TH1F( 'position'      , '' , 50, 0,50)} )
index.update({'position0' :ROOT.TH1F( 'position0'     , '' , 50, 0,50)} )
index.update({'position1' :ROOT.TH1F( 'position1'     , '' , 50, 0,50)} )
index.update({'position2' :ROOT.TH1F( 'position2'     , '' , 50, 0,50)} )
index.update({'position3' :ROOT.TH1F( 'position3'     , '' , 50, 0,50)} )
index.update({'position4' :ROOT.TH1F( 'position4'     , '' , 50, 0,50)} )
index.update({'position5' :ROOT.TH1F( 'position5'     , '' , 50, 0,50)} )
index.update({'position6' :ROOT.TH1F( 'position6'     , '' , 50, 0,50)} )
index.update({'position7' :ROOT.TH1F( 'position7'     , '' , 50, 0,50)} )


# myFiles = ['/afs/cern.ch/work/m/manzoni/TauHLT/michal4feb/CMSSW_5_3_14_patch2/src/TriggerStudies/Tau/test/patTuple.root',] 
# myFiles = ['/afs/cern.ch/work/m/manzoni/TauHLT/CMSSW_5_3_14_patch2_trg/src/TriggerStudies/Tau/test/patTuple_loosenIter0Jet_v2.root',]  
# myFiles = ['/afs/cern.ch/work/m/manzoni/TauHLT/CMSSW_5_3_14_patch2_trg/src/TriggerStudies/Tau/test/patTuple_originalIter0Jet_v2.root',] 
# failingEvents = [28150788,38979698,9377365,34287744,2073115,62411153,61730373,45685986,47009379,4002807,22405779,56029277,18718809,52991929,13991388,1953725,16196942,67886619,16228470,16138268,16277738,27435007,9365765,22024092,28389058,27226213,27228342,30051102,19575720,62078292,3835767,21848492,2682170,11037065,16270377,26689779,24705865,38498563,40177109,6063353,3924919,61479375,24710730,38972916,38951854,56561840,61830800,19760180,16253201,36230639,33444947,12782522,45053556,4441121,66238069,65020368,24505983,11490191,12838373,14199880,53197377,1382277,12812297,1249504,21513095,25618944,16215296,37977062,68700985,40605935,61890250,13727268,65101560,38184411,9353868,38410378,16160789,16273551,63543902,26934110,9368795,37232492,11498432,52813775,52536300,70645969,6524418,9355742,16189544,16190949]  

## for Ztt only!!
# failingEvents_1PixVtx = [9355742, 12836548, 16273551, 12788490, 37844429, 37977062, 24505983, 2728836, 16160789, 61891001, 28389058, 12855253, 16179527, 37114441, 22024092, 68866402, 18718809, 49051581, 23178399, 1934739, 12838373, 16270905, 61953253, 37315787, 5445840, 45402126, 38184411, 13814635, 40113637, 12782522, 3924919, 6836511, 56029277, 52813775, 61890250, 26934110, 11040918, 11830230, 33444947, 4862655, 27228342, 1537386, 19575720, 53197377, 38292325, 51945386, 61632501, 38185091, 34287744, 14199880, 45685986, 49150061, 13450075, 6524418, 63980635, 16174728, 1382277, 9365765, 38979698, 9373492, 40063225, 16277738, 66229955, 63642402, 51735684, 16196942, 16253201, 26794570, 68867776, 2073115, 2682170, 38972916, 14001295, 13991388, 16190949, 40605935, 5579574, 4600136, 24710730, 5446802, 1953725, 28150788, 21513095, 6063398, 67886619, 49155873, 16155809, 36981079, 11735920, 67888923, 54102415, 29421565, 45053556, 33003781, 26689779, 66238069, 62411153, 66225640, 29888452, 65101560, 32378912, 64757643, 65020368, 11490191, 27435007, 2388191, 61480025, 26689862, 70645969, 4002807, 68862357, 61830800, 47009379, 11498432, 61479375, 47258711, 16228470, 16215296, 11037065, 40177109, 13727268, 9377365, 16138268, 57109773, 3835767, 56561840, 52536300, 52991929, 38299583, 19760180, 13325636, 12814106, 50606870, 9353868, 25618944, 38410378, 67794329, 44035084, 9368795, 61375679, 16189544, 27226213, 6499602, 16270377, 36230639, 37232492, 64758888, 18509391, 30051102, 47341800, 68695948, 51734730, 62078292, 22405779, 57067295, 2651715, 63543902, 50899976, 24705865, 20206887, 12860291, 6063353, 49504218, 12796007, 68700985, 12812297, 33373632, 10941554, 61730373, 1249504, 38951854, 21848492, 19931030, 44313110, 38498563, 47932862, 2278242, 45160602, 28394489, 4441121, 12818292]
# failingEvents_4PixVtx = [67888923, 16273551, 47341800, 37977062, 2728836, 40063225, 61891001, 28389058, 68867776, 11737338, 12782522, 18718809, 49051581, 37699381, 23178399, 61953253, 37315787, 57109773, 45402126, 9377365, 38184411, 23470147, 27678516, 66587558, 3924919, 6836511, 52813775, 61890250, 26934110, 11040918, 4862655, 1537386, 11727857, 51945386, 61632501, 38185091, 14199880, 45685986, 68866402, 13450075, 6524418, 16277738, 66229955, 51735684, 16196942, 33444947, 2282835, 26794570, 12855253, 2073115, 2682170, 38972916, 14001295, 1953725, 12814106, 21513095, 24603796, 22024092, 68861614, 29720603, 54102415, 29421565, 33003781, 31769099, 66238069, 66225640, 65101560, 32378912, 64757643, 46987534, 65020368, 62411153, 2388191, 70645969, 4002807, 68862357, 47009379, 11498432, 30053127, 37314302, 33373632, 47258711, 16228470, 16215296, 40177109, 16270377, 61830800, 16138268, 49150061, 56561840, 52536300, 52991929, 38299583, 19760180, 13325636, 12788490, 50606870, 9353868, 38410378, 67794329, 44035084, 9368795, 61375679, 16189544, 27226213, 5445840, 37114441, 37844429, 51734730, 62078292, 24705865, 12860291, 6063353, 40176732, 12796007, 12812297, 61730373, 38951854, 21848492, 19931030, 44313110, 38498563, 47932862, 2278242, 28394489, 4441121, 12818292]
# failingEvents_4PixVtx_and_1pixVtx = [16273551, 6836511, 37977062, 2728836, 40063225, 61891001, 28389058, 68867776, 22024092, 51734730, 49051581, 29421565, 61953253, 37315787, 57109773, 45402126, 9377365, 38184411, 3924919, 52813775, 61890250, 26934110, 11040918, 4862655, 1537386, 16189544, 51945386, 61632501, 38185091, 14199880, 45685986, 68866402, 13450075, 38299583, 16277738, 66229955, 51735684, 16196942, 33444947, 26794570, 12855253, 2073115, 2682170, 38972916, 14001295, 1953725, 12814106, 21513095, 12782522, 37844429, 67888923, 23178399, 33003781, 66238069, 66225640, 65101560, 32378912, 64757643, 65020368, 62411153, 2388191, 70645969, 4002807, 68862357, 47009379, 11498432, 33373632, 47258711, 16228470, 16215296, 40177109, 5445840, 61830800, 16138268, 49150061, 56561840, 52536300, 52991929, 6524418, 19760180, 13325636, 12788490, 50606870, 9353868, 38410378, 67794329, 44035084, 9368795, 61375679, 54102415, 27226213, 16270377, 37114441, 47341800, 18718809, 62078292, 24705865, 12860291, 6063353, 12796007, 12812297, 61730373, 38951854, 21848492, 19931030, 44313110, 38498563, 47932862, 2278242, 28394489, 4441121, 12818292]
# failingEvents_4PixVtx_not_1pixVtx = [29720603, 11737338, 24603796, 46987534, 23470147, 30053127, 37314302, 37699381, 31769099, 27678516, 40176732, 66587558, 11727857, 68861614, 2282835]
# failingEvents_1PixVtx_not_4pixVtx = [9355742, 12836548, 67886619, 25618944, 34287744, 1249504, 22405779, 24505983, 26689779, 63980635, 16174728, 1382277, 16160789, 38979698, 9373492, 9365765, 29888452, 57067295, 36230639, 16179527, 11037065, 18509391, 24710730, 11490191, 49504218, 63642402, 27435007, 1934739, 45053556, 61480025, 26689862, 68700985, 16270905, 2651715, 63543902, 50899976, 13727268, 64758888, 13991388, 20206887, 61479375, 11735920, 40113637, 45160602, 16190949, 40605935, 5579574, 4600136, 56029277, 5446802, 12838373, 28150788, 6499602, 10941554, 11830230, 16253201, 6063398, 13814635, 27228342, 49155873, 37232492, 16155809, 19575720, 68695948, 53197377, 36981079, 38292325, 30051102, 3835767]
# failingEvents_failReco_offVtx     = [68867776 ,2388191 ,38410378 ,52813775 ,12796007 ,38292325 ,33003781 ,46987534 ,64757643 ,6524418 ,16189544 ,12788490 ,1953725 ,16196942 ,13450075 ,16228470 ,16138268 ,12860291 ,27226213 ,45402126 ,11727857 ,20206887 ,6868312 ,37315787 ,16270377 ,24705865 ,38498563 ,38951854 ,33373632 ,33444947 ,37844429 ,68862357 ,65020368 ,16498823 ,14199880 ,5445840 ,23468201 ,19931030 ,13325636 ,2278242 ,11040918 ,1934739 ,21768480 ,61730373 ,40063225 ,61891001 ,37977062 ,38184411 ,6836511 ,1537386 ,18718809 ,37114441 ,52991929 ,23178399 ,]
# failingEvents_failReco_hasRealOnlineTrk_offVtx = [2388191 ,52813775,38292325,12788490,16196942,45402126,6868312 ,16270377,24705865,38498563,38951854,33373632,68862357,16498823,5445840 ,23468201,2278242 ,11040918,21768480,40063225,37977062,1537386 ,37114441,]
# these are for events that pass reco at least, but not DM
# failingEvents_1PixVtx_has_some_sort_of_track_online = [51734730,29421565,11037065,26794570,67888923,3924919,61890250,6063398,63642402,52991929,26689862,61830800,12855253,62411153,5579574,47009379,28394489,57109773,9368795,]
# failingEvents_1PixVtx_has_some_sort_of_track_online = [38292325 ,64757643 ,70645969 ,12814106 ,5446802 ,6524418 ,16277738 ,51734730 ,50899976 ,27226213 ,11735920 ,45402126 ,29421565 ,14001295 ,37315787 ,11037065 ,14199880 ,5445840 ,26794570 ,2388191 ,16160789 ,68695948 ,67888923 ,3924919 ,24710730 ,6499602 ,37977062 ,61890250 ,1382277 ,18509391 ,1249504 ,2278242 ,44313110 ,11040918 ,12836548 ,49150061 ,38498563 ,6063398 ,63642402 ,38951854 ,49051581 ,38299583 ,37114441 ,52991929 ,16155809 ,4862655 ,66225640 ,16270377 ,26689862 ,2651715 ,2728836 ,24705865 ,61830800 ,16253201 ,32378912 ,33373632 ,68862357 ,12855253 ,61375679 ,4441121 ,66238069 ,65020368 ,24505983 ,47932862 ,9373492 ,62411153 ,61730373 ,40063225 ,40113637 ,45685986 ,61891001 ,5579574 ,45160602 ,54102415 ,9353868 ,47009379 ,1537386 ,22405779 ,66229955 ,28394489 ,18718809 ,57109773 ,67794329 ,68866402 ,68867776 ,38185091 ,9368795 ,16179527 ,12788490 ,16174728 ,52813775 ,61632501 ,12796007 ,13814635 ,]
# failingEvents_4PixVtx_has_some_sort_of_track_online = [57109773 ,67794329 ,68866402 ,68867776 ,38185091 ,23470147 ,26934110 ,9368795 ,37314302 ,12788490 ,52813775 ,61632501 ,12796007 ,64757643 ,70645969 ,12814106 ,6524418 ,16228470 ,16277738 ,51734730 ,27226213 ,45402126 ,2282835 ,29421565 ,14001295 ,21848492 ,37315787 ,66225640 ,16270377 ,2728836 ,24705865 ,68861614 ,49150061 ,38498563 ,38951854 ,49051581 ,61830800 ,19760180 ,32378912 ,33373632 ,68862357 ,12855253 ,29720603 ,61375679 ,4441121 ,66238069 ,65020368 ,47932862 ,67888923 ,30053127 ,37699381 ,3924919 ,11737338 ,14199880 ,5445840 ,26794570 ,2278242 ,40176732 ,44313110 ,11040918 ,38299583 ,62411153 ,61730373 ,40063225 ,45685986 ,61891001 ,37977062 ,61890250 ,54102415 ,9353868 ,47009379 ,1537386 ,66229955 ,28394489 ,18718809 ,27678516 ,37114441 ,52991929 ,4862655 ,2388191 ,]
# 
# riccardo_not_michal = [16270721, 26934110, 36981079, 52813775, 2729782, 12794115, 52536300, 38292325, 64757643, 70645969, 6524418, 16179527, 28150788, 50610855, 1953725, 13450075, 16138268, 51945386, 27226213, 27228342, 37315787, 12818292, 14001295, 38295304, 2651715, 24705865, 6063353, 49051581, 56561840, 61480241, 16253201, 33373632, 33444947, 37844429, 66238069, 65020307, 65020368, 24505983, 12838373, 9373492, 11737541, 14199880, 34396543, 24710730, 61375679, 4441121, 30282289, 53197377, 18509391, 21513095, 44313110, 47341800, 1934739, 40113637, 1314411, 37977062, 32288028, 12810056, 13727268, 9353868, 22405779, 66229955, 18718809, 47258711, 64758888, 23178399, 11739734]

## for DY and ZPrime /store/cmst3/user/manzoni/TauPOG/11feb/Z{,Prime}TauTau_first4PixelVtx_sorted4power_threshold25gev/

# failing_HLT_4vtx_11feb = [68866402,68867776,23470147,37314302,11498432,12788490,52813775,66587558,12796007,52536300,33003781,46987534,64757643,70645969,4001987,12814106,6524418,1953725,13450075,16228470,16138268,12860291,16277738,51945386,28389058,27226213,45244421,45402126,14001295,21848492,37315787,66225640,12818292,16270377,24705865,4381202,68861614,38498563,6063353,38951854,49051581,56561840,32378912,33373632,61953253,33444947,37844429,68862357,29720603,54945074,61375679,4441121,66238069,50606870,65020368,30053127,37699381,3924919,11737338,14199880,5445840,19931030,13325636,2278242,40176732,44313110,11040918,38299583,1934739,61730373,40063225,45685986,61891001,16215296,37977062,31769099,54102415,46758795,38184411,6836511,9353868,1537386,4002807,66229955,18718809,47258711,27678516,45540930,51735684,4862655,23178399,2388191,38410378,46348,47571,47661,49263,571,704,3591,27648,6741,16922,31456,45739,2070,2223,2921,4627,11967,17971,5861,5870,32855,181,23415,22249,29027,6511,2822,7737,8005,12533,18570,13276,20259,21034,11315,21932,37611,39994,40013,4805,14895,34090,34235,34514,43371,43429,15622,44111,44131,43006,43071,29901,39267,40610,40761]
failing_HLT_1vtx_11feb = [38292325,33003781,49504218,64757643,70645969,12814106,5446802,6524418,16189544,16190949,28150788,1953725,13450075,16228470,16138268,12860291,16277738,50899976,51945386,27435007,27226213,27228342,11735920,19575720,45402126,62078292,14001295,20206887,21848492,37315787,10941554,14199880,5445840,2388191,38410378,16160789,68695948,24710730,6499602,16215296,37977062,68700985,40605935,53197377,1382277,19931030,13325636,18509391,1249504,2278242,21513095,44313110,38979698,11040918,12836548,49150061,38498563,6063353,11830230,38951854,49051581,56561840,61480025,38299583,1934739,29888452,34287744,47258711,64758888,37114441,16155809,13991388,51735684,57067295,4862655,23178399,66225640,12818292,16270377,16270905,2651715,2728836,24705865,16253201,32378912,33373632,36230639,61953253,33444947,37844429,68862357,61375679,4441121,66238069,50606870,65020368,24505983,47932862,12838373,9373492,61730373,40063225,40113637,45685986,61891001,45160602,13727268,54102415,38184411,6836511,9353868,1537386,4002807,22405779,66229955,4600136,56029277,18718809,67794329,63543902,68866402,68867776,38185091,26934110,36981079,16179527,37232492,12788490,16174728,52813775,61632501,12796007,52536300,13814635,9617,9668,13276,10118,10431,10508,20259,20476,20539,20850,20887,3936,11290,11315,11504,22048,37611,39994,40013,4805,4817,7325,14895,15033,14207,34090,34235,34514,43334,43371,43429,43932,44111,44131,31696,38415,43006,43071,44475,44628,29770,29901,29913,33699,45177,45582,29306,29458,31456,29306,29458,31456,38964,39116,39267,40414,40610,40761,41137,41175,46082,46348,47661,49263,571,607,704,3591,3709,27648,6741,6777,16922,17631,17971,5861,5870,6102,24304,24417,32855,39678,146,50318,19517,36624,36735,36777,45085,45089,45108,45739,45980,2070,2223,2349,2921,4627,11967,12211,22249,22862,22932,16006,28359,29027,29205,1141,6511,1857,2777,7737,8005,9086,18316,18570]

myAnalyzer = PATreader.PATreader(myFiles                               , 
                                 basic_histos         = basic_histos   , 
                                 track_histos         = track_histos   , 
                                 vertex_histos        = vertex_histos  , 
                                 sorting_histos       = sorting_histos , 
                                 index                = index          ,
                                 onlineTauCollections = tauCollections ,
                                 keepAllTaus          = False          ) 
 
 
# failingEvents_1PixVtx_no_track_at_all = set( failingEvents_1PixVtx) - set( failingEvents_1PixVtx_has_some_sort_of_track_online )
# failingEvents_4PixVtx_no_track_at_all = set( failingEvents_4PixVtx) - set( failingEvents_4PixVtx_has_some_sort_of_track_online )
                                 
# myAnalyzer.bookTree('vertexTree')                       
myAnalyzer.looper(maxEvents=-1, pickEvents=failing_HLT_1vtx_11feb, verbose=False)
# myAnalyzer.writeTree( myAnalyzer.tree, myAnalyzer.treeFile)
myAnalyzer.printSummary()

# outFile = ROOT.TFile.Open('out_firstPixVtx_standard.root' ,'recreate')
# outFile = ROOT.TFile.Open('out_first4PixVtx_sorted4power_threshold25gev.root' ,'recreate')
# outFile = ROOT.TFile.Open('out_offlineVtx.root'    ,'recreate')
# outFile = ROOT.TFile.Open('out_firstPixelVtx.root' ,'recreate')
# outFile = ROOT.TFile.Open('out_first2PixelVtx.root','recreate')
# outFile = ROOT.TFile.Open('out_first4PixelVtx.root','recreate')


# outFile = ROOT.TFile.Open('out_4pixVtx_sandbox.root' ,'recreate')
# outFile = ROOT.TFile.Open('out_OffVtx_sandbox.root' ,'recreate')
outFile = ROOT.TFile.Open('out_1vtx_cut_test.root' ,'recreate')


outFile.cd()

for key in basic_histos.keys() :
  outFile.mkdir(key)
  outFile.cd(key)
  for histo in basic_histos[key].values() :
    histo.Write()

outFile.cd()

for key in track_histos.keys() :
  outFile.mkdir(key)
  outFile.cd(key)
  for histo in track_histos[key].values() :
    histo.Write()

outFile.cd()

for key in vertex_histos.keys() :
  outFile.mkdir(key)
  outFile.cd(key)
  for histo in vertex_histos[key].values() :
    histo.Write()

outFile.cd()

for key in sorting_histos.keys() :
  outFile.mkdir(key)
  outFile.cd(key)
  for histo in sorting_histos[key].values() :
    histo.Write()

outFile.cd()

for key in index.keys() :
  outFile.mkdir(key)
  outFile.cd(key)
  index[key].Write()

outFile.Close()


