import ROOT

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
# ROOT.gStyle.SetTitleX(-0.038) ## to be changed to 0.15
ROOT.gStyle.SetTitleY(0.96)
ROOT.gStyle.SetTitleW(0.8)
ROOT.gStyle.SetTextFont(42)
ROOT.gStyle.SetLegendFont(42)	
ROOT.gStyle.SetLabelSize(0.030,'x')
# ROOT.gStyle.SetLabelSize(0.0140,'y')
ROOT.gStyle.SetLabelFont(42, 'xy')
ROOT.gStyle.SetTitleFont(42, 'xy')
# ROOT.gStyle.SetTitleSize(0.505,'xy')
# ROOT.gStyle.SetErrorX(0)
# ROOT.gStyle.SetErrorY(0)

# ROOT.TH1.SetDefaultSumw2()

file = ROOT.TFile.Open('test.root','r')
file.cd()

directories = ROOT.gDirectory.GetListOfKeys()

mean   = ROOT.TH1F('mean'  ,'CMS Simulation, #sqrt{s} = 8 TeV',len(directories)-4,0. ,0.5)
first  = ROOT.TH1F('first' ,'CMS Simulation, #sqrt{s} = 8 TeV',len(directories)-4,0.8,1. )
second = ROOT.TH1F('second','CMS Simulation, #sqrt{s} = 8 TeV',len(directories)-4,0.8,1. )
fourth = ROOT.TH1F('fourth','CMS Simulation, #sqrt{s} = 8 TeV',len(directories)-4,0.8,1. )

for dd in directories[4:] : 
  print ''
  print dd.GetName()
  positionHisto = ROOT.gDirectory.Get(dd.GetName()+'/position')

  print 'mean\t', positionHisto.GetMean()  
  mean.Fill(dd.GetName(),positionHisto.GetMean())
  #mean.SetBinError(dd.GetName(),positionHisto.GetMean())

  firstBin  = positionHisto.GetBinContent(1)
  print 'offVtx == offline [0]\t', firstBin/positionHisto.Integral()
  first.Fill(dd.GetName(),firstBin/positionHisto.Integral())

  firstBin += positionHisto.GetBinContent(2)
  print 'offVtx <= offline [1]\t', firstBin/positionHisto.Integral()
  second.Fill(dd.GetName(),firstBin/positionHisto.Integral())

  firstBin += positionHisto.GetBinContent(3)
  firstBin += positionHisto.GetBinContent(4)
  print 'offVtx <= offline [3]\t', firstBin/positionHisto.Integral()
  fourth.Fill(dd.GetName(),firstBin/positionHisto.Integral())

for hist in [mean,first,second,fourth] :
  hist.SetLineWidth(2)
  hist.SetMarkerStyle(7)
  hist.SetLineColor(ROOT.kRed)
  hist.GetYaxis().SetTitle('efficiency')
  hist.GetYaxis().SetTitleOffset(1.5)
  hist.GetXaxis().LabelsOption('v')

mean.SetMaximum(0.55)
mean.SetMinimum(0.25)
mean.GetYaxis().SetTitle('mean')

first.SetMaximum(0.90)
first.SetMinimum(0.86)

second.SetMaximum(0.96)
second.SetMinimum(0.90)

fourth.SetMaximum(0.98)
fourth.SetMinimum(0.94)


c1 = ROOT.TCanvas('','',2000,2000)

ROOT.gPad.SetLeftMargin(0.18)
ROOT.gPad.SetBottomMargin(0.25)
ROOT.gPad.SetFrameLineWidth(3)
ROOT.gPad.SetGridx(1)
ROOT.gPad.SetGridy(1)

mean.Draw('H][')
c1.SaveAs('mean.pdf'  )
first.Draw('H][')
c1.SaveAs('first.pdf' )
second.Draw('H][')
c1.SaveAs('second.pdf')
fourth.Draw('H][')
c1.SaveAs('fourth.pdf')
