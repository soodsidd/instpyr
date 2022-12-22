import pymodbus
from pymodbus.client import ModbusTcpClient
import struct
import bitstring
CURRENT_TEMP_ADDR=360
CURRENT_SETPOINT_ADDR=2160
COOLPOWER=1906
HEATPOWER=1904
SETPOINTLIMITS=(-20,70)


class WatlowPM_TCP():
    def __init__(self, IPaddr='172.20.20.20'):
        self.client=ModbusTcpClient(IPaddr)

    def connect(self):
        if self.client is not None:
            self.client.connect()

    def readCurrentTemperature(self):
        bits=self._readLoHiRegisters(CURRENT_TEMP_ADDR)
        return self._convertToFloat(bits)

    def readCurrentSetpoint(self):
        bits = self._readLoHiRegisters(CURRENT_SETPOINT_ADDR)
        return self._convertToFloat(bits)

    def readCurrentCoolingPower(self):
        bits = self._readLoHiRegisters(COOLPOWER)
        return self._convertToFloat(bits)

    def readCurrentHeatingPower(self):
        bits = self._readLoHiRegisters(HEATPOWER)
        return self._convertToFloat(bits)

    def _readLoHiRegisters(self,addr):
        result = self.client.read_input_registers(addr, 2)
        bits = (result.registers[1] << 16) + result.registers[0]
        return bits

    def writeSetpoint(self,setpoint):
        if setpoint>=SETPOINTLIMITS[0] and setpoint<=SETPOINTLIMITS[1]:
            res=self._convertToBits(setpoint)
            hi=int(res[0:16].bin.encode('ascii'),2)
            lo=int(res[16:].bin.encode('ascii'),2)
            self.client.write_registers(CURRENT_SETPOINT_ADDR,[lo,hi])


    def _convertToFloat(self,bits):
        s = struct.pack('>L', bits)
        final = struct.unpack('>f', s)[0]
        return final

    def _convertToBits(self,num):
        f1=bitstring.BitArray(float=num,length=32)
        return f1

    def close(self):
        self.client.close()


if __name__=='__main__':
    Watlowinst=WatlowPM_TCP()
    Watlowinst.connect()
    Watlowinst.writeSetpoint(20)
    print(Watlowinst.readCurrentTemperature())
    print(Watlowinst.readCurrentSetpoint())
    print(Watlowinst.readCurrentCoolingPower())
    print(Watlowinst.readCurrentHeatingPower())


    Watlowinst.close()

