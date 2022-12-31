import RPi.GPIO as io
from time import sleep


io.setwarnings(False)
io.setmode(io.BCM)
buzzer = 26
io.setup(buzzer, io.OUT)
pin7 = io.PWM(buzzer, 100)
pin7.start(50)


def sound_the_alarm(times):
  i = 0
  while i < times - 1:
    io.output(buzzer, io.HIGH)
    pin7.ChangeFrequency(16.35) # C0
    sleep(0.25)
    pin7.ChangeFrequency(261.63) # C4
    sleep(0.25)
    pin7.ChangeFrequency(293.66) # D4
    sleep(0.25)
    pin7.ChangeFrequency(329.63) # E4
    sleep(0.25)
    pin7.ChangeFrequency(349.23) # F4
    sleep(0.25)
    pin7.ChangeFrequency(392.00) # G4
    sleep(0.25)
    pin7.ChangeFrequency(440.00) # A4
    sleep(0.25)
    pin7.ChangeFrequency(493.88) # B4
    sleep(0.25)
    pin7.ChangeFrequency(523.25) # A5
    sleep(0.33)
    pin7.ChangeFrequency(16.35) # C0
    sleep(0.25)
    io.output(buzzer, io.LOW)
    sleep(0.25)
    i += 1

sound_the_alarm(2)