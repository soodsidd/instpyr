import sys
import pyvisa
from ..Common.interface import  interface
from visa import *
import time

_delay=0.01

class Rigol832(interface):
    def __init__(self):
        super().__init__(self)
        self.analogmode='CV'
        try:
            self.rm=pyvisa.ResourceManager()
            self.instrument_list=self.rm.list_resources()

            self.address=[elem for elem in self.instrument_list if (elem.find('USB')!=-1) and elem.find('DP')!=-1]
            if self.address.__len__() == 0:
                self.status = "Not Connected"
                # print("Could not connect to device")
            else:
                self.address = self.address[0]
                self.device = self.rm.open_resource(self.address)
                # print("Connected to " + self.address)
                self.status = "Connected"
                self.connected_with = 'USB'

        except VisaIOError:
            print('Instrument not found')



    def initializeIO(self, din=[], dout=[], ain=[],
                     aout=[]):
        pass


    def write_digital(self, channel, state):
        outputstate='ON' if state==1 else 'OFF'
        command=':OUTP CH%s, %s'%(channel,outputstate)
        print(command)
        self.device.write(command)
        time.sleep(_delay)

    def read_digital(self, channel):
        command=':OUTP? CH%s'%channel
        return self.device.query(command).rstrip()

    def write_analog(self, channel,current=0.0,voltage=0.0,mode=''):
        #TODO change this enum
        if mode !='':
            self.analogmode=mode
        if self.analogmode=='CC':
            self.SetCurrent(channel,current)
        elif self.analogmode=='CV':
            self.SetVoltage(channel, voltage)
        if self.read_digital(channel)=='OFF':
            self.write_digital(channel,1)






    def setDigitalVoltage(self, voltage, channel=1,currentlim=0.0):
        if currentlim==0:
            command=':APPL Ch%s,%s'%(channel,voltage)
        else:
            command=':APPL Ch%s,%s,%s'%(channel,voltage,currentlim)
        self.device.write(command)
        time.sleep(_delay)

    def getCurrent(self,channel):
        command=':MEAS:CURR? CH%s'%(channel)
        return self.device.query(command)

    def getVoltage(self,channel):
        command=':MEAS:VOLT? CH%s'%(channel)
        return self.device.query(command)

    def getPower(self,channel):
        command=':MEAS:POWE? CH%s'%(channel)
        return self.device.query(command)

    def SetCurrent(self,channel,current):
        command=':INST:NSEL %s'%(channel)
        self.device.write(command)
        time.sleep(_delay)
        command=':CURR %s'%current
        time.sleep(_delay)

    def SetVoltage(self,channel,voltage):
        command = ':INST:NSEL %s' % (channel)
        self.device.write(command)
        time.sleep(_delay)
        command = ':VOLT %s' % voltage
        time.sleep(_delay)



if __name__=='__main__':
    mydevice=Rigol832()
    mydevice.setDigitalVoltage(10,1)
    mydevice.write_digital(1,1)


