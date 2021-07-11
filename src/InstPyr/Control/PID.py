import numpy as np

class PID:
    def __init__(self,Kp,Ki,Kd,out_min,out_max):
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







if __name__=="__main__":
    pid=PID(1,1,1,0,10)
    t=np.linspace(0,10,100)
    print(pid.apply(1,0.5))





    # for i in range(len(t)):
    #     next(pid.apply())