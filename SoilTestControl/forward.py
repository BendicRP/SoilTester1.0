import PiMotor
import time
import RPi.GPIO as GPIO

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2)


def stop():
    print("Robot Stop ")
    motorAll.stop()
    time.sleep(2)

def forward():
    print("Robot Moving Forward ")
    motorAll.forward(25)
    time.sleep(2)
    
forward()