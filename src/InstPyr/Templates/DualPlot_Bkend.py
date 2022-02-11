import threading

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
import time
from queue import Queue
from datetime import datetime
import os
import numpy as np
path=os.getcwd()
curr=os.path.basename(path)
if curr=='Templates':
    from src.InstPyr.UI import DualPlotUI
    import src.InstPyr.Interfaces.simulator as simulator
    from src.InstPyr.Plotting.PlotterWatch import MyPlotterWatch as Plotter
    from src.InstPyr.Logging import Logger
    from src.InstPyr.Utilities.watch import watch
    from src.InstPyr.Control.Plant import Plant
    from src.InstPyr.Control.Filter import MyFilter,RateLimiter
    from src.InstPyr.Control.Waveform import *
    from src.InstPyr.Utilities.shiftregister import shiftregister
    from src.InstPyr.Control.PID import PID,PIDAutotuneRT, TuningStatus
else:
    from InstPyr.UI import DualPlotUI
    import InstPyr.Interfaces.simulator as simulator
    from InstPyr.Plotting.PlotterWatch import MyPlotterWatch as Plotter
    from InstPyr.Logging import Logger
    from InstPyr.Control.Plant import Plant
    from InstPyr.Utilities.watch import watch
    from InstPyr.Utilities.shiftregister import shiftregister
    from InstPyr.Control.Filter import MyFilter,RateLimiter
    from InstPyr.Control.Waveform import *
    from InstPyr.Control.PID import PID,PIDAutotuneRT, TuningStatus



from varname import nameof
#************STATIC CODE************
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)

class DualPlot_Bkend(DualPlotUI.Ui_MainWindow):
    def __init__(self, PIDMode=True, ATMode=True):
        #************STATIC CODE************
        # super(self.__class__,self).__init__()
        self._appsetup()



        if PIDMode:
            #PID variables:
            self.P=0
            self.I=1000
            self.D=0
            self.PV=0
            self.outmin=0
            self.outmax=100
            self.controlsig=0
            self.setpoint=0
            self.PIDenable=True
            self.PID=PID(self.P,self.I,self.D,self.outmin,self.outmax)

            # PID controls:
            self.pidgrp = self.addGroup('PID control')
            self.setpointctrl=self.addNumeric('Setpoint', -1000, 1000, 0.1, 0, self.pidgrp,
                            callback=lambda val: setattr(self, 'setpoint', val))
            self.Pctrl = self.addNumeric('P', 0, 1000, 0.1, 0, self.pidgrp, callback=self.pidchange)
            self.Ictrl = self.addNumeric('I', 0, 1000, 0.1, 1000, self.pidgrp, callback=self.pidchange)
            self.Dctrl = self.addNumeric('D', 0, 1000, 0.1, 0, self.pidgrp, callback=self.pidchange)
            self.outminctrl = self.addNumeric('OutMin', -1000, 1000, 0.1, 0, self.pidgrp, callback=self.pidchange)
            self.outmaxctrl = self.addNumeric('OutMax', -1000, 1000, 0.1, 100, self.pidgrp, callback=self.pidchange)

            self.addButton('DisablePID', latching=True, parent=self.pidgrp,
                           callback=lambda val: setattr(self, 'PIDenable', not val))
            self.addNumeric('Direct', -1000, 1000, 0.1, 0, self.pidgrp,
                            callback=lambda val: setattr(self, 'controlsig', val))

            if ATMode:
                #Autotuning Variables
                self.PIDAT=None
                self.ATprevStatus=0
                self.ATstatus=0
                self.ATactive=False
                self.ATsetpoint=0
                self.ATmethod=0
                self.ATCoarseAmp=0
                self.ATFineAmp=0
                self.ATcycles=3
                # PID autotuning controls:
                self.ATgroup = self.addGroup('Autotuning', self.pidgrp)
                self.addNumeric('AT Setpoint', -1000, 1000, 0.1, 0, self.ATgroup,
                                callback=lambda val: setattr(self, 'ATsetpoint', val))
                self.addNumeric('AT Coarse Amp', -1000, 1000, 0.1, 0, self.ATgroup,
                                callback=lambda val: setattr(self, 'ATCoarseAmp', val))
                self.addNumeric('AT Fine Amp', -1000, 1000, 0.1, 0, self.ATgroup,
                                callback=lambda val: setattr(self, 'ATFineAmp', val))
                self.addNumeric('AT Cycles', 0, 10, 1, 3, parent=self.ATgroup,
                                callback=lambda val: setattr(self, 'ATcycles', val))
                self.addDropdown('AT Method', ['ZN- P', 'ZN-PI', 'ZN-PID', 'TL-PI', 'TL-PID'], parent=self.ATgroup,
                                 callback=lambda val: setattr(self, 'ATmethod', val))
                self.ATbtn = self.addButton('Autotune!', latching=True, parent=self.ATgroup,
                                            callback=lambda val: self.autotuningTrigger(val))











    def mainloop(self):
        #************YOUR CODE GOES HERE************
        #use this for accurate timekeeping
        pass





        #************STATIC CODE************
        self.loadqueues()


    # ************YOUR CODE GOES HERE************
    #use this method for asynchronous function calls (that could use a separate thread)
    def autotuningRoutine(self):
        if self.ATactive:
            control,self.ATstatus=self.PIDAT.nextVal(self.PV,self.controlsig)
            self.setStatus(str(self.ATstatus))
            if self.ATstatus==TuningStatus.COARSE_SETTLING:
                print(self.PIDenable)
                print(self.ATactive)
                pass
            elif self.ATstatus==TuningStatus.COARSE_READY or self.ATstatus==TuningStatus.FINE_READY:
                params=self.PIDAT.PIDparameters()
                self.P=params['Kc']
                self.I=params['Ti']
                self.D=params['Td']
                self.Pctrl.setValue(self.P)
                self.Ictrl.setValue(self.I)
                self.Dctrl.setValue(self.D)
                self.pidchange()
                self.setpoint=self.ATsetpoint
                self.PIDenable=True
                if self.ATstatus == TuningStatus.FINE_READY:
                    self.ATbtn.setChecked(False)
                    self.ATactive=False
                    self.PIDenable=True
                    self.PIDAT=None
            elif self.ATstatus == TuningStatus.COARSE_RELAY or self.ATstatus == TuningStatus.FINE_RELAY:
                self.controlsig=control

            elif self.ATstatus==TuningStatus.DWELL:
                if self.ATstatus!=self.ATprevStatus:
                    self.PIDenable=False

                self.controlsig=control

            self.ATprevStatus=self.ATstatus



    #Define callbacks functions for your controls here
    def pidchange(self):
        self.PID=PID(self.Pctrl.value(),self.Ictrl.value(),self.Dctrl.value(),self.outminctrl.value(),self.outmaxctrl.value())
        self.P=self.Pctrl.value()
        self.I=self.Ictrl.value()
        self.D=self.Dctrl.value()
        self.outmin=self.outminctrl.value()
        self.outmax=self.outmaxctrl.value()


    def autotuningTrigger(self, enable):
        if enable:
            self.ATactive=True
            self.PIDenable=False
            self.PIDAT=PIDAutotuneRT(self.ATsetpoint,self.ATCoarseAmp,self.ATFineAmp,cycles=self.ATcycles,method=int(self.ATmethod), midpoint=self.ATCoarseAmp/2)
            # self.startThread(self.autotuningRoutine)
        else:
            self.ATactive=False
            self.PIDenable=True


    # ************STATIC CODE************
    def _appsetup(self):
        self.setupUi(self)
        self.ControlBay.hide()
        #Setup variables
        self.watchlist=[]
        self.logger = None
        self.samplingrate = int(1000/self.Sampling.value())
        self.logfilename = ''
        self.logenable = False
        self.currentTime=time.time()
    def _postInit(self):
        # ************STATIC CODE************
        # setup widgets
        self.plot_top = Plotter(self.Mainplot_top,datetimeaxis=False, variables=[x for x in self.watchlist if x.plot==0])
        self.plot_bottom = Plotter(self.Mainplot_bottom,datetimeaxis=False, variables=[x for x in self.watchlist if x.plot==1])

        # setup threads
        self.lock=threading.Lock
        self.threadpool = QThreadPool()
        self.dispQueue = Queue()
        dispWorker = Worker(self.update_display)
        self.threadpool.start(dispWorker)

        self.logQueue = Queue()
        logWorker = Worker(self.logdata)
        self.threadpool.start(logWorker)

        self.eventQueue = Queue()

        # Define mainloop timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.samplingrate)
        self.timer.timeout.connect(self.mainloop)
        self.timer.start()
        self.logQueue.join()
        self.dispQueue.join()

        # Redefine UI
        if len(self.ControlBay.findChildren(QtWidgets.QWidget)) is not 0:
            self.ControlBay.show()

        # Reformat watchlist:
        temp = {}
        for item in self.watchlist:
            name = item.variableName
            temp[name] = item
        self.watchlist = temp
    def loadqueues(self):
        vardata = {}
        for watch in self.watchlist.values():
            vardata[watch.name] = watch.read()
        data = [datetime.now(), vardata]
        self.dispQueue.put(data)
        if self.logenable:
            try:
                event = self.eventQueue.get(timeout=0.1)
                self.logQueue.put(data + [event])
            except Exception:
                self.logQueue.put(data)
    def update_display(self):
        while(True):
            data=self.dispQueue.get(timeout=1000)
            self.dispQueue.task_done()
            time=data[0]
            vardata=data[1]
            self.plot_top.updatedata(time,vardata)
            self.plot_bottom.updatedata(time,vardata)

    def logdata(self):
        while True:
            data = self.logQueue.get()
            self.logQueue.task_done()
            if self.logger is not None and self.logenable:
                writedata=[data[0]]
                for key in data[1].keys():
                    writedata.append(data[1][key])
                self.logger.writetimedata(writedata)
    def eventHandler(self,*args):
        name=self.sender().objectName()
        print(name)
        if name=="LogEnable":
            self.logenable=self.LogEnable.isChecked()
            if self.logenable is True and self.filename.toPlainText() != '':
                if self.logger is not None:
                    #if filename is new, create new logger
                    if self.logger.fname != self.filename.toPlainText():
                        #close previous file
                        self.logger.close()
                        try:
                            self.logger=Logger.Logger(self.filename.toPlainText(),[x.name for x in self.watchlist.values()],'w+')
                        except Exception as e:
                            print(e)
                            self.logger=None
                            self.LogEnable.setChecked(False)

                    else:
                        while not self.logQueue.empty():
                            try:
                                self.logQueue.get(False)
                            except Exception as e:
                                print(e)
                                continue
                            self.logQueue.task_done()
                        self.logger = Logger.Logger(self.filename.toPlainText(),
                                                    [x.name for x in self.watchlist.values()], 'a')
                else:
                    try:
                        self.logger = Logger.Logger(self.filename.toPlainText(), [x.name for x in self.watchlist.values()],'w+')
                    except Exception as e:
                        print(e)
                        self.logger=None
                        self.LogEnable.setChecked(False)
            elif self.logenable is False:
                if self.logger is not None:
                    self.logger.close()
        if name=='Buffersize':
            self.plot.buffer=int(self.Buffersize.value()*self.Sampling.value())
            self.statusmsg.emit('Changed show last')
        if name=='Sampling':
            # self.timer.stop()
            self.timer.setInterval(int(1000/self.Sampling.value()))
            self.samplingrate=self.Sampling.value()
        if name=='clear':
            self.plot.clear()
        if name=='annotate':
            self.plot.annotate(self.annotatemsg.toPlainText())
            if self.logEnable:
                #construct blank data:
                self.eventQueue.put(self.annotatemsg.toPlainText())
            self.annotatemsg.setText('')
    def variableProbe(self,name):
        return eval('self.'+name)
    def addButton(self,name,latching=False,parent=None,callback=None):
        btn=QtWidgets.QPushButton(name)
        font = QtGui.QFont()
        font.setPointSize(8)
        btn.setFont(font)
        btn.setCheckable(latching)
        if callback is not None:
            btn.clicked['bool'].connect(callback)
        if parent is None:
            self.verticalLayout_6.addWidget(btn)
        else:
            parent.addWidget(btn)
        return btn
    def addNumeric(self,label,min=0,max=100,stepsize=1.0,default=0,parent=None,callback=None):
        font = QtGui.QFont()
        font.setPointSize(8)
        label=QtWidgets.QLabel(label)
        label.setFont(font)
        doubleEdit=QtWidgets.QDoubleSpinBox()
        doubleEdit.setMinimum(min)
        doubleEdit.setMaximum(max)
        doubleEdit.setSingleStep(0.1)
        doubleEdit.setValue(default)
        doubleEdit.setFont(font)
        hbox=QtWidgets.QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(doubleEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        doubleEdit.setSizePolicy(sizePolicy)
        if parent is None:
            self.verticalLayout_6.addLayout(hbox)
        else:
            parent.addLayout(hbox)
        doubleEdit.setKeyboardTracking(False)
        if callback is not None:
            doubleEdit.valueChanged['double'].connect(callback)
        return doubleEdit
    def addGroup(self,name,parent=None):
        gbox=QtWidgets.QGroupBox(name)
        glayout=QtWidgets.QVBoxLayout(gbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        gbox.setFont(font)
        if parent is None:
            self.verticalLayout_6.addWidget(gbox)
        else:
            parent.addWidget(gbox)
        return glayout
    def addDropdown(self, label,items,parent=None,callback=None):
        vbox=QtWidgets.QVBoxLayout()
        label=QtWidgets.QLabel(label)
        font = QtGui.QFont()
        font.setPointSize(8)
        label.setFont(font)

        drpdown=QtWidgets.QComboBox()
        drpdown.setFont(font)
        drpdown.addItems(items)
        drpdown.setCurrentIndex(0)
        if callback is not None:
            drpdown.currentIndexChanged['int'].connect(callback)

        vbox.addWidget(label)
        vbox.addWidget(drpdown)

        if parent==None:
            self.verticalLayout_6.addLayout(vbox)
        else:
            parent.addLayout(vbox)

        return drpdown
    def addTextInput(self, label,placeholder,parent=None,callback=None):
        vbox=QtWidgets.QVBoxLayout()
        label=QtWidgets.QLabel(label)
        font = QtGui.QFont()
        font.setPointSize(8)
        label.setFont(font)

        linedit=QtWidgets.QLineEdit()
        linedit.setFont(font)
        linedit.setPlaceholderText(placeholder)
        if callback is not None:
            linedit.textChanged['QString'].connect(callback)

        vbox.addWidget(label)
        vbox.addWidget(linedit)

        if parent==None:
            self.verticalLayout_6.addLayout(vbox)
        else:
            parent.addLayout(vbox)

        return linedit
    def setStatus(self,text):
        print(text)
    def startThread(self,callback):
        wrkr = Worker(callback)
        self.threadpool.start(wrkr)
