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

MODELPATH='C:\\Users\\ssood\\PycharmProjects\\instpyr\\src\\InstPyr\\Control\\Models\\Step_response_Full_Red.xls'


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
        solved=False
        initwn=0.006
        initk=.46
        initzeta=1.6
        wnbounds=[0,0.01]
        Kbounds=[0,1]
        zetabounds=[1,5]

        while solved==False:
            m = GEKKO()
            # m_time = m.Param(value=time)
            m.time=time
            m_input = m.Param(value=input)

            m_wn = m.FV(value=initwn, lb=wnbounds[0],ub=wnbounds[1])
            m_wn.STATUS = 1

            m_k = m.FV(value=initk,lb=Kbounds[0],ub=Kbounds[1])
            m_k.STATUS = 1

            m_zeta = m.FV(value=initzeta,lb=zetabounds[0],ub=zetabounds[1])
            m_zeta.STATUS = 1

            m_output = m.Param(value=output)
            # m_output.FSTATUS = 1

            m_sim=m.Var(value=0)

            err=m.Intermediate(m_output-m_sim)
            m_x=m.Var(value=0)
            abserr=m.if2(err,-err,err)


            m.Equation(m_x.dt()+(m_wn**2)*m_sim==m_k*m_input)
            m.Equation(m_sim.dt()+2*m_zeta*m_wn*m_sim==m_x)

            m.Minimize(err**2)#+abserr)
            m.options.IMODE = 6
            m.options.MAX_ITER = 10000
            m.options.OTOL=1e-8
            m.options.RTOL=1e-8
            try:
                m.solve(disp=True)
                solved=True
            except Exception:
                initwn=np.random.uniform(wnbounds[0],wnbounds[1])
                initk=np.random.uniform(Kbounds[0],Kbounds[1])
                initzeta=np.random.uniform(zetabounds[0],zetabounds[1])
                print(initk,initwn,initzeta)
                solved=False


        print(m_k.value[0])
        print(m_wn.value[0])
        print(m_zeta.value[0])

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
    sysid.inputs=input

    # params=sysid.identify_first_order(time,input,output)
    params=sysid.identify_second_order_undamped(time,input,output)

    print(params['k'])
    print(params['wn'])
    print(params['zeta'])
    # params=sysid.identify_first_order(time,input,output)
    # simout=sysid.first_order_mdl(time,params['k'],params['tau'])
    simout=sysid.second_order_mdl(time,params['k'],params['wn'],params['zeta'])
    print(simout)
    # print(params['zeta'])
    # print(params['tau'])

    #
    plt.figure()
    # plt.plot(time,input)
    plt.plot(time,output)
    plt.plot(time,simout)
    plt.show()
