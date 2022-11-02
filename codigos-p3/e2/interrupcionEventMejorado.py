#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO

button1 = 16
button2 = 20

led1 = 17
led2 = 27

def callbackExit(signal, frame): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup() # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def callbackButton1(channel):
    GPIO.output(led1, not GPIO.input(led1))

def callbackButton2(channel):
    GPIO.output(led2, not GPIO.input(led2))

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)

    GPIO.add_event_detect(button1, GPIO.BOTH, callback=callbackButton1, bouncetime=100)
    GPIO.add_event_detect(button2, GPIO.BOTH, callback=callbackButton2, bouncetime=100)
    
    signal.signal(signal.SIGINT, callbackExit) # callback para CTRL+C
    signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar

