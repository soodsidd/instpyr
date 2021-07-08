import scipy.signal as signal
import numpy as np
class MyFilter:
    def __init__(self):
        self.lowpassfilt=None

    @classmethod
    def lowpass(cls,data,cutoff, sampling):
        # if self.lowpassfilt==None:
        # b, a = signal.butter(10,cutoff,fs=sampling)
        b,a=signal.butter(10,cutoff,fs=sampling)
        # print(data)
        # print(b)
        # print(a)
        y=signal.filtfilt(b,a,data)
        # print(y)
        yout=y[len(y)-1]
        # # print(b)
        # newval=signal.filtfilt(b,a,data,padlen=0)
        # print(newval)
        # return newval[len(newval)-1]
        #TODO figure out how lowpass filtering works
        return yout

    @classmethod
    def movingaverage(cls,data,pts=0):
        if pts==0:
            return np.average(data)
        else:
            return np.average(data[len(data)-pts:len(data)-1])




