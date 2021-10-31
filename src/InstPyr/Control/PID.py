import numpy as np
from gekko import GEKKO
from scipy.signal import tf2ss
import collections


class PID:
    def __init__(self,Kp,Ki,Kd,out_min=-999999,out_max=999999):
        self.Kp=Kp
        self.Ki=Ki
        self.Kd=Kd
        self.limits=[out_min,out_max]
        self.e_prev=0
        self.t_prev=-0.001
        self.I=0
        self.P=0
        self.D=0

    def apply(self,error,t):
        self.P=self.Kp*error
        self.I=self.I+self.Ki*error*(t-self.t_prev)
        self.D=self.Kd*(error-self.e_prev)/(t-self.t_prev)

        self.e_prev=error
        self.t_prev=t

        output=self.P+self.I+self.D
        return np.max([np.min([output,self.limits[1]]),self.limits[0]])

    @classmethod
    def autotune(self,tf_num, tf_den, tf,steps,amp,
                 Kc_min=0.01, Kc_max=100,
                 Ti_min=0.01,Ti_max=100,
                 Td_min=0.01,Td_max=100,
                 outmin=0,outmax=1000,
                 overshootweight=0,
                 risetimeweight=0,
                 settlingtimeweight=0):
        self.m = GEKKO()

        self.tf = tf
        self.steps = steps
        self.m.time = np.linspace(0, self.tf, self.steps)
        self.step = np.zeros(self.steps)
        self.step[0:10] = 0
        self.step[11:] = amp

        self.Kc = self.m.FV(value=0.01, lb=Kc_min, ub=Kc_max)
        self.Kc.STATUS = 1

        # tauI=3.0
        self.Ti = self.m.FV(value=100, lb=Ti_min, ub=Ti_max)
        self.Ti.STATUS = 1

        # tauD=0.0
        self.Td = self.m.FV(value=100, lb=Td_min, ub=Td_max)
        self.Td.STATUS = 1

        self.OP_0 = 0.0
        self.OP = self.m.Var(value=0, lb=outmin, ub=outmax)
        self.PV = self.m.Var(value=0)
        self.SP = self.m.Param(value=self.step)
        self.Intgl = self.m.Var(value=0)
        self.err = self.m.Intermediate(self.SP - self.PV)
        self.overshoot=self.m.if2(self.err+0.02*self.SP,-self.err,0)
        self.risetime=self.m.if2(self.err-0.1*self.SP,0,self.err)
        self.settlingtime=self.m.if2(self.err-0.2*self.SP,-self.err,0)
        self.settlingtime=self.settlingtime-self.overshoot

        self.m.Equation(self.Intgl.dt() == self.err)
        self.m.Equation(self.OP == self.OP_0 + self.Kc * self.err + (self.Kc / self.Ti) * self.Intgl
                        - self.Kc * self.Td * self.PV.dt())
        self.m.Obj(self.err ** 2 + overshootweight*self.overshoot**2+risetimeweight*self.risetime**2+settlingtimeweight*self.settlingtime**2)
        # TODO make UI control for overshoot weight

        # Process model
        # convert transfer function to statespace
        A, B, C, D = tf2ss(tf_num, tf_den)
        # Find order of equation
        order = len(A)
        x = self.m.Array(self.m.Var, (order))
        # create state variables
        eqn = np.dot(A, x)
        eqn2 = np.dot(C, x)

        for i in range(order):
            self.m.Equation(x[i].dt() == eqn[i] + B[i][0] * self.OP)

        self.m.Equation(self.PV == eqn2[0] + D[0][0] * self.OP)

        self.m.options.IMODE = 6
        self.m.options.MAX_ITER=1000
        # self.m.options.OTOL=0.5
        PIDvals = collections.namedtuple('PIDvals', ['Kc', 'Ti', 'Td'])
        StepResponse=collections.namedtuple('StepResponse',['time','step','PV','OP'])
        print(self.overshoot.value)

        try:
            self.m.solve()

            return PIDvals(self.Kc.value[0],self.Ti.value[0],self.Td.value[0]),StepResponse(self.m.time, self.step,self.PV.value,self.OP.value)

        except Exception:
            print("no solution found")
            return 0


if __name__=="__main__":
    # pid=PID(1,1,1,0,10)
    # t=np.linspace(0,10,100)
    # print(pid.apply(1,0.5))





    # for i in range(len(t)):
    #     next(pid.apply())
    pid,res=PID.autotune([1],[1,10],30,100,1)
    print(pid)
    print(res)