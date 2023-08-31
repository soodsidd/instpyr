import u6
from InstPyr.Interfaces.Common import interface,inf_enums

class MyU6(interface.interface):
    def __init__(self):
        super().__init__(self)

        self.inst=u6.U6()
        self.inst.getCalibrationData()

    def getAIN(self,channel, differential=False,gainIndex=1,settlingFactor=6):
        if self.inst is not None:
            return self.inst.getAIN(channel,differential=False,gainIndex=0,settlingFactor=6)

    def close(self):
        if self.inst is not None:
            self.inst.close()
            self.inst=None

if __name__=='__main__':
    inst=MyU6()
    scalefactor=100
    print(inst.getAIN(0)*scalefactor)
    inst.close()
