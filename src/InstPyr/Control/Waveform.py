import collections

class square:
    def __init__(self,sample:float,period:float,maxval=1,minval=0,duty=0.5 ):
        #initialize waveform here
        self.sample_num=(int)(period/sample)
        self.signal=[]
        self.midsample=duty*self.sample_num
        self.currentindex=0
        for i in range(self.sample_num):
            if i>self.midsample:
                self.signal+=[minval]
            else:
                self.signal+=[maxval]

    def nextval(self):
        out=self.signal[self.currentindex]
        self.currentindex+=1
        if self.currentindex>=self.sample_num:
            self.currentindex=0
        return out

    def __len__(self):
        return len(self.signal)

    def __str__(self):
        return str(self.signal)

if __name__=="__main__":
    squarewave=square(0.25,1)
    print(squarewave)
    a=len(squarewave)
    print(a)
    for i in range(3*a):
        print(i)
        print(squarewave.nextval())



