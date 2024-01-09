import collections
import _ctypes

class watch:
    instances=[]
    #use this class to define a 'watch' variable- that you will log and plot
    def __init__(self,context,name,variableName=None,callfunc=None, object=None,buffer=10,precision=2,plot=0):
        self.object = object
        self.variableName=variableName
        self.callfunc = callfunc
        self.context=context
        self.name = name
        self.precision=precision
        self.buffersize=buffer
        self.plot=plot
        self.buffer = collections.deque(maxlen=buffer)
        for i in range(buffer):
            self.buffer.append(0)
        self.val=self.read()
        watch.instances.append(self)
    # @property
    # def buffer(self):
    #     return list(self.buffer)
    #
    # @buffer.setter
    # def buffer(self,buff):
    #     self.buffer=buff

    @property
    def buffersize(self):
        return self._buffersize

    @buffersize.setter
    def buffersize(self,val):
        self._buffersize=int(val)
        self.buffer=collections.deque(maxlen=int(val))
        for i in range(int(val)):
            self.buffer.append(0)


    def read(self):
        if self.variableName is not None:
            val=getattr(self.context,self.variableName,None)
        else:
            val = self.callfunc(self.object)
        self.buffer.append(val)
        self.val=val
        return val

    @classmethod
    def get_all_instances(cls):
        return cls.instances

    @classmethod
    def remove_instance(cls, variableName):
        # Remove dead references and the instance with the specified variable name
        cls.instances = [ref for ref in cls.instances if ref() is not None and ref().variableName != variableName]


if __name__ == '__main__':
    class person:
        def __init__(self):
            self.name = 'sid'

        def readname(self,last):
            return self.name+last
    obj=person()
    a = watch(obj, lambda x: x.readname('sood'), 'this')
    print(a.read())