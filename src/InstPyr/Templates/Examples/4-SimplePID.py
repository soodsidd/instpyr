import os
path=os.getcwd()
if 'InstPyr\Templates' in path:
    from src.InstPyr.Templates.Template_Backend import *
else:
    from InstPyr.Templates.Template_Backend import *


#remove src. when copying out the template
from src.InstPyr.Control.Plant import Plant


class MainWindow(QMainWindow,Template_Backend):
    def __init__(self):
        super(self.__class__,self).__init__(PIDMode=True,ATMode=False,DUALPLOT=True)
        # PID Mode: Show PID controls
        # AT Mode: Show Autotuning controls
        # DUALPLOT: Add a secondary plot

        #use mutex.lock() and mutex.unlock() every time you access shared variables from a thread
        self.mutex=QMutex()

        #setup default PID values
        self.Pctrl.setValue(1)
        self.Ictrl.setValue(10)
        self.Dctrl.setValue(0)

        #Controller saturation limits
        self.outminctrl.setValue(-100)
        self.outmaxctrl.setValue(100)


        #Setup interface and devices
        #A simple first order system
        self.system=Plant([1],[100,10,1])



        #Setup variables
        self.variable=0



        #Define controls and callback functions



        #setup a 'watch' for every variable that you want to plot and append that to 'watchlist'
        self.watchlist.append(watch('A single variable', nameof(self.variable),self.variableProbe))

        #PID variables
        self.watchlist.append(watch('Setpoint', nameof(self.setpoint),self.variableProbe))
        self.watchlist.append(watch('Process Variable', nameof(self.PV), self.variableProbe))
        self.watchlist.append(watch('Control Signal', nameof(self.controlsig),self.variableProbe,plot=1))







        #************STATIC CODE************
        self._postInit()


    def mainloop(self):
        #Read sensors and update variables


        #PID assignments- Assign variable to control to self.PV, input self.controlsig to actuator
        self.variable = self.system.realTime(self.controlsig, self.currentTime)
        self.PV=self.variable


        #************STATIC CODE************
        self.mainloop_static()


#************STATIC CODE************
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()