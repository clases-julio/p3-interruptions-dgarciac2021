#!/usr/bin/env python3

import signal
import time
import RPi.GPIO as GPIO

button1 = 16
button2 = 20

led1 = 27
led2 = 17

def driveLed(led, state):
    GPIO.output(led, state)
    return None

def checkButton(button):
    return GPIO.input(button)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    buttons = [button1, button2]
    leds = [led1, led2]

    for button in buttons:
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    for led in leds:
        GPIO.setup(led, GPIO.OUT)

    while True:
        # bouncetime and timeout are both parameters of wait_for_edge.
        #
        # bouncetime means the time which the state of the channel should not change
        # to consider it as a valid change.
        #
        # timeout is the time which the program will wait for the input. If not detected, 
        # the program will continue.
        for button in buttons:
             index = buttons.index(button)
             led = leds[index]
             driveLed(led, not checkButton(button))

        # 'None' is the data type that wait_for_edge returns when a timeout is stablished and no
        # change in the channel is detected.
