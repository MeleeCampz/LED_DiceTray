import board
import neopixel
import digitalio
import rotaryio
import Helpers

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.color import PURPLE, AMBER, JADE
from adafruit_led_animation.sequence import AnimationSequence

import adafruit_debouncer

class Hardware:
    default_brightness= 0.1
    max_brightness = 0.5
    steps_brightness = 25
    
    def __init__(self):
        #Neopixels
        self.current_brightness = Hardware.default_brightness
        self.neopixels = neopixel.NeoPixel(board.GP15, 24, brightness=self.current_brightness)
        #Rotary Encoder
        self.encoder = rotaryio.IncrementalEncoder(board.GP5, board.GP6, 20)
        #Mode Switch Button
        modeButtonPin = digitalio.DigitalInOut(board.GP11)
        modeButtonPin.direction = digitalio.Direction.INPUT
        modeButtonPin.pull = digitalio.Pull.UP
        #Add debouncer to button
        self.modeButton = adafruit_debouncer.Debouncer(modeButtonPin)

        self.last_Position = 0
        self.last_modeButton_State = False

        comet = Comet(self.pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
        blink = Blink(self.pixels, speed=0.5, color=JADE)
        chase = Chase(self.pixels, speed=0.1, size=3, spacing=6, color=AMBER)
        self.animSequence = AnimationSequence(comet, blink, chase)

    def CheckButtonPress(self):
         return self.modeButton.fell

    def UpdateButton(self):
        self.modeButton.update()

    def UpdateRotaryEncoder(self):
        newPos = self.encoder.position
        delta = self.last_Position - newPos
        self.last_Position = newPos
        return delta
    
    def UpdateBrightness(self, steps):
        self.current_brightness += Helpers.Clamp01(steps / self.steps_brightness) 
        self.neneopixels.brightness = self.current_brightness * self.max_brightness

    def DisplayProgress(self, progress):
        self.neopixels.fill(0)
        fillIndex = Helpers.Clamp01(progress) * (self.neopixels.n)
        for i in range(fillIndex):
            lerp = i / self.neopixels.n
            self.neopixels[i] = [Helpers.Lerp(255,0,lerp), Helpers.Lerp(0, 255, lerp), 0]
        self.neopixels.show()

    def DisplayCurrentAnimation(self):
        self.animSequence.animate()

    def DisplayNextAnimation(self):
        self.animSequence.next()

    def DisplayPreviousAnimation(self):
        self.animSequence.previous()