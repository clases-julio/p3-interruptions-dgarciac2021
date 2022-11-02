#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

pulsadorGPIO = 16

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pulsadorGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        state = GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING, bouncetime=50, timeout=100)
        # bouncetime and timeout are both parameters of wait_for_edge.
        #
        # bouncetime means the time which the state of the channel should not change
        # to consider it as a valid change.
        #
        # timeout is the time which the program will wait for the input. If not detected, 
        # the program will continue.

        if state is not None: print("El boton se ha pulsado")

        # 'None' is the data type that wait_for_edge returns when a timeout is stablished and no
        # change in the channel is detected.

        else: time.sleep(0.1)
