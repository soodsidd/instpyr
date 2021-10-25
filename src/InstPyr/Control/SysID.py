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

MODELPATH='C:\\Users\\soods\\Desktop\\Python\\InstPyr\\src\\InstPyr\\Control\\Models\\model.xls'


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


    def identify_first_order(self, t, u, orig_output, method='lm', p0=[1.0, 1.0]):
        self.inputs = u
        params, params_cov = opt.curve_fit(self.first_order_mdl, t, orig_output,
                                           method=method, maxfev=1000, p0=p0)
        print(params_cov)
        return {'k': params[0], 'tau': params[1]}

    def identify_second_order(self, t, u, orig_output, method='lm', p0=[1.0, 1.0, 0.1],lb=[0,0,1],ub=[10,10,1.001]):
        self.inputs = u
        params, params_cov = opt.curve_fit(self.second_order_mdl, t, orig_output, bounds=(lb,ub),
                                           method=method, maxfev=1000, p0=p0)
        print(params_cov)
        return {'k': params[0], 'wn': params[1], 'zeta': params[2]}


if __name__=='__main__':
    sysid=TF_identificator()
    df=pd.read_excel(MODELPATH)
    time=df['Time'].to_list()
    input=df['input'].to_list()
    output=df['output'].to_list()
    params=sysid.identify_second_order(time,input,output,method='trf',p0=[1,2,1])

    simout=sysid.second_order_mdl(time,params['k'],params['wn'],params['zeta'])
    print(params)

    plt.figure()
    plt.plot(time,input)
    plt.plot(time,output)
    plt.plot(time,simout)
    plt.show()
