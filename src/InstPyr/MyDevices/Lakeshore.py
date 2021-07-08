from lakeshore import temperature_controllers

import serial

class Lakeshore218_probe:
    def __init__(self,comport, channel):
        self.channel=channel
        try:
            self.dev_conn=serial.Serial(port=comport,
                                        baudrate=9600,
                                        xonxoff=False,
                                        parity=serial.PARITY_ODD,
                                        bytesize=serial.SEVENBITS,
                                        stopbits=serial.STOPBITS_ONE,
                                        timeout=2.0,
                                        rtscts=False)
        except Exception:
            print('Could not connect to lakeshore')
            self.dev_conn=None

        print(self._query('*IDN?'))
        self.currentTemp=self.readTemperature()

    def _query(self,command):
        self.dev_conn.write(command.encode('ascii')+b'\n')
        return self.dev_conn.readline().decode('ascii')

    def readTemperature(self):
        self.currentTemp=float(self._query('CRDG? {}'.format(self.channel)))
        return self.currentTemp

    def close(self):
        self.dev_conn.close()

if __name__=='__main__':
    probe=Lakeshore218_probe('COM8',1)
    print(probe.readTemperature())

