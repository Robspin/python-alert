import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)
buzzer = 23
io.setup(buzzer, io.OUT)

while True:
    io.output(buzzer, io.HIGH)
    print("Beep")
    sleep(0.5)
    io.output(buzzer, io.LOW)
    print("No Beep")
    sleep(0.5)
