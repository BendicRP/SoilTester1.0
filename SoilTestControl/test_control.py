import PiMotor
import time
import RPi.GPIO as GPIO


GPIO.setwarnings(False)

TRIG = 29
ECHO = 31

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

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
    motorAll.forward(100)
    time.sleep(2)

def back():
    print("Robot Moving Backward ")
    motorAll.reverse(100)
    time.sleep(2)

def left():
    print("Robot Moving Left ")
    m1.forward(100)
    m2.stop()
    time.sleep(2)

def right():
    print("Robot Moving Right ")
    m1.stop()
    m2.forward(100)
    time.sleep(2)
    
stop()
forward()
right()
left() 
back()