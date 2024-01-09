import os
path=os.getcwd()
if 'InstPyr\Templates' in path:
    from src.InstPyr.Templates.Template_Backend import *
else:
    from InstPyr.Templates.Template_Backend import *


#remove src. when copying out the template
from src.InstPyr.Interfaces.simulator import simulator


class MainWindow(QMainWindow,Template_Backend):
    def __init__(self):
        super(self.__class__,self).__init__(PIDMode=False,ATMode=False,DUALPLOT=True)
        # PID Mode: Show PID controls
        # AT Mode: Show Autotuning controls
        # DUALPLOT: Add a secondary plot

        #use mutex.lock() and mutex.unlock() every time you access shared variables from a thread
        self.mutex=QMutex()



        #Setup interface and devices
        self.inst=simulator()



        #Setup variables
        self.variable=0
        self.variable2=0
        self.time=0



        #Define controls and callback functions



        #setup a 'watch' for every variable that you want to plot
        watch(self,'A single variable', nameof(self.variable),plot=0)
        watch(self,'A second variable', nameof(self.variable2),plot=1)
        watch(self,'Time (s)',nameof(self.time),plot=0)





        #************STATIC CODE************
        self._postInit()


    def mainloop(self):
        #Read sensors and update variables
        self.variable=self.inst.readTemperature(1)
        self.variable2=self.variable/10
        self.time+=1/self.samplingrate

        #PID assignments- Assign variable to control to self.PV, input self.controlsig to actuator



        #************STATIC CODE************
        self.mainloop_static()


    def closeEvent(self, a0: QtGui.QCloseEvent):
        #peform cleanup here


        #**************STATIC CODE************
        self.closeApp()

#************STATIC CODE************
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()