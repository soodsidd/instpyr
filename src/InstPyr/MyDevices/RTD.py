from ..Interfaces.Common import interface,inf_enums
from scipy import interpolate
import numpy as np
class RTD:
    def __init__(self,interface:interface.interface,channel, units=inf_enums.TempUnits.CELSIUS):
        self.interface=interface
        self.calX=[]
        self.calY=[]
        self.calfunc=None
        self.currentTemp=0
        self.channel=channel


    def readTemperature(self):
        self.currentTemp=self.interface.readTemperature(self.channel)
        if self.calfunc is not None:
            self.currentTemp=self._applyCalibration(self.currentTemp)
        return self.currentTemp


    def _applyCalibration(self,rawTemp):
        if self.calfunc is not None:
            return float(self.calfunc(rawTemp))

    def calibrate(self,Xin,Yin):
        self.calX=Xin
        self.calY=Yin
        self.calfunc=interpolate.interp1d(self.calX,self.calY)

    def config(self,type):
        pass

    def calcTemp(self):
        pass