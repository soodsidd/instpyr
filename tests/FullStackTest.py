from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
# from Logging import Logger
from src.InstPyr.UI import mainpanel
from queue import Queue
from datetime import datetime
# from Plotting import Plotter
# from Interfaces.MCCDaq import myMcc
# from Interfaces.simulator import simulator
# import MyDevices.thermocouple as thermocouple
# from Control.Sensor import MySensor
# from Control.Filter import MyFilter
# from MyDevices.helpers import *
import time
import src.InstPyr.Interfaces.simulator as simulator
# from src.InstPyr.Control.Sensor import MySensor
from src.InstPyr.Control.Filter import MyFilter
from src.InstPyr.MyDevices.thermocouple import thermocouple
from src.InstPyr.Plotting import Plotter
from src.InstPyr.Logging import Logger
from src.InstPyr.Utilities import watch


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)

class MainWindow(QMainWindow,mainpanel.Ui_MainWindow):
    statusmsg = pyqtSignal(str, name='statusmsg')
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.checkboxcount=0

        # self.formLayout.addWidget(self.checkbox3)

        #setup interface and devices
        # self.interface=myMcc.myMcc()
        self.interface=simulator.simulator()
        # self.thermocouple1=thermocouple.thermocouple(self.interface,2)
        # self.thermocouple2=thermocouple.thermocouple(self.interface,2)
        # self.thermocouple3=thermocouple.thermocouple(self.interface,1)#1,2,4,5 work
        # self.thermocouple4=thermocouple.thermocouple(self.interface,4)#1,2,4,5,6 work 5- is quartz cuvette

        #create dictionary of thermocouples
        thermconfig={'skbot':[2,'Temperature_SkirtBottom(C)'],
                     'sktop': [1, 'Temperature_SkirtTop(C)'],
                     'Cuv': [4, 'Temperature_Cuvette(C)']}
        self.sensors={}
        self.var_checkboxes=[]
        for t in thermconfig.keys():
            self.sensors[t]=watch.watch(thermocouple(self.interface,thermconfig[t][0]),thermocouple.readTemperature,name=thermconfig[t][1],buffer=100)
            # self.var_checkboxes+=[self.addCheckbox(thermconfig[t][1],t)]
        self.sensors['Lowpass']=watch.watch(self.sensors['sktop'],lambda x: MyFilter.lowpass(list(x.buffer),0.25,10),
                                                 'Low pass filter (C)')

        self.logger=None

        #initialize sensor variables
        # self.sensornames=['Temperature_SkirtBottom (C)','Temperature_SkirtTop (C)','Temperature_Cuvette (C)']


        #setup widgets
        self.plot=Plotter.MyPlotter(self.plot, initdata={self.sensors[x].name:[] for x in self.sensors.keys()},buffersize=1000,oneaxis=True)
        # self.plot.addLine('MovingAvgFilter')


        for key in self.sensors.keys():
            self.var_checkboxes+=[self.addCheckbox(self.sensors[key].name,key)]
        self.statusmsg.connect(self.eventHandler)

        #shared variables
        self.buffersize=self.Buffersize.value()
        self.samplingrate=100#int(1000/self.Sampling.value())
        self.logfilename=''
        self.logEnable=False

        #setup threads
        self.threadpool=QThreadPool()
        self.dispQueue=Queue()
        dispWorker=Worker(self.update_display)
        self.threadpool.start(dispWorker)

        self.logQueue = Queue()
        logWorker = Worker(self.logdata)
        self.threadpool.start(logWorker)

        self.eventQueue=Queue()
        # print(self.var_checkboxes)

        self.timer=QtCore.QTimer()
        self.timer.setInterval(self.samplingrate)
        self.timer.timeout.connect(self.mainloop)
        self.timer.start()
        self.logQueue.join()
        self.dispQueue.join()

    def mainloop(self):
        # for t in self.thermocouples:
        #     t.readTemperature()

        data=[datetime.now()]+[x.read() for x in self.sensors.values()]
        # filtered=MyFilter.lowpass(list(self.sensors['sktop'].buffer),0.25,10)
        # data+=[filtered]
        self.dispQueue.put(data)
        if self.logEnable:

        #     self.logQueue.put(data)
        #
        # #     #poll event queue
            try:
                event=self.eventQueue.get(timeout=0.1)
                self.logQueue.put(data+[event])
            except Exception:
                self.logQueue.put(data)




    def update_display(self):
        while(True):
            data=self.dispQueue.get(timeout=1000)
            self.dispQueue.task_done()
            self.plot.updatedata(data)
            self.plot.redraw()

    def logdata(self):
        while True:
            data = self.logQueue.get()
            self.logQueue.task_done()
            if self.logger is not None and self.logEnable:
                self.logger.writetimedata(data)



    def eventHandler(self,*args):
        name=self.sender().objectName()
        print(name)
        if name=="logenable":
            self.logEnable=self.logenable.isChecked()
            if self.logEnable is True and self.filename.toPlainText() != '':
                if self.logger is not None:
                    #if filename is new, create new logger
                    # print(self.logger.fname)
                    # print(self.filename.toPlainText())
                    if self.logger.fname != self.filename.toPlainText():
                        #close previous file
                        self.logger.close()
                        try:
                            self.logger=Logger.Logger(self.filename.toPlainText(),[x.name for x in self.sensors.values()],'w+')
                            self.statusmsg.emit('Recording')
                        except Exception:
                            self.logger=None
                            self.statusmsg.emit('File already exists')
                            self.logenable.setChecked(False)

                    else:
                        while not self.logQueue.empty():
                            try:
                                self.logQueue.get(False)
                            except Exception:
                                continue
                            self.logQueue.task_done()
                        self.logger = Logger.Logger(self.filename.toPlainText(),
                                                    [x.name for x in self.sensors.values()], 'a')
                        self.statusmsg.emit('Recording')

                else:
                    try:
                        self.logger = Logger.Logger(self.filename.toPlainText(), [x.name for x in self.sensors.values()],'w+')
                        self.statusmsg.emit('Recording')
                    except Exception:
                        self.logger=None
                        self.statusmsg.emit('File already exists')
                        self.logenable.setChecked(False)



            elif self.logEnable is False:
                self.statusmsg.emit('')
                if self.logger is not None:
                    self.logger.close()
        if name=='Buffersize':
            self.plot.buffer=int(self.Buffersize.value()*self.Sampling.value())
            self.statusmsg.emit('Changed show last')
        if name=='Sampling':
            # self.timer.stop()
            self.timer.setInterval(int(1000/self.Sampling.value()))
            self.statusmsg.emit('Changed sampling rate')
        if name=='clear':
            self.plot.clear()
        if name=='MainWindow':
            self.statusbar_2.setText(args[0])
        if name=='annotate':
            self.plot.annotate(self.annotatemsg.toPlainText())
            if self.logEnable:
                #construct blank data:
                self.eventQueue.put(self.annotatemsg.toPlainText())
            self.annotatemsg.setText('')

        if name in self.var_checkboxes:
            exec("self.cname=self."+name)
            # print(name)
            # dispname=self.skbot.text()
            if self.cname.isChecked():
                self.plot.show(self.cname.text())
            else:
                self.plot.hide(self.cname.text())
            # pass

            #TODO - annotate at any timestamp

    def addCheckbox(self,dispname, varname):
        print(dispname,varname)
        exec("self."+varname+"=QtWidgets.QCheckBox(self.groupBox)")
        exec("self.checkboxname=self."+varname)
        self.checkboxname.setObjectName(varname)
        self.checkboxname.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkboxname.setFont(font)
        # self.checkbox3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkboxname.setText(dispname)
        self.checkboxname.setChecked(True)
        # self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkbox3)
        self.formLayout.setWidget(self.checkboxcount, QtWidgets.QFormLayout.LabelRole, self.checkboxname)
        self.checkboxname.stateChanged['int'].connect(self.eventHandler)
        self.checkboxcount+=1
        return varname






app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()