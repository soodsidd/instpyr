from ..Interfaces.Common import interface,inf_enums
from scipy import interpolate
class thermocouple():
    def __init__(self,interface:interface.interface,pins, type='k', units=inf_enums.TempUnits.CELSIUS):
        self.interface=interface
        self.interface.initializeIO(ain=[pins])
        self.pins=pins
        self.type=type
        self.calX=[]
        self.calY=[]
        self.calfunc=None
        self.currentTemp=0
        if(self.interface.configThermocouple(pins,type)==None):
            self.config(type)
        self.units=units

    def readTemperature(self):
        self.currentTemp=round((self.interface.readTemperature(self.pins,self.units)),3)
        self.currentTemp=self._applyCalibration(self.currentTemp)
        if(self.currentTemp==None):
            return self.calcTemp()
        else:
            return self.currentTemp

    def _applyCalibration(self, rawTemp):
        if self.calfunc is not None:
            return float(self.calfunc(rawTemp))
        else:
            return self.currentTemp

    def calibrate(self,Xin,Yin):
        self.calX=Xin
        self.calY=Yin
        self.calfunc=interpolate.interp1d(self.calX,self.calY)

    def config(self,type):
        pass

    def calcTemp(self):
        pass


