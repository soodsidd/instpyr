from MyDevices import switch
from Interfaces.Arduino import  myarduino

import time

def main():
    arduino= myarduino.myarduino('COM3')
    led= switch.switch(arduino, 3)
    while(True):
        time.sleep(1)
        led.setstate(not led.state)

if __name__=='__main__':
    main()
