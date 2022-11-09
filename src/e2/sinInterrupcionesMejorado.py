#!/usr/bin/env python3

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

    # Scalable code. With those loops we assign the same behavior to all the components in the same line.

    while True:
        for button in buttons:
             index = buttons.index(button)
             led = leds[index]
             # both lists follow concordance between the led and the button that controls it.
             # so the index of the button in the buttons list is the same index of the led.
             driveLed(led, not checkButton(button)) # Inverted Logic

