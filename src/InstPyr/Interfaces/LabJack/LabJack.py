import u6
from InstPyr.Interfaces.Common import interface,inf_enums

class MyU6(interface.interface):
    def __init__(self):
        super().__init__(self)

        self.inst=u6.U6()
        self.inst.getCalibrationData()

        #all digital lines configured as outputs by default
        self.inst.getFeedback(u6.PortDirWrite(Direction=[0, 0, 0]))

    def getAIN(self,channel, differential=False,gainIndex=1,settlingFactor=6):
        if self.inst is not None:
            return self.inst.getAIN(channel,differential=False,gainIndex=0,settlingFactor=6)

    def setDO(self,channel, val):
        if val==0 or val==1:
            self.inst.getFeedback(u6.BitStateWrite(IONumber=channel, State=val))

    def setup_pwm(self,channel, frequency=5000):

        # Timer Configuration for PWM16 mode (TimerMode=0)
        self.inst.configIO(NumberTimersEnabled=channel + 1)
        self.inst.getFeedback(u6.Timer0Config(TimerMode=0, Value=32768))

        # Set frequency
        self.inst.getFeedback(u6.Timer0(0, 65536 - int(4E6 / frequency), 32768))

    def set_pwm(self,value, channel):
        # Clamp value to [0, 1]
        value = max(0, min(1, value))


        # Map value to a 16-bit timer value
        timer_value = int(65535 * value)

        # Set PWM duty cycle based on the channel
        if channel == 0:
            self.inst.getFeedback(u6.Timer0(0, Value=timer_value))
        elif channel == 1:
            self.inst.getFeedback(u6.Timer1(0, Value=timer_value))
        # Add more elif clauses if you have more channels
        else:
            print(f"Invalid channel number {channel}")

    def set_dac_output(self, dac_channel, value):
        # Clamp value to [0, 1]
        value = max(0, min(1, value))

        # Map value to voltage level between 0 and 5V
        voltage = value * 5

        print(voltage)
        # Set the voltage on the DAC channel
        if dac_channel == 0:
            self.inst.getFeedback(u6.DAC0_8(Value=int((voltage / 5) * 255)))
        elif dac_channel == 1:
            self.inst.getFeedback(u6.DAC1_8(Value=int((voltage / 5) * 255)))
        else:
            print(f"Invalid DAC channel {dac_channel}. Only 0 and 1 are supported.")

    def close(self):
        if self.inst is not None:
            self.inst.close()
            self.inst=None

if __name__=='__main__':
    inst=MyU6()
    scalefactor=100
    print(inst.getAIN(0)*scalefactor)
    inst.close()
