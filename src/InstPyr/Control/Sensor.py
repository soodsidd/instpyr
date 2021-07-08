import collections

class MySensor:
    def __init__(self,sensor,callfunc,name,buffer=10):
        self.sensor=sensor
        self.callfunc=callfunc
        self.name=name
        self.buffer=collections.deque(maxlen=buffer)
        for i in range(buffer):
            self.buffer.append(0)

    def read(self):
        val=self.callfunc(self.sensor)
        self.buffer.append(val)
        return val





if __name__=='__main__':
    class person:
        def __init__(self):
            self.name='sid'

        def readname(self):
            return self.name

    a=MySensor(person(),person.readname,'this')
    print(a.read())

