import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

TRIG = 29
ECHO = 31

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

count=0
while True:
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
        print("Stop")
        time.sleep(1)
        print("Back")
        time.sleep(2)
        if (count%4 ==1):
            print("right")

        else:
            print("Forward")
