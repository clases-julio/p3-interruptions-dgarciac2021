#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO

button1 = 16
button2 = 20

led1 = 27
led2 = 17

def callbackExit(signal, frame): # señal y estado cuando se produjo la interrup.
    GPIO.cleanup() # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def callbackButton(button):
    index = buttons.index(button)
    led = leds[index]
    GPIO.output(led, not GPIO.input(led))

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    buttons = [button1, button2]
    leds = [led1, led2]

    for button in buttons:
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for led in leds:
        GPIO.setup(led, GPIO.OUT)

    for button in buttons:
        GPIO.add_event_detect(button, GPIO.BOTH, callback=callbackButton, bouncetime=100)

    signal.signal(signal.SIGINT, callbackExit) # callback para CTRL+C
    signal.pause() # esperamos por hilo/callback CTRL+C antes de acabar

