import ROOT

# file = ROOT.TFile.Open('test.root','read')
# file = ROOT.TFile.Open('test_chi2.root','read')
file = ROOT.TFile.Open('test_chi2_0p1_20.root','read')
file.cd()
file.cd('sorter')
tree = ROOT.gDirectory.FindObjectAny('vertexTree')

failing_match = 0
this_event    = -1

myevents = {}


numVtx          = ROOT.TH1F('numVtx'         ,'numVtx'         ,150 , 0, 150 )
vtxToPass       = ROOT.TH1F('vtxToPass'      ,'vtxToPass'      ,50  , 0, 50  )
position        = ROOT.TH1F('position'       ,'position'       ,50  , 0, 50  )
sumpt2first     = ROOT.TH1F('sumpt2first'    ,'sumpt2first'    ,100 , 0, 1000)
sumpt2match     = ROOT.TH1F('sumpt2match'    ,'sumpt2match'    ,100 , 0, 100)
matchOverFirst  = ROOT.TH1F('matchOverFirst' ,'matchOverFirst' ,50  , 0, 1   )
secondOverFirst = ROOT.TH1F('secondOverFirst','secondOverFirst',50  , 0, 1   )
thirdOverFirst  = ROOT.TH1F('thirdOverFirst' ,'thirdOverFirst' ,50  , 0, 1   )
fourthOverFirst = ROOT.TH1F('fourthOverFirst','fourthOverFirst',50  , 0, 1   )
fifthOverFirst  = ROOT.TH1F('fifthOverFirst' ,'fifthOverFirst' ,50  , 0, 1   )


for event in tree :

  if event.isfirst > 0.5 : continue

  evt        = event.evt
  onlvtxsize = event.onlvtxsize
  ntrk       = event.ntrk      
  ntrk5gev   = event.ntrk5gev  
  ntrk10gev  = event.ntrk10gev 
  cl         = event.cl        
  sumpt2     = event.sumpt2    
  ltpt       = event.ltpt      
  avesumpt   = event.avesumpt  
  isfirst    = event.isfirst
  ismatched  = event.ismatched
  
  if evt != this_event : 
    myevents.update({evt:{'disc':[],'ismatched':[],'sumpt2':[]}})
    myevents[evt]['ismatched'].append(ismatched)
    myevents[evt]['sumpt2'   ].append(sumpt2)
  else : 
    myevents[evt]['ismatched'].append(ismatched)
    myevents[evt]['sumpt2'   ].append(sumpt2)
  
  this_event = event.evt

for event in myevents.keys() :

  try    : position_       = myevents[event]['ismatched'].index(1) 
  except : position_       = -1
  sumpt2match_    = myevents[event]['sumpt2'][position_]
  myevents[event]['sumpt2'].sort(reverse=True)
  sumpt2first_    = myevents[event]['sumpt2'][0]
  matchOverFirst_ = sumpt2match_ / sumpt2first_
  secondOverFirst_= myevents[event]['sumpt2'][1] / sumpt2first_
  thirdOverFirst_ = myevents[event]['sumpt2'][2] / sumpt2first_
  fourthOverFirst_= myevents[event]['sumpt2'][3] / sumpt2first_
  fifthOverFirst_ = myevents[event]['sumpt2'][4] / sumpt2first_

  # if matchOverFirst_ > 0.3 : continue
    
  for i in range(len(myevents[event]['sumpt2'])) :
    #import pdb ; pdb.set_trace()
    if myevents[event]['sumpt2'][i] / sumpt2first_ < 0.5 or sumpt2match_ < -99.9 :
      vtxToPass.Fill(i+1)
      break
    
  numVtx         .Fill(len(myevents[event]['sumpt2']))  
  position       .Fill(position_       ) 
  sumpt2match    .Fill(sumpt2match_    )
  sumpt2first    .Fill(sumpt2first_    )
  matchOverFirst .Fill(matchOverFirst_ )
  secondOverFirst.Fill(secondOverFirst_)
  thirdOverFirst .Fill(thirdOverFirst_ )
  fourthOverFirst.Fill(fourthOverFirst_)
  fifthOverFirst .Fill(fifthOverFirst_ )

histos = []
histos.append(numVtx         )
histos.append(vtxToPass      )
histos.append(position       )
histos.append(sumpt2match    )
histos.append(sumpt2first    )
histos.append(matchOverFirst )
histos.append(secondOverFirst)
histos.append(thirdOverFirst )
histos.append(fourthOverFirst)
histos.append(fifthOverFirst )


outfile = ROOT.TFile.Open('checker2_notmatched.root','recreate')
outfile.cd()
for hist in histos : hist.Write()
outfile.Close() 
  
c1 = ROOT.TCanvas('','',700,700)
numVtx.Draw()      
c1.SaveAs('numVtx.pdf')
vtxToPass.Draw()      
c1.SaveAs('vtxToPass.pdf')
position.Draw()      
c1.SaveAs('position.pdf')
sumpt2match.Draw()   
c1.SaveAs('sumpt2match.pdf')
sumpt2first.Draw()   
c1.SaveAs('sumpt2first.pdf')
matchOverFirst.Draw()
c1.SaveAs('matchOverFirst.pdf')
secondOverFirst.Draw()
c1.SaveAs('secondOverFirst.pdf')
thirdOverFirst.Draw()
c1.SaveAs('thirdOverFirst.pdf')
fourthOverFirst.Draw()
c1.SaveAs('fourthOverFirst.pdf')
fifthOverFirst.Draw()
c1.SaveAs('fifthOverFirst.pdf')




