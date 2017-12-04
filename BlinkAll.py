import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BCM);
    GPIO.setup(17,GPIO.OUT);
    GPIO.setup(27,GPIO.OUT);
    GPIO.setup(22,GPIO.OUT);
    GPIO.setup(23,GPIO.OUT);

def turnOn1():
    init();
    GPIO.output(17,False);

def turnOn2():
    init();
    GPIO.output(27,False);

def turnOn3():
    init();
    GPIO.output(22,False);

def turnOn4():
    init();
    GPIO.output(23,False);

def turnOffAll():
    init();
    GPIO.output(17,True);
    GPIO.output(27,True);
    GPIO.output(22,True);
    GPIO.output(23,True);
    GPIO.cleanup();

a = 1
while a < 20:
    turnOn1()
    time.sleep(.2)

    turnOn2()
    time.sleep(.2)

    turnOn3()
    time.sleep(.2)

    turnOn4()
    time.sleep(.2)

    turnOffAll()
    time.sleep(.2)
    
    a += 1;
