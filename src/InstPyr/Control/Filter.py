import scipy.signal as signal
import numpy as np
from ..Utilities.shiftregister import shiftregister
import time
from dataclasses import dataclass

@dataclass
class FilterTypes:
    LOWPASS='lowpass'
    HIGHPASS='highpass'
    MOVINGAVERAGE='movavg'

class MyFilter:
    def __init__(self, buffersize=10,type=FilterTypes.LOWPASS,cutoff=0.1,samplingrate=1,order=3):
        self.lowpassfilt=None
        self.buffersize=buffersize
        self.filtertype = type
        if self.filtertype==FilterTypes.LOWPASS or FilterTypes.HIGHPASS:
            self.buffer=shiftregister(int(samplingrate/cutoff)*2)

        self.cutoff=cutoff
        self.samplingrate=samplingrate
        self.order=order
        self.sos=None

    def nextVal(self,data):
        self.buffer.push(data)
        if self.filtertype==FilterTypes.LOWPASS:
            if self.sos is None:
                self.sos = signal.butter(self.order, self.cutoff, btype='lowpass', output='sos', fs=self.samplingrate)
            y=signal.sosfilt(self.sos,self.buffer.data())
            return y[-1]
        elif self.filtertype==FilterTypes.HIGHPASS:
            if self.sos is None:
                self.sos = signal.butter(self.order, self.cutoff,btype='highpass', output='sos', fs=self.samplingrate)
            y=signal.sosfilt(self.sos,self.buffer.data())
            return y[-1]
        elif self.filtertype==FilterTypes.MOVINGAVERAGE:
            return np.average(self.buffer.data())

class RateLimiter(MyFilter):
    def __init__(self,ratelimit):
        super().__init__()
        self.output=0
        self.rate=ratelimit
        self.maxrate=ratelimit
        self.currentTime=time.time()
        self.registersize=10
        self.buffer=shiftregister(self.registersize)

    def nextVal(self,data):
        self.buffer.push(data)
        self.newtime=time.time()
        elapsedtime=self.newtime-self.currentTime
        #read last two values:
        list=self.buffer.showlast(2)
        if elapsedtime!=0:
            rate=(list[1]-self.output)/elapsedtime
        else:
            rate=0

        if abs(rate)<self.maxrate:
            self.rate=rate
        else:
            self.rate=np.sign(rate)*self.maxrate

        self.currentTime=self.newtime
        self.output=self.output+self.rate*elapsedtime
        return self.output



    def reset(self):
        self.output=0
        self.buffer=shiftregister(self.registersize)




