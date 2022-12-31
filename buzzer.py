import RPi.GPIO as io
from time import sleep


def sound_the_alarm(times):
    io.setwarnings(False)
    io.setmode(io.BCM)
    buzzer = 26
    io.setup(buzzer, io.OUT)
    audio_pin = io.PWM(buzzer, 100)
    audio_pin.start(50)
    i = 0

    while i < times:
        io.output(buzzer, io.HIGH)
        # audio_pin.ChangeFrequency(16.35) # C0
        # sleep(0.25)
        # audio_pin.ChangeFrequency(261.63) # C4
        # sleep(0.25)
        # audio_pin.ChangeFrequency(293.66) # D4
        # sleep(0.25)
        # audio_pin.ChangeFrequency(329.63) # E4
        # sleep(0.25)
        audio_pin.ChangeFrequency(349.23) # F4
        sleep(0.25)
        audio_pin.ChangeFrequency(392.00) # G4
        sleep(0.25)
        audio_pin.ChangeFrequency(440.00) # A4
        sleep(0.25)
        audio_pin.ChangeFrequency(493.88) # B4
        sleep(0.25)
        # audio_pin.ChangeFrequency(523.25) # A5
        # sleep(0.33)
        # audio_pin.ChangeFrequency(16.35) # C0
        # sleep(0.25)
        io.output(buzzer, io.LOW)
        sleep(0.25)
        i += 1

    io.cleanup()
