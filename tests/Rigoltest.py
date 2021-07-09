from src.InstPyr.Interfaces.Rigol.Rigol832 import Rigol832

import time

mydevice=Rigol832()
mydevice.setDigitalVoltage(10,1,0.5)
mydevice.write_digital(1,0)
print(mydevice.getCurrent(1))
mydevice.setVoltage(1,9)
mydevice.setVoltageLim(0.5,2)
state=0
flag=0
while flag<10:
    mydevice.write_analog(2,voltage=0.1*flag,mode='CV')
    # mydevice.setVoltage(1,7)
    # mydevice.setVoltage(1,9.3)
    # mydevice.setCurrent(2,0.2)
    time.sleep(0.5)
    flag+=1

mydevice.shutdown()