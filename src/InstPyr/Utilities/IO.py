import serial.tools.list_ports

class IO:
    def __init__(self):
        pass

    @classmethod
    def findCOMports(cls, name:str):
        ports=list(serial.tools.list_ports.comports())
        print('FOUND: '+str(ports))
        for p in ports:
            if p[1].find(name)!=-1:
                return p[0]

        return -1


if __name__=='__main__':
    IO.findCOMports('')