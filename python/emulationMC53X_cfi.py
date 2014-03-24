'''

Emulate the L1 and UCT upgrade primitives, and put them in the event.

For MC we need to add an extra step to work around an HCAL bug.  After the
hcalDigis, we need to re-emulate the TPGs from the full readout.
This wraps the normal from-data behaviour in emulator_cfi and adds MC specific
HCAL TPG emulation step.

Authors:  Michal Bluj

'''

from L1Trigger.UCT2015.emulation_cfi import *  # NOQA
from L1Trigger.Configuration.ValL1Emulator_cff import *  # NOQA
process.load("SimCalorimetry.HcalSimProducers.hcalUnsuppressedDigis_cfi")
process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")


print "Using workarounds for MC RAW data content bugs"

process.hcalReEmulDigis = process.simHcalTriggerPrimitiveDigis.clone()
process.hcalReEmulDigis.inputLabel = cms.VInputTag(cms.InputTag('hcalDigis'), cms.InputTag('hcalDigis'))
process.HcalTPGCoderULUT.LUTGenerationMode = cms.bool(True)
process.hackHCALMIPs.src = cms.InputTag("hcalReEmulDigis")

process.emulationSequence.replace(process.hcalDigis,
                                  process.hcalDigis+process.hcalReEmulDigis) #Reproduce HCal digis 




