import PiMotor
import time
import RPi.GPIO as GPIO

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2)

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

TRIG = 29
ECHO = 31

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

servoPIN = 2
#GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization


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
<<<<<<< HEAD
    #m1.reverse(100)
    #m2.reverse(100)
    motorAll.reverse(100)
=======
    m1.reverse(100)
    m2.reverse(100)
    #motorAll.reverse(25)
    #m1.forward(25)
    #m2.forward(25)
>>>>>>> 7e62cbf7f9a4cfbf56922aa5a4d39c0e1f723b3f
    time.sleep(2)

def left():
    print("Robot Moving Left ")
    m1.stop()
    m2.forward(100)
    time.sleep(2)

def right():
    print("Robot Moving Right ")
    m1.forward(100)
    m2.stop()
    time.sleep(2)
    
count=0

try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    i=0
    avgDistance=0
    for i in range(5):
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start

        distance = (pulse_duration * 34300)/2
        distance = round(distance,2)
        avgDistance=avgDistance+distance

        avgDistance=avgDistance/5
        print(avgDistance)

    if avgDistance < 20:
        count=count+1
        stop()
        time.sleep(1)
        left()
        time.sleep(2)
        if (count%4 ==1):
            right()

        else:
            forward()
            
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()



