#TODO this class should house any typedefs relevant to the interface class
class interface():
    """This class is the base class for interface objects such as Arduino and rigol power supply"""
    def __init__(self, port, readenable=False):
        pass

    def initializeIO(self, din=[], dout=[], ain=[],
                     aout=[]):
        """pass pins that have corresponding modes"""
        return self.not_implemented()

    def write_digital(self, pin, state, voltage):
        return self.not_implemented()

    def read_digital(self, pin):
        return self.not_implemented()

    def read_analog(self, pin):
        return self.not_implemented()

    def write_analog(self, pin, pwmvalue):
        return self.not_implemented()

    def configThermocouple(self,channel,type):
        return self.not_implemented()

    def readTemperature(self,channel,units):
        return self.not_implemented()

    def not_implemented(self):
        print('not implemented')
        return None

