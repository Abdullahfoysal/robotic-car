from MotorModule import Motor
from time import sleep

import KeyPressModule as kp
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

motor= Motor(15,11,13,33,35,37)
kp.init()
ls=70
rs=70
def main():
    if kp.getKey('UP'):
        #motor.move(0.5,0,0.1)
        motor.motorMove(ls,rs);
    elif kp.getKey('DOWN'):
        #motor.move(-0.5,0,0.1)
        motor.motorMove(-ls,-rs)
    elif kp.getKey('LEFT'):
        #motor.move(0.5,0.3,0.1)
        motor.motorMove(-ls,rs)
    elif kp.getKey('RIGHT'):
        #motor.move(0.5,-0.3,0.1)
        motor.motorMove(ls,-rs)
    else:
        #motor.stop(0.1)
        motor.motorMove(0,0)
 
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
