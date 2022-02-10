from src.InstPyr.Interfaces.Rigol.Rigol832 import Rigol832

r=Rigol832(deviceId='DP8C224905668')
r.setDigitalVoltage(1,10)