#!/bin/tcsh -f
       setenv SCRAM_ARCH slc6_amd64_gcc481
       set W_DIR = "/afs/cern.ch/work/m/manzoni/TauHLT/700_v2/CMSSW_7_0_0/src/TriggerStudies/Tau/test/batch"
       set CFG = "/afs/cern.ch/work/m/manzoni/TauHLT/700_v2/CMSSW_7_0_0/src/TriggerStudies/Tau/test/batch/cfgs/hlt.py"
       cd $W_DIR
       eval `scramv1 runtime -csh`
       cmsenv
       cmsRun $CFG > hlt.log
       #/afs/cern.ch/cms/caf/scripts/cmsStage RESFILE EOSDIR
       #rm RESFILE
