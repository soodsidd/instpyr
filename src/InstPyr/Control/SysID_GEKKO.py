# class SysID:
#     def __init__(self):
#         pass
#
#     @classmethod
#
import numpy as np
from scipy import signal as sig
from scipy import optimize as opt
import pandas as pd
import matplotlib.pyplot as plt
from gekko import GEKKO

MODELPATH='C:\\Users\\soods\\Desktop\\Python\\InstPyr\\src\\InstPyr\\Control\\Models\\model_undamped.xls'


class TF_identificator:
    def __init__(self):
        self.tf = None
        self.inputs = None

    def first_order_mdl(self, t, k, pole):
        self.tf = sig.TransferFunction(k, [pole, 1])
        to, yo, xo = sig.lsim2(self.tf, U=self.inputs, T=t)
        return yo

    def second_order_mdl(self, t, k, wn, delta):
        self.tf = sig.TransferFunction(k*(wn**2), [1, 2*delta*wn, wn**2])
        to, yo, xo = sig.lsim2(self.tf, U=self.inputs, T=t)
        return yo



    def identify_first_order(self,time,input,output):
        m = GEKKO()
        m_time = m.Param(value=time)
        m_input = m.Param(value=input)

        m_tau = m.FV(value=1)
        m_tau.STATUS = 1

        m_k = m.FV(value=1)
        m_k.STATUS = 1

        m_output = m.CV(value=output)
        m_output.FSTATUS = 1

        m.Equation(m_output == m_k * (1 - m.exp(-m_time / m_tau)) * m_input)

        m.options.IMODE = 2
        m.options.MAX_ITER=1000

        m.solve()

        # print(m_k.value[0])
        # print(m_tau.value[0])
        return {'k':m_k.value[0],
                'tau':m_tau.value[0]}

    def identify_second_order_undamped(self,time,input,output):
        m = GEKKO()
        # m_time = m.Param(value=time)
        m.time=time
        m_input = m.Param(value=input)

        m_wn = m.FV(value=0.1, lb=0,ub=1)
        m_wn.STATUS = 1

        m_k = m.FV(value=1,lb=0,ub=10)
        m_k.STATUS = 1

        m_zeta = m.FV(value=0.25,lb=0,ub=0.5)
        m_zeta.STATUS = 1

        m_output = m.Param(value=output)
        # m_output.FSTATUS = 1

        m_sim=m.Var(value=0)

        err=m.Intermediate(m_output-m_sim)
        m_x=m.Var(value=0)
        abserr=m.if2(err,-err,err)


        m.Equation(m_x.dt()+(m_wn**2)*m_sim==m_k*m_input)
        m.Equation(m_sim.dt()+2*m_zeta*m_wn*m_sim==m_x)

        m.Minimize(err**2+abserr)
        m.options.IMODE = 6
        m.options.MAX_ITER = 10000
        m.options.OTOL=1e-12
        m.options.RTOL=1e-12

        m.solve()

        plt.figure()
        plt.plot(time,input)
        plt.plot(time,output)
        plt.plot(time,m_sim.value)
        plt.show()

        # print(m_k.value[0])
        # print(m_tau.value[0])
        return {'k': m_k.value[0],
                'wn': m_wn.value[0],
                'zeta':m_zeta.value[0]}


if __name__=='__main__':
    # sysid=TF_identificator()
    sysid=TF_identificator()
    df=pd.read_excel(MODELPATH)
    time=np.array(df['Time'].to_list())
    input=np.array(df['Input'].to_list())
    output=np.array(df['Output'].to_list())

    # params=sysid.identify_first_order(time,input,output)
    params=sysid.identify_second_order_undamped(time,input,output)

    print(params['k'])
    print(params['wn'])
    print(params['zeta'])
    # print(params['tau'])

    #
    # plt.figure()
    # plt.plot(time,input)
    # plt.plot(time,output)
    # plt.plot(time,simout)
    # plt.show()
