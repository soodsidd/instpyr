from InstPyr.Interfaces.Common import interface,inf_enums
from scipy import interpolate
import numpy as np
import math
class Thermistor:
    def __init__(self,interface:interface.interface,channel,interfacescale=1.0,divideresistance=9150,Bconstant=3380, REFTEMP=25,REFRES=10000, units=inf_enums.TempUnits.CELSIUS):
        self.interface=interface
        self.calX=[]
        self.calY=[]
        self.calfunc=None
        self.currentTemp=0
        self.channel=channel
        self.divideresistance=divideresistance
        self.Bconstant=Bconstant
        self.reftemp=REFTEMP+273.15
        self.refres=10000
        self.interface_scalefactor=interfacescale


    def _voltage_to_resistance(self,voltage):
        Vin=5.0
        R1=self.divideresistance
        R2 = R1 * (voltage) / (Vin-voltage)  # Thermistor resistance
        # print(R2)
        return R2

    def _resistance_to_temperature(self,resistance):
        # Calculate the temperature using the Beta Parameter equation
        # T = 1 / ( (1/T0) + (1/B) * ln(R/R0) ) - 273.15
        # Where, T is the temperature in Celsius
        T0=self.reftemp
        R0=self.refres
        B=self.Bconstant
        # T = 1.0 / ((1.0 / T0) + (1.0 / B) * math.log(resistance / R0)) - 273.15
        # print(resistance)
        try:
            T=B*T0/(B-T0*math.log(R0/resistance))-273.15
        except Exception as e:
            T=0
        # print(T)
        return T


    def readTemperature(self):
        self.currentTemp=self.interface.getAIN(self.channel)*self.interface_scalefactor
        self.currentTemp=self._voltage_to_resistance(self.currentTemp)
        self.currentTemp=self._resistance_to_temperature(self.currentTemp)

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