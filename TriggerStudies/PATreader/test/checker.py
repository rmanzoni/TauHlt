import ROOT

file = ROOT.TFile.Open('test.root','read')
file.cd()
file.cd('sorter')
tree = ROOT.gDirectory.FindObjectAny('vertexTree')

failing_match = 0
this_event    = -1

myevents = {}

for event in tree :
#   if event.isfirst > 0.5 : continue

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
  
#   discr = -3.1327991846824776e-02 * sumpt2    + \
#            8.8394987781991623e-04 * ntrk      + \
#            5.7524818636658849e-04 * ntrk5gev  + \
#            1.3525466529345670e-02 * ntrk10gev + \
#            5.6848729864949356e-02 * ltpt      + \
#            1.6917675215048249e-05 * avesumpt 

#   discr =  8.8394987781991623e-04 * sumpt2    + \
#            5.7524818636658849e-04 * ntrk      + \
#            1.3525466529345670e-02 * ntrk5gev  + \
#            5.6848729864949356e-02 * ntrk10gev + \
#            1.6917675215048249e-05 * ltpt      + \
#           -5.6139379732648184e-05 * avesumpt 

#   discr =  8.7935450672209565e-04 * sumpt2    + \
#            3.6420911807874448e-04 * ntrk      + \
#            1.4202446017075245e-02 * ntrk5gev  + \
#            6.2321686696701580e-02 * ntrk10gev + \
#            1.6742885500209335e-05 * ltpt      + \
#           -5.4981590355099178e-05 * avesumpt 


#   print 3.8324663627255950e-04 * sumpt2, '\t', 2.4421095537881357e-04 *ntrk, '\t',6.3290404218937875e-03 * ntrk5gev, '\t', 2.8800916885034698e-02 *ntrk10gev
#   discr =  3.8324663627255950e-04 * sumpt2    + \
#            2.4421095537881357e-04 * ntrk      + \
#            6.3290404218937875e-03 * ntrk5gev  + \
#            2.8800916885034698e-02 * ntrk10gev 

#   discr =  3.8324663630406381e-04 * sumpt2             + \
#           -4.2916529418151064e-02 * ntrk               + \
#            4.3203073772384547e-02 * ntrk-ntrk5gev      + \
#            4.9415876361901409e-02 * ntrk5gev-ntrk10gev + \
#            7.8265682935863348e-02 * ntrk10gev 

  discr =  6.7857799012604862e-04 * sumpt2             + \
          -2.6500643043350961e-04 * ntrk               + \
          -2.4409283096776284e-06 * avesumpt 

#   discr = -1*discr
  
  if evt != this_event : 
    myevents.update({evt:{'disc':[],'ismatched':[],'sumpt2':[]}})
    myevents[evt]['disc'     ].append(discr)
    myevents[evt]['ismatched'].append(ismatched)
    myevents[evt]['sumpt2'   ].append(sumpt2)
  else : 
    myevents[evt]['disc'     ].append(discr)
    myevents[evt]['ismatched'].append(ismatched)
    myevents[evt]['sumpt2'   ].append(sumpt2)
  
  this_event = event.evt

import pdb ; pdb.set_trace()  

bad  = 0
good = 0
for event in myevents.keys() :
  try :
    if myevents[event]['ismatched'].index(1) == myevents[event]['disc'].index(max(myevents[event]['disc'])) : good += 1
    else                                                                                                    : bad  += 1
  except :
    bad += 1
    
print 'tot ', len(myevents)
print 'good', good
print 'bad ', bad



import pdb ; pdb.set_trace()  


#   evt        = event.evt
#   onlvtxsize = event.onlvtxsize
#   ntrk       = event.ntrk      
#   ntrk5gev   = event.ntrk5gev  
#   ntrk10gev  = event.ntrk10gev 
#   cl         = event.cl        
#   sumpt2     = event.sumpt2    
#   ltpt       = event.ltpt      
#   avesumpt   = event.avesumpt  
# #   weigh      = event.weigh     
#   isfirst    = event.isfirst
#   ismatched  = event.ismatched
#   
# 
#   print evt
#   failing_match += 1
# 
# 
# 
# 
# 
# 
# 
#   #print evt
#   #print discr,'\t\t',sumpt2,'\t\t',ismatched,'\t\t',isfirst
#   if evt != this_event :
#     print 'cazzo'
#     disc_dict = {}
#     disc_dict.update({ismatched:[discr,sumpt2]})
#   else :
#     disc_dict.update({ismatched:[discr,sumpt2]})
#   
#   import pdb ; pdb.set_trace()  
#   
#   this_event = evt
#     
# 
