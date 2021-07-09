import collections

class watch:
    #use this class to define a 'watch' variable- that you will log and plot
    def __init__(self,name, variable=None,object=None, callfunc=None, buffer=10):
        self.object = object
        self.variable=variable
        self.callfunc = callfunc
        self.name = name
        self.buffer = collections.deque(maxlen=buffer)
        for i in range(buffer):
            self.buffer.append(0)
    #
    # @property
    # def buffer(self):
    #     return list(self.buffer)
    #
    # @buffer.setter
    # def buffer(self,buff):
    #     self.buffer=buff



    def read(self):
        val = self.callfunc(self.object)
        self.buffer.append(val)
        return val

if __name__ == '__main__':
    class person:
        def __init__(self):
            self.name = 'sid'

        def readname(self,last):
            return self.name+last
    obj=person()
    a = watch(obj, lambda x: x.readname('sood'), 'this')
    print(a.read())
