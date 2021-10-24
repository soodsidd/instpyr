from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from src.InstPyr.UI import mainpanel_autotuner
from queue import Queue
import time
from src.InstPyr.Plotting import Plotter
from gekko import GEKKO
from scipy.signal import tf2ss
import numpy as np

OVERSHOOT_WEIGHT=0

class MainWindow(QMainWindow,mainpanel_autotuner.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)


        self.TF_num=[]
        self.TF_den=[]

        #Controlvariables
        self.Kcini=0
        self.KcLb=0
        self.KcUb=0
        self.Tiini=0
        self.TiLb=0
        self.TiUb=0
        self.Tdini=0
        self.TdLb=0
        self.TdUb =0
        self.outmin=0
        self.outmax=0




        #setup widgets
        self.mainplot=Plotter.MyPlotter(self.Plot1, initdata={'Setpoint':[],
                                                              'Process Variable':[]},buffersize=1000,oneaxis=True,datetimeaxis=False)

        self.controllerplot = Plotter.MyPlotter(self.Plot2, initdata={'ControlSignal': []}, buffersize=1000, oneaxis=True,
                                          datetimeaxis=False)

        # self.mainplot.updatedata([self.m.time,self.step])
        # self.mainplot.redraw()

    def eventHandler(self,*args):
        name=self.sender().objectName()
        print(name)

        if name=='Autotune':
            self.parseTF()
            self.parsePID()
            self.autotune()

        if name=='Simulate':
            pass

    def parseTF(self):
        self.TF_num=self.parseArray(self.Tfnum.text())
        self.TF_den= self.parseArray(self.Tfden.text())

    def parseArray(self,text):
        return [float(x) for x in text.strip('][').split(',')]

    def parsePID(self):
        self.Kcini=self.Kc_ini.value()
        self.KcLb=self.Kc_lb.value()
        self.KcUb=self.Kc_ub.value()
        self.Tiini=self.Ti_ini.value()
        self.TiLb=self.Ti_lb.value()
        self.TiUb=self.Ti_ub.value()
        self.Tdini=self.Td_ini.value()
        self.TdLb=self.Td_lb.value()
        self.TdUb=self.Td_ub.value()
        self.outmin=self.out_min.value()
        self.outmax=self.out_max.value()

    def varmultiply(self,mat,s):
        #return a list of summed values
        out=[]
        col=mat.shape[0]
        rows=mat.shape[1]

        for i in range(rows):
            rowsum=0
            for j in range(col):
                rowsum+=mat[i][j]*s[i]
            out+=[rowsum]
        return out



    def autotune(self):
        # PID controller model
        # reinitialize gekko

        self.m=GEKKO()


        self.tf=self.simDuration.value()
        self.steps=self.timeSteps.value()
        self.m.time=np.linspace(0,self.tf,self.steps)
        self.step=np.zeros(self.steps)
        self.step[0:10]=0
        self.step[11:]=self.stepAmp.value()



        self.Kc = self.m.FV(value=self.Kcini, lb=self.KcLb, ub=self.KcUb)
        self.Kc.STATUS = 1

        # tauI=3.0
        self.Ti = self.m.FV(value=self.Tiini, lb=self.TiLb, ub=self.TiUb)
        self.Ti.STATUS = 1

        # tauD=0.0
        self.Td = self.m.FV(value=self.Tdini, lb=self.TdLb, ub=self.TdUb)
        self.Td.STATUS = 1

        self.OP_0 = 0.0
        self.OP = self.m.Var(value=0, lb=self.outmin, ub=self.outmax)
        self.PV = self.m.Var(value=0)
        self.SP = self.m.Param(value=self.step)
        self.Intgl = self.m.Var(value=0)
        self.err = self.m.Intermediate(self.SP - self.PV)
        self.m.Equation(self.Intgl.dt() == self.err)
        self.m.Equation(self.OP == self.OP_0 + self.Kc * self.err + (self.Kc / self.Ti) * self.Intgl
                        - self.Kc * self.Td * self.PV.dt())
        self.m.Obj(self.err ** 2-self.doubleSpinBox.value()*self.err)
        #TODO make UI control for overshoot weight

        # Process model
        #convert transfer function to statespace
        A,B,C,D=tf2ss(self.TF_num,self.TF_den)
        #Find order of equation
        order=len(A)
        x=self.m.Array(self.m.Var,(order))
        #create state variables
        eqn=np.dot(A,x)
        eqn2=np.dot(C,x)


        for i in range(order):
            self.m.Equation(x[i].dt()==eqn[i]+B[i][0]*self.OP)

        self.m.Equation(self.PV==eqn2[0]+D[0][0]*self.OP)

        self.m.options.IMODE = 6
        self.m.solve()
        print('Kc: ' + str(self.Kc.value[0]))
        print('Ti: ' + str(self.Ti.value[0]))
        print('Td: ' + str(self.Td.value[0]))
        self.Kc_ini.setValue(self.Kc.value[0])
        self.Ti_ini.setValue(self.Ti.value[0])
        self.Td_ini.setValue(self.Td.value[0])
        self.mainplot.clear()
        self.controllerplot.clear()
        self.mainplot.updatedata([self.m.time,self.step,self.PV.value])
        self.controllerplot.updatedata([self.m.time,self.OP.value])
        self.mainplot.redraw()
        self.controllerplot.redraw()



app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()