import src.InstPyr.Control.Plant as plant
import src.InstPyr.Control.PID as PID
import numpy as np
import matplotlib.pyplot as plt


motor=plant.Plant([1,1],[1,2])
nt=1000
t=np.linspace(0,100,nt)

# motor.impulseResponse()

# plt.close('all')

pid=PID.PID(0.5,5,0,0,10)
# pid=PID.PID(10,0,0,0,10)
setpoint=1
y=[]
controloutput=[]
control=0

for i in range(len(t)):
    out=motor.realTime(control,t[i])
    # print(out)
    error=setpoint-out
    # print(error)
    control=pid.apply(error,t[i])
    control_P=pid.P
    control_I=pid.I
    controloutput.append(control_P)
    y.append(out)

plt.plot(t,y)
# plt.plot(t,controloutput)
plt.show()




