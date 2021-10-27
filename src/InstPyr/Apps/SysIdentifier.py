from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from src.InstPyr.UI import mainpanel_sysid
from queue import Queue
import time
from src.InstPyr.Plotting import Plotter
from src.InstPyr.Control import SysID
from gekko import GEKKO
from scipy.signal import tf2ss
import numpy as np
import pandas as pd
from ast import literal_eval


class MainWindow(QMainWindow,mainpanel_sysid.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)

        self.df=0
        self.fname=0
        self.time=[]
        self.input=[]
        self.actual=[]
        self.model=[]
        self.modelselected=0

        self.sysID=SysID.TF_identificator()
        self.showParameters(0)




        #setup widgets
        self.mainplot=Plotter.MyPlotter(self.plot, initdata={'Input':[],
                                                              'Actual':[],
                                                             'Model':[]},buffersize=1000,oneaxis=True,datetimeaxis=False)



        # self.mainplot.updatedata([self.m.time,self.step])
        # self.mainplot.redraw()

    def eventHandler(self,*args):
        name=self.sender().objectName()
        print(name)

        if name=='loadModel':
            self.fname=self.filename.toPlainText()
            print(self.fname)
            self.df=pd.read_excel(self.fname)
            print(self.df)
            self.time=self.df['Time'].to_list()
            self.input=self.df['Input'].to_list()
            self.actual=self.df['Output'].to_list()

            self.mainplot.clear()
            self.mainplot.updatedata([self.time,self.input,self.actual])
            self.mainplot.redraw()

        if name=='modelselect':
            if self.modelselect.currentIndex()==0:
                self.modelselected=0
                self.showParameters(0)
            else:
                self.modelselected=1
                self.showParameters(1)
        if name=='CuveFit':
            if self.modelselect.currentIndex()==0:
                #first order model
                self.showParameters(0)
                params=self.sysID.identify_first_order(self.time, self.input,self.actual)
                k=params['k']
                tau=params['tau']
                self.K_fo.setText(str(params['k']))
                self.Tau.setText(str(params['tau']))
                self.Tf_num.setText('['+str(k)+']')
                self.Tf_den.setText('['+str(tau)+',1]')
                simout=self.sysID.first_order_mdl(self.time,k,tau)
                for i in range(len(simout)):
                    self.mainplot.updatedata({'Model':[self.time[i],simout[i]]})
                self.mainplot.redraw()
            else:
                self.showParameters(1)
                initialguess=literal_eval(self.initialGuess.text())
                lowerbound=literal_eval(self.lowerB.text())
                upperbound=literal_eval(self.upperB.text())

                params = self.sysID.identify_second_order(self.time, self.input, self.actual, p0=initialguess,lb=lowerbound,ub=upperbound)
                k = params['k']
                wn = params['wn']
                zeta=params['zeta']
                self.K_fo_3.setText(str(params['k']))
                self.K_fo_4.setText(str(params['wn']))
                self.K_fo_2.setText(str(params['zeta']))
                self.Tf_num.setText('[{:.2f}]'.format(k))
                self.Tf_den.setText('[1,{:.2f},{:.2f}]'.format(2*wn*zeta,wn**2))
                simout = self.sysID.second_order_mdl(self.time, k,wn,zeta)
                for i in range(len(simout)):
                    self.mainplot.updatedata({'Model': [self.time[i], simout[i]]})
                self.mainplot.redraw()

    def showParameters(self,order):
        if order==0:
            self.firstOrderModel.setVisible(True)
            self.secondOrderModel.setVisible(False)
        else:
            self.firstOrderModel.setVisible(False)
            self.secondOrderModel.setVisible(True)





if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec_()