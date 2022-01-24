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
    def movingaverage(cls,data,N=0):
        #sampling rate in seconds
        if N==0 or N>len(data):
            return np.average(data)
        else:
            return np.average(data[len(data)-N:len(data)-1])

    # @classmethod
    # # def rampfilter(cls,data,rate):



