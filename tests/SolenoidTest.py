from src.InstPyr.Interfaces.Rigol import Rigol832
from src.InstPyr.MyDevices.switch import switch
from src.InstPyr.Interfaces.MCCDaq import myMcc
import matplotlib.pyplot as plt
import time
import numpy as np

PERIOD=1
ACTVOLTAGE=6.5
OFFVOLTAGE=0
CHANNEL=1
TCPIN=3

def setState(state:bool):
    if state==True:
        ps.setDigitalVoltage(OFFVOLTAGE,CHANNEL)
    else:
        ps.setDigitalVoltage(ACTVOLTAGE,CHANNEL)


tc=myMcc.myMcc()


ps=Rigol832.Rigol832()
ps.setDigitalVoltage(ACTVOLTAGE,CHANNEL)
valve=switch(ps,CHANNEL)
valve.setstate(True)
state=False
count=0
print(tc.readTemperature(TCPIN))

# counts=[]
# Temp=[]
# plt.ion()
# h1,=plt.plot([],[])
plt.ion()
plt.show()
countarr=[]
Temparr=[]
while True:

    print(state)
    setState(state)
    state=True if state is False else False

    if state is True:
        count+=1
        # countarr+=[count]
        print('Cycles: ' + str(count))
        Temp = tc.readTemperature(TCPIN)
        # Temparr+=[Temp]
        if Temp>50:
            #cool down every 10000 cycles
            #stop for x seconds
            print('cooling down')
            time.sleep(600)
        print(count)
        print(Temp)
        # plt.plot(countarr,Temparr)
        # h1.set_xdata(np.append(h1.get_xdata(),count))
        # h1.set_ydata(np.append(h1.get_ydata(), Temp))
        # plt.draw()
        # plt.pause(0.001)
    time.sleep(PERIOD/2)

