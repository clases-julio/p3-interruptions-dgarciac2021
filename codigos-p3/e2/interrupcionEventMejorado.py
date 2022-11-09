#!/usr/bin/env python3

import signal
import sys
import RPi.GPIO as GPIO

button1 = 16
button2 = 20

led1 = 27
led2 = 17

def callbackExit(signal, frame): # signal and frame when the interrupt was executed.
    GPIO.cleanup() # Clean GPIO resources before exit.
    sys.exit(0)

def callbackButton(button):
    # button is actually the channel of the interrupt procedure. Thus equals to
    # the GPIO number of the channel where the interrupt was detected.
    index = buttons.index(button)
    led = leds[index]
    # both lists follow concordance between the led and the button that controls it.
    # so the index of the button in the buttons list is the same index of the led.
    GPIO.output(led, not GPIO.input(led)) # write the opposite to the current state

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
    
    # Scalable code. With those loops we assign the same behavior to all the components in the same line.

    signal.signal(signal.SIGINT, callbackExit) # callback for CTRL+C
    signal.pause() # wait for thread/callback CTRL+C before exit

