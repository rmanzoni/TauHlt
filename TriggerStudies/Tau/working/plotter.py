import ROOT

from copy import deepcopy as dc

### style parameters
ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetLegendFillColor(0)
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetStatBorderSize(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPadTickX(1)
ROOT.gStyle.SetPadTickY(1)
ROOT.gStyle.SetTitleSize(0.040,'t')
# ROOT.gStyle.SetTitleOffset(1.200,"X")
ROOT.gStyle.SetTitleX(0.14) ## to be changed to 0.15
ROOT.gStyle.SetTitleY(0.96)
ROOT.gStyle.SetTitleW(0.8)
ROOT.gStyle.SetTextFont(42)
ROOT.gStyle.SetLegendFont(42)	
# ROOT.gStyle.SetLabelSize(0.040,'xy')
ROOT.gStyle.SetLabelFont(42, 'xy')
# ROOT.gStyle.SetTitleFont(42, 'xy')
# ROOT.gStyle.SetTitleSize(0.105,'xy')

def doRatio( num, den ) :
  num1 = dc(num)
  den1 = dc(den)
  ratio = dc(num1)
#   import pdb ; pdb.set_trace()
  ratio.Divide(num1,den1,1.,1.,'b')
  ratio.SetMinimum(0.7)
  ratio.SetMaximum(1.05)
  return ratio  

def plot( basehisto, basehistolegend, name, xaxis, yaxis, title='CMS Simulation, #sqrt{s} = 13 TeV, PU 40, bx 25 ns', morehistos = {}, color = ROOT.kRed, drawoptions = 'E', log = False , setRangeX = []) :
  '''
  Plots an histogram, eventually more histos to be drawn with Draw(SAME).
  morehistos should be a dict like {histo:[ROOT.kBlue,'legend entry']}
  '''
  c1 = ROOT.TCanvas('','',700,700)
  
  ROOT.gPad.SetLeftMargin(0.18)
  ROOT.gPad.SetBottomMargin(0.18)
  ROOT.gPad.SetFrameLineWidth(3)
  ROOT.gPad.SetGridx(1)
  ROOT.gPad.SetGridy(1)
  ROOT.gPad.SetLogy(log)

  l1 = ROOT.TLegend(0.5,0.3,0.8,0.5)
  l1.AddEntry(basehisto,basehistolegend)
  l1.SetFillColor(0)

  basehisto.SetLineWidth(2)  
  basehisto.SetLineColor(color)
  basehisto.SetMarkerStyle(9)
  basehisto.SetTitle('{TITLE};{XAXIS};{YAXIS}'.format(TITLE=title, XAXIS=xaxis, YAXIS=yaxis))
  basehisto.GetXaxis().SetTitle(xaxis)
  basehisto.GetYaxis().SetTitle(yaxis)
  basehisto.GetYaxis().SetTitleOffset(1.5)
  basehisto.GetXaxis().SetTitleOffset(1.5)
  if setRangeX != [] : basehisto.GetXaxis().SetRangeUser(setRangeX[0],setRangeX[1])  
  #basehisto.DrawNormalized(drawoptions)
  basehisto.Draw(drawoptions)
  
  for key in morehistos.keys() :
    l1.AddEntry(key,morehistos[key][1])
    key.SetLineWidth(2)  
    key.SetLineColor(morehistos[key][0])
    key.SetMarkerStyle(9)
    key.Draw('SAME'+drawoptions)

  if len(basehistolegend) > 0 : l1.Draw('sameAEPZ')
  
  c1.SaveAs(name+'.pdf')

# suffix = 'onlinePt0_PVconstraint'
# suffix = 'onlinePt0_noPVconstraint'
# suffix = 'onlinePt17_PVconstraint'
# suffix = 'onlinePt17_noPVconstraint'
# suffix = 'onlinePt17_noPVconstraint_online_matches_offline'
# suffix = 'onlinePt17_PVconstraint_online_matches_offline'
# suffix = 'onlinePt17_noPVconstraint_threshold0p7'
suffix = 'onlinePt17_noPVconstraint_threshold0p3_notrackProb1permille'

file = ROOT.TFile.Open('mt_13TeV_VBF_HToTauTau_M-125_13TeV-powheg-pythia6_{SUF}.root'.format(SUF=suffix),'read')

file.cd()

# variable = '_gen_pt'
variable = '_pt'


offTaus              = ROOT.gDirectory.FindObjectAny('offTaus'                + variable)
onlTauPix            = ROOT.gDirectory.FindObjectAny('onlTausPixVtx_recoHLT'  + variable)
onlTauPixPassingDM   = ROOT.gDirectory.FindObjectAny('onlTausPixVtx_passDM'   + variable)
onlTauPixPassingIso  = ROOT.gDirectory.FindObjectAny('onlTausPixVtx_passIso'  + variable)
# onlTauPix2           = ROOT.gDirectory.FindObjectAny('onlTausPixVtx2S12NN_recoHLT' + variable)
# onlTauPixPassingDM2  = ROOT.gDirectory.FindObjectAny('onlTausPixVtx2S12NN_passDM'  + variable)
# onlTauPixPassingIso2 = ROOT.gDirectory.FindObjectAny('onlTausPixVtx2S12NN_passIso' + variable)
onlTauPix2           = ROOT.gDirectory.FindObjectAny('onlTausPixVtx2_recoHLT' + variable)
onlTauPixPassingDM2  = ROOT.gDirectory.FindObjectAny('onlTausPixVtx2_passDM'  + variable)
onlTauPixPassingIso2 = ROOT.gDirectory.FindObjectAny('onlTausPixVtx2_passIso' + variable)
onlTauMu             = ROOT.gDirectory.FindObjectAny('onlTausMuVtx_recoHLT'   + variable)
onlTauMuPassingDM    = ROOT.gDirectory.FindObjectAny('onlTausMuVtx_passDM'    + variable)
onlTauMuPassingIso   = ROOT.gDirectory.FindObjectAny('onlTausMuVtx_passIso'   + variable)
position             = ROOT.gDirectory.FindObjectAny('position')


vert = ROOT.gDirectory.FindObjectAny('pixVtx_failDMonl_noOnlTrk_dz(offlineVtx)')

# import pdb ; pdb.set_trace()

pix2Ratio1 = doRatio( onlTauPix2          , offTaus )
pix2Ratio2 = doRatio( onlTauPixPassingDM2 , offTaus )
pix2Ratio3 = doRatio( onlTauPixPassingIso2, offTaus )

# muRatio1 = doRatio( onlTauMu          , offTaus )
# muRatio2 = doRatio( onlTauMuPassingDM , offTaus )
# muRatio3 = doRatio( onlTauMuPassingIso, offTaus )

plot( pix2Ratio1, 'Tau Jet', 'pix2efficiency' + suffix, '#tau p_{T} [GeV]', 'efficiency', morehistos = {pix2Ratio2:[ROOT.kGreen+3,'leading track'],pix2Ratio3:[ROOT.kBlue,'isolation']}, setRangeX = [0.,110.] )
# plot( muRatio1  , 'Tau Jet', 'muefficiency'   + suffix, '#tau p_{T} [GeV]', 'efficiency', morehistos = {muRatio2  :[ROOT.kGreen+3,'leading track']}, setRangeX = [0.,110.] )
# plot( position   , ''            , 'position'       + suffix, 'position of offline PV in online PixVtx collection', 'fraction', drawoptions = '', log = True, setRangeX = [0.,20.] )

# plot( vert , '', 'dzPix_Off' , 'dz [cm]', 'events' )
