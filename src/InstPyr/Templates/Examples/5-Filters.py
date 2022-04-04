import os
path=os.getcwd()
if 'InstPyr\Templates' in path:
    from src.InstPyr.Templates.Template_Backend import *
else:
    from InstPyr.Templates.Template_Backend import *


#remove src. when copying out the template
from src.InstPyr.Interfaces.simulator import simulator
from src.InstPyr.Control.Filter import MyFilter,RateLimiter,FilterTypes
from src.InstPyr.Control.Waveform import triangle



class MainWindow(QMainWindow,Template_Backend):
    def __init__(self):
        super(self.__class__,self).__init__(PIDMode=False,ATMode=False,DUALPLOT=False)
        # PID Mode: Show PID controls
        # AT Mode: Show Autotuning controls
        # DUALPLOT: Add a secondary plot

        #use mutex.lock() and mutex.unlock() every time you access shared variables from a thread
        self.mutex=QMutex()



        #Setup interface and devices
        self.inst=simulator()



        #Setup variables
        self.variable=0
        self.filteredvariable=0
        self.ratelimitedvariable=0
        self.cutoff=1
        self.Sampling.blockSignals(True)
        self.Sampling.setValue(10)
        self.Sampling.blockSignals(False)
        self.samplingrate=100

        #Define a rate filter- units/second
        self.ratefilter=RateLimiter(0.1)

        #define a low pass filter
        self.filtertype=FilterTypes.LOWPASS
        self.myfilter=MyFilter(type=self.filtertype,samplingrate=1000/self.samplingrate,cutoff=self.cutoff)
        self.trianglewave=triangle(samplerate=self.Sampling.value(),frequency=0.1,maxval=1,minval=0)



        #Define controls and callback functions
        self.addDropdown('Filter Type',['Lowpass','Highpass','MovingAverage'],callback=self.typechanged)
        self.addNumeric('Cutoff Frequency',min=0,max=100,stepsize=0.01,default=self.cutoff,callback=self.cutoffchanged)

        #setup a 'watch' for every variable that you want to plot and append that to 'watchlist'
        self.watchlist.append(watch('A single variable', nameof(self.variable),self.variableProbe))
        self.watchlist.append(watch('Filtered variable', nameof(self.filteredvariable),self.variableProbe))
        self.watchlist.append(watch('Rate limited variable (0.1 units/second)', nameof(self.ratelimitedvariable),self.variableProbe))




        #************STATIC CODE************
        self._postInit()


    def mainloop(self):
        #Read sensors and update variables
        self.variable=10*self.trianglewave.nextval()+self.inst.readTemperature(1)/10
        self.filteredvariable=self.myfilter.nextVal(self.variable)
        self.ratelimitedvariable=self.ratefilter.nextVal(self.variable)


        #PID assignments- Assign variable to control to self.PV, input self.controlsig to actuator



        #************STATIC CODE************
        self.mainloop_static()

    def cutoffchanged(self,val):
        self.mutex.lock()
        if val<=(1000/self.samplingrate)/2:
            self.myfilter=MyFilter(type=self.filtertype,samplingrate=1000/self.samplingrate,cutoff=val)
            self.cutoff=val
        self.mutex.unlock()

    def typechanged(self,index):
        self.mutex.lock()
        if index==0:
            self.filtertype=FilterTypes.LOWPASS
        elif index==1:
            self.filtertype=FilterTypes.HIGHPASS
        elif index==2:
            self.filtertype = FilterTypes.MOVINGAVERAGE

        self.myfilter = MyFilter(type=self.filtertype, samplingrate=1000/self.samplingrate, cutoff=self.cutoff)
        self.mutex.unlock()



#************STATIC CODE************
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()