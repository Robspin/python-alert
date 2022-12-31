import RPi.GPIO as io
from time import sleep

length = 6

io.setwarnings(False)
io.setmode(io.BCM)
buzzer = 26
io.setup(buzzer, io.OUT)
tone1 = io.PWM(buzzer, 100)
tone1.start(50)

i = 0
while i < length:
    io.output(buzzer, io.HIGH)
    sleep(0.5)
    io.output(buzzer, io.LOW)
    sleep(0.5)
    i += 1
