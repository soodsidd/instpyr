import os
import time

path=os.getcwd()
if 'InstPyr\Templates' in path:
    from src.InstPyr.Templates.Template_Backend import *
else:
    from InstPyr.Templates.Template_Backend import *


#remove src. when copying out the template
from src.InstPyr.Interfaces.simulator import simulator


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

        #Variables that will be controlled
        self.controlvar=0
        self.valvestate=False

        #Define controls and callback functions

        #use lambda functions to define inline callbacks- this one updates variable directly
        self.addNumeric('Setpoint',-1,1,0.1,callback=lambda val: setattr(self,'controlvar',val))

        #lambda can also be used to add parameters, the button returns the handle to the button widget. You can use this later in code to change state:
        self.pushbtn=self.addButton('Push Me',latching=True,callback=lambda val: self.startThread(self.asychronousMethod) if val is True else print('this')) #can manipulate pushbtn later if necessary

        #A control group pulls related items together- assign controls to this group by using the 'parent' parameter
        subcon=self.addGroup('Sub Controls')

        #All callbacks, if not using lambda will return a 'val'
        self.addDropdown('Instrument List',['2001dn','2002dn'],parent=subcon,callback=self.dropdownchanged)
        self.addButton('Connect', parent=subcon,callback=self.instconnect)

        #Add an indicator and save the object for future manipulation
        self.valveindicator=self.addIndicator('Valve State',default=True)

        #setup a 'watch' for every variable that you want to plot and append that to 'watchlist'
        self.watchlist.append(watch('A single variable', nameof(self.variable),self.variableProbe))



        #************STATIC CODE************
        self._postInit()


    def mainloop(self):
        #Read sensors and update variables
        try:
            if(self.mutex.tryLock()):
                self.variable=self.inst.readTemperature(1)
                self.mutex.unlock()
        except Exception as e:
            print(e)
        self.valvestate=not self.valvestate
        self.valveindicator.setChecked(self.valvestate)

        #PID assignments- Assign variable to control to self.PV, input self.controlsig to actuator



        #************STATIC CODE************
        self.mainloop_static()


    #PLACE CALLBACKS HERE

    def asychronousMethod(self):
        #Acquire mutex lock here as we will be manipulating a shared variable
        print('here')
        self.mutex.lock()
        count=0
        while (count<10):
            self.variable=2
            time.sleep(1)
            count+=1
        self.mutex.unlock()

        #Turn off button after routine complete
        self.pushbtn.setChecked(False)

    def dropdownchanged(self,val):
        print(val)

    def instconnect(self,val):
        print('Instrument connection:'+str(val))


    def closeEvent(self, a0: QtGui.QCloseEvent):
        #peform cleanup here


        #**************STATIC CODE************
        self.closeApp()

#************STATIC CODE************
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()