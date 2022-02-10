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
    from src.InstPyr.UI import SinglePlotUI
    import src.InstPyr.Interfaces.simulator as simulator
    from src.InstPyr.Plotting.PlotterWatch import MyPlotterWatch as Plotter
    from src.InstPyr.Logging import Logger
    from src.InstPyr.Utilities.watch import watch
    from src.InstPyr.Control.Plant import Plant
    from src.InstPyr.Control.Filter import MyFilter,RateLimiter
    from src.InstPyr.Control.Waveform import *
    from src.InstPyr.Utilities.shiftregister import shiftregister
    from src.InstPyr.Templates.SinglePlot_Bkend import SinglePlot_Bkend
else:
    from InstPyr.UI import SinglePlotUI
    import InstPyr.Interfaces.simulator as simulator
    from InstPyr.Plotting.PlotterWatch import MyPlotterWatch as Plotter
    from InstPyr.Logging import Logger
    from InstPyr.Control.Plant import Plant
    from InstPyr.Utilities.watch import watch
    from InstPyr.Utilities.shiftregister import shiftregister
    from InstPyr.Control.Filter import MyFilter,RateLimiter
    from InstPyr.Control.Waveform import *


from varname import nameof
class MainWindow(QMainWindow,SinglePlot_Bkend):
    def __init__(self):
        #************STATIC CODE************
        super(self.__class__,self).__init__(PIDMode=False)


        #************YOUR CODE GOES HERE************
        #setup interface and devices
        self.interface=simulator.simulator()
        self.simsystem=Plant([1],[1,0.5,1])

        #setup variables
        self.realTemp = 0
        self.procTemp=0
        self.lidTemp=0
        self.processoutput=0
        self.realTemp_filtered=0
        self.scalefactor=1
        self.targetinst=''
        self.realTempRegister=shiftregister(size=10)
        self.rampfilter=RateLimiter(1)


        #Define Controls,Define callback functions past 'MainLoop'
        self.addNumeric('Setpoint',-1,1,0.1,callback=lambda val: setattr(self,'scalefactor',val))
        self.pushbtn=self.addButton('Push Me',latching=True,callback=lambda val: self.startThread(self.asychronousMethod) if val is True else print('this')) #can manipulate pushbtn later if necessary
        subcon=self.addGroup('Sub Controls')
        self.addNumeric('RampRate (C/sec)',1,1000,1,1,parent=subcon,callback= lambda val: setattr(self.rampfilter,'maxrate',val))
        self.addDropdown('Instrument List',['2001dn','2002dn'],parent=subcon,callback=self.dropdownchanged)
        self.addButton('Connect', parent=subcon,callback=self.instconnect)


        #setup a 'watch' for every variable that you want to plot
        self.watchlist.append(watch('Real Temperature (C)',nameof(self.realTemp),callfunc=self.variableProbe))
        self.watchlist.append(watch('Real Temp(filt) (C)', nameof(self.realTemp_filtered),callfunc=self.variableProbe))
        self.watchlist.append(watch('Process Output', nameof(self.processoutput),callfunc=self.variableProbe))
        self.watchlist.append(watch('Process Temperature (C)', nameof(self.procTemp),callfunc=self.variableProbe))
        self.watchlist.append(watch('Lid Temperature (C)', nameof(self.lidTemp),callfunc=self.variableProbe))


        #************STATIC CODE************
        self._postInit()


    def mainloop(self):
        #************YOUR CODE GOES HERE************
        #use this for accurate timekeeping
        newtime=time.time()
        elapsedtime=newtime-self.currentTime
        self.currentTime=newtime

        #update statusbar here:
        self.setStatus('Online')

        self.realTemp=self.scalefactor*self.interface.readTemperature(0)
        self.realTempRegister.push(self.realTemp)
        self.procTemp=self.interface.readTemperature(0)/1000000
        self.lidTemp=self.interface.readTemperature(0)
        self.realTemp_filtered=self.rampfilter.nextVal(self.realTemp)
        self.processoutput=self.simsystem.realTime(self.realTemp,self.currentTime)


        #************STATIC CODE************
        self.loadqueues()


    # ************YOUR CODE GOES HERE************
    #use this method for asynchronous function calls (that could use a separate thread)
    def asychronousMethod(self):
        for i in range(50):
            time.sleep(1)
            print(i)
        self.pushbtn.setChecked(False)



    #Define callbacks functions for your controls here
    def instconnect(self,val):
        print(val)

    def dropdownchanged(self,val):
        print(val)





app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()