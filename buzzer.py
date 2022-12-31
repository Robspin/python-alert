import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)
buzzer = 26
io.setup(buzzer, io.OUT)
tone1 = GPIO.PWM(buzzer, 100)
tone1.start(50)

c = [32, 65, 131, 262, 523]
db= [34, 69, 139, 277, 554]
d = [36, 73, 147, 294, 587]
eb= [37, 78, 156, 311, 622]
e = [41, 82, 165, 330, 659]
f = [43, 87, 175, 349, 698]
gb= [46, 92, 185, 370, 740]
g = [49, 98, 196, 392, 784]
ab= [52, 104, 208, 415, 831]
a = [55, 110, 220, 440, 880]
bb= [58, 117, 223, 466, 932]
b = [61, 123, 246, 492, 984]

cmajor = [c, d, e, f, g, a, b]
aminor = [a, b, c, d, e, f, g]


def playScale(scale, pause):
    '''
    scale: scale name to be played
    pause: pause between each notes played

    This function plays the given scale in every available octave
    I used this to test what was audible on the buzzer
    '''
    for i in range(0, 5):
        for note in scale:
            tone1.ChangeFrequency(note[i])
            sleep(pause)
    tone1.stop()

starwars_notes = [c[1], g[1], f[1], e[1], d[1], c[2], g[1], f[1], e[1], d[1], c[2], g[1],
              f[1], e[1], f[1], d[1]]
starwars_beats = [4,4,1,1,1,4,4,1,1,1,4,4,1,1,1,4]


def playSong(songnotes, songbeats, tempo):
    '''
    songnotes: list of the melodies notes
    songbeats: list of melodies beat times
    tempo: speed of song, this is not traditional tempo in bpm like on a metronome,
        but more like a multiplier for whatever the notes are so a tempo value of 2
        make it play twice as fast. Adjust this by ear.

    This function plays the melody, simply by iterating through the list.
    '''
    tone1.ChangeDutyCycle(50)
    for i in range(0, len(songnotes)):
        tone1.ChangeFrequency(songnotes[i])
        time.sleep(songbeats[i] * tempo)
    tone1.ChangeDutyCycle(0)


# play two songs
playSong(starwars_notes, starwars_beats, 0.2)

# while True:
#     io.output(buzzer, io.HIGH)
#     print("Beep")
#     sleep(0.5)
#     io.output(buzzer, io.LOW)
#     print("No Beep")
#     sleep(0.5)
