from wipy.wicontrol import *
from wipy.wislicemonitor import InstrumentSliceMonitor

class MyHPLC():
    def __init__(self, ip='127.0.0.1',port=10023):
        self.inst=InstrumentControl(ip,port)
        self.instconnected=False

    def connect(self):
        self.inst.Connect()
        self.instconnected=True

    def setFlowRatemLmin(self,flow):
        self.inst.Execute("SetDevicePropertyValueImmediate 0 0 0 0 6 %f" % flow)

    def getFlowRatemLmin(self,):
        a=self.inst.Execute("GetDevicePropertyValueImmediate 0 0 0 0 6")

    def close(self):
        self.inst.Disconnect()
        self.instconnected=False

