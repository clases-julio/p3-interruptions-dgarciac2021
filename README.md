# P2-gpio-ledrgb

This exercise consists on drive two [LED's](https://github.com/clases-julio/p1-introrpi-pwm-dgarciac2021/wiki/LED) through [GPIO](https://github.com/clases-julio/p1-introrpi-pwm-dgarciac2021/wiki/GPIO) available on the [Raspberry Pi 3B+](https://github.com/clases-julio/p1-introrpi-pwm-dgarciac2021/wiki/Raspberry-Pi#raspberry-pi-3b) and the help of two buttons. You might want to take a look on the wiki, since there is info of everything involved on this project. From the [button](https://github.com/clases-julio/p3-interruptions-dgarciac2021/wiki/Button) to the [interruption procedure](https://github.com/clases-julio/p3-interruptions-dgarciac2021/wiki/Interruption).

## Circuit Assembly

This time the assembly gets a little bit more complex. We are using two buttons, two LED's and two 220Ω[^1] resistors.

This is an schematic made with [Fritzing](https://fritzing.org/):

![Schematic](./doc/img/schematic.png)

And this is the real circuit!

## Code

We would like to highlight some remarkable aspects from our code.

In [e1](./src/e1/interrupcionEdgeBueno.py), we found that there is more parameters for `GPIO.wait_for_edge` that we saw in the exercise guide. More on them [here](https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/). More precisely, we focused on `timeout`, which is a parameter that sets the time which the `GPIO.wait_for_edge` *will actually wait for that edge*. If that time expires, a `None` is returned, whereas an edge is detected on time, any number is returned. 

```python
state = GPIO.wait_for_edge(pulsadorGPIO, GPIO.RISING, bouncetime=50, timeout=100)
if state is not None: print("El boton se ha pulsado")
```

This turned out to be very handy to solve a lot of problems with our code.

## Circuit testing

This is the result! Pretty nice, isn't it?

[^1]: As we saw in previous exercises, this resistor value might be too high for the 3V3 that the RPI GPIO provides. The only issue is that the LED's will be dimmer.
