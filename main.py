# Add your Python code here. E.g.
from microbit import *
from math import sin, pi
import neopixel

# --- CONFIG --- #
TPS = 20
secondsToDecay = 2

ticksLeft = 0
ticksMax = TPS * secondsToDecay

vibrationThreshold = 20

BASE_ORANGE = (90,30,0)   # Base color to be used
DIFF_ORANGE = (30,10,0)    # Darker Orange
COLOR_DIFF = tuple([(BASE_ORANGE[j]-DIFF_ORANGE[j]) for j in range(3)])

STRIP_SIZE = 10                             # Number of LEDs on strip
np = neopixel.NeoPixel(pin0, STRIP_SIZE)

tick=0
while True:
    soundLevel = microphone.sound_level()
    print(soundLevel)
    if soundLevel > vibrationThreshold:
        ticksLeft = ticksMax
    if ticksLeft > 0:
        for i in range(STRIP_SIZE):
            np[i] = tuple([round(BASE_ORANGE[j]-COLOR_DIFF[j]*sin(pi*(tick%360)/180+(tick%360)*pi/18)) for j in range(3)])
        tick+=1; ticksLeft -= 1; np.show()
        if ticksLeft == 0: np.clear()
        
    else: np.clear()
    sleep(1000//TPS)