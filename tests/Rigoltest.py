from src.InstPyr.Interfaces.Rigol.Rigol832 import Rigol832

import time

mydevice=Rigol832()
mydevice.setDigitalVoltage(10,1,0.5)
mydevice.write_digital(1,0)
print(mydevice.getCurrent(1))
state=0
while True:
    mydevice.write_analog(2,voltage=0.1,mode='CV')
    time.sleep(0.5)