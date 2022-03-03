import os
path=os.getcwd()
if 'InstPyr\Templates' in path:
    from src.InstPyr.Templates.Template_Backend import *
else:
    from InstPyr.Templates.Template_Backend import *


#remove src. when copying out the template
from src.InstPyr.Interfaces.simulator import simulator
from src.InstPyr.Control.Filter import MyFilter,RateLimiter


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
        #Define a rate filter- units/second
        self.ratefilter=RateLimiter(0.1)
        self.filter=MyFilter(size=10)



        #Define controls and callback functions



        #setup a 'watch' for every variable that you want to plot and append that to 'watchlist'
        self.watchlist.append(watch('A single variable', nameof(self.variable),self.variableProbe))
        self.watchlist.append(watch('Filtered variable (10 pt mov average)', nameof(self.filteredvariable),self.variableProbe))
        self.watchlist.append(watch('Rate limited variable (0.1 units/second)', nameof(self.ratelimitedvariable),self.variableProbe))




        #************STATIC CODE************
        self._postInit()


    def mainloop(self):
        #Read sensors and update variables
        self.variable=self.inst.readTemperature(1)/10
        self.filteredvariable=self.filter.movingaverage(self.variable)
        self.ratelimitedvariable=self.ratefilter.nextVal(self.variable)


        #PID assignments- Assign variable to control to self.PV, input self.controlsig to actuator



        #************STATIC CODE************
        self.mainloop_static()


#************STATIC CODE************
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()