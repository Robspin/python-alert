import RPi.GPIO as io
from time import sleep

# length = 6

io.setwarnings(False)
# io.setmode(io.BCM)
buzzer = 26
io.setup(buzzer, io.OUT)
# tone1 = io.PWM(buzzer, 100)
# tone1.start(50)
io.setmode(io.BOARD)
io.setup(buzzer, io.OUT)
pin7 = io.PWM(buzzer, 100)
pin7.start(50)

# i = 0
# while i < length:
#     io.output(buzzer, io.HIGH)
#     sleep(0.5)
#     io.output(buzzer, io.LOW)
#     sleep(0.5)
#     i += 1

while True:
  io.output(7, io.HIGH)
  pin7.ChangeFrequency(16.35) # C0
  sleep(1)
  pin7.ChangeFrequency(261.63) # C4
  sleep(1)
  pin7.ChangeFrequency(293.66) # D4
  sleep(1)
  pin7.ChangeFrequency(329.63) # E4
  sleep(1)
  pin7.ChangeFrequency(349.23) # F4
  sleep(1)
  pin7.ChangeFrequency(392.00) # G4
  sleep(1)
  pin7.ChangeFrequency(440.00) # A4
  sleep(1)
  pin7.ChangeFrequency(493.88) # B4
  sleep(1)
  pin7.ChangeFrequency(523.25) # A5
  sleep(1.5)
  pin7.ChangeFrequency(16.35) # C0
  sleep(1)
  io.output(7, io.LOW)
  sleep(1)