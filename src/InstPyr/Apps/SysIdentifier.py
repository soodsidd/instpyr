from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from src.InstPyr.UI import mainpanel_sysid
from queue import Queue
import time
from src.InstPyr.Plotting import Plotter
from src.InstPyr.Control import SysId
from gekko import GEKKO
from scipy.signal import tf2ss
import numpy as np
import pandas as pd
from ast import literal_eval
import xlrd


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

        self.sysID=SysId.TF_identificator()
        self.showParameters(0)




        #setup widgets
        self.mainplot=Plotter.MyPlotter(self.plot, initdata={'Input':[],
                                                              'Actual':[],
                                                             'Model':[]},buffersize=100000,oneaxis=True,datetimeaxis=False)



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
                params=self.sysID.identify_first_order_gek(self.time, self.input,self.actual)
                k=params['k']
                tau=params['tau']
                self.K_fo.setText(str(params['k']))
                self.Tau.setText(str(params['tau']))
                self.Tf_num.setText('['+str(k)+']')
                self.Tf_den.setText('['+str(tau)+',1]')
                simout=params['sim']
                res=params['res']
                self.label_4.setText(str(res))
                self.mainplot.clear('Model')
                for i in range(len(simout)):
                    self.mainplot.updatedata({'Model':[self.time[i],simout[i]]})
                self.mainplot.redraw()
            else:
                self.showParameters(1)
                params = self.sysID.identify_second_order_damped(self.time, self.input, self.actual, dynamicsratiomax=self.spinBox.value())
                k = params['k']
                T1 = params['T1']
                T2=params['T2']
                T3 = params['T3']
                self.K_so.setText(str(k))
                self.T1_so.setText(str(T1))
                self.T2_so.setText(str(T2))
                self.T3_so.setText(str(T3))

                self.Tf_num.setText('[{:.1f},{:.1f}]'.format(k*T3,k))
                self.Tf_den.setText('[{:.1f},{:.1f},1]'.format(T1*T2,(T1+T2)))
                res=params['res']
                simout = params['sim']
                self.label_4.setText(str(res))
                self.mainplot.clear('Model')
                for i in range(len(simout)):
                    self.mainplot.updatedata({'Model': [self.time[i], simout[i]]})
                self.mainplot.redraw()

    def showParameters(self,order):
        if order==0:
            self.firstOrderModel.setVisible(True)
            self.secondOrderModel.setVisible(False)
            self.secondOrderParams.setVisible(False)
        else:
            self.firstOrderModel.setVisible(False)
            self.secondOrderModel.setVisible(True)
            self.secondOrderParams.setVisible(True)






if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec_()