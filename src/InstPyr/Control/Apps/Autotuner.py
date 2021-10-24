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
import numpy as np

class MainWindow(QMainWindow,mainpanel_autotuner.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        self.m=GEKKO()
        self.tf=self.simDuration.value()
        self.steps=self.timeSteps.value()
        self.m.time=np.linspace(0,self.tf,self.steps)
        self.step=np.zeros(self.steps)
        self.step[0:10]=0
        self.step[11:]=self.stepAmp.value()

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
        self.mainplot=Plotter.MyPlotter(self.Plot1, initdata={},buffersize=1000,oneaxis=True,datetimeaxis=False)
        # self.plot.addLine('MovingAvgFilter')

    def eventHandler(self,*args):
        name=self.sender().objectName()
        print(name)

        if name=='Autotune':
            self.parseTF()
            self.parsePID()
            self.Autotune()

        if name=='Simulate':
            pass

    def parseTF(self):
        self.TF_num=self.parseArray(self.Tfnum.text())
        self.TF_den= self.parseArray(self.Tfden.text())

    def parseArray(self,text):
        out_text = text.split('[')[1].split(']')[0].split(',')
        out=[]
        for i in out_text:
            out=out+[float(i)]
        return out

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

    def autotune(self):
        # PID controller model
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
        self.m.Obj(self.err ** 2)

        # Process model
        # Kp = 1
        # tauP = 1
        # x = m.Var(value=0)
        # m.Equation(tauP * x.dt() + 0.25 * x == OP)
        # m.Equation(tauP * PV.dt() + 4 * PV == Kp * x)
        #
        # # m.options.IMODE=4
        # m.options.IMODE = 6
        # m.solve()
        # print('Kc: ' + str(Kc.value[0]))
        print('TauI: ' + str(self.Ti.value[0]))
        print('TauD: ' + str(self.Td.value[0]))


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()