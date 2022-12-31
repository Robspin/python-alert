import time
import RPi.GPIO as io

LED_RED = 27
LED_BLUE = 22


def green_light():
    io.setmode(io.BCM)
    io.setup(LED_RED, io.OUT)
    io.setup(LED_BLUE, io.OUT)
    io.output(LED_RED, False)
    io.output(LED_BLUE, True)
    time.sleep(1)


def red_light():
    io.setmode(io.BCM)
    io.setup(LED_RED, io.OUT)
    io.setup(LED_BLUE, io.OUT)
    io.output(LED_BLUE, False)
    io.output(LED_RED, True)
    time.sleep(1)
    io.output(LED_RED, False)
    time.sleep(1)
