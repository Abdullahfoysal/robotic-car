from MotorModule import Motor
from time import sleep

import KeyPressModule as kp
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

motor= Motor(12,8,10,33,35,37)
kp.init()

def main():
    if kp.getKey('UP'):
        motor.move(0.5,0,0.1)
    elif kp.getKey('DOWN'):
        motor.move(-0.5,0,0.1)
    elif kp.getKey('LEFT'):
        motor.move(0.5,0.3,0.1)
    elif kp.getKey('RIGHT'):
        motor.move(0.5,-0.3,0.1)
    else:
        motor.stop(0.1)
 
if __name__ == '__main__':
    while True:
        main()
        #try:
        #    main()
        #except KeyboardInterrupt:
        #    print("Keyboard Interrupt occured")
        #except:
        #    print("Other exception occured")
        #finally:
        #    GPIO.cleanup()
        #    print("clean exit")*/
