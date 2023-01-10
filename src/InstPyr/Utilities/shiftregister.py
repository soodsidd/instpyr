import collections
import numpy as np

class shiftregister:
    def __init__(self,size,initval=0):
        self.size=size
        self.buffer = collections.deque(maxlen=size)
        #initialize buffer
        for i in range(size):
            self.buffer.append(initval)

    def push(self,val):
        self.buffer.append(val)

    def pop(self):
        a=self.buffer.pop()
        self.buffer.insert(0,0)
        return a

    def showlast(self,number):
        #show last N entries
        return list(self.buffer)[self.size-number:self.size]

    def data(self):
        return list(self.buffer)

    def allequal(self):
        data=np.array(list(self.buffer))
        return np.all(data==data[0])

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = int(val)
        self.buffer = collections.deque(maxlen=int(val))
        for i in range(int(val)):
            self.buffer.append(0)

    def __str__(self):
        return str(list(self.buffer))



if __name__=="__main__":
    a=shiftregister(10)

    for i in range(10):
        a.push(i)
        print(a)

    for i in range(10):
        a.pop()
        print(a)