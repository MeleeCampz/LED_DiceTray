import board
import neopixel
import digitalio
import rotaryio
import Helpers

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.color import PURPLE, AMBER, JADE
from adafruit_led_animation.sequence import AnimationSequence

import adafruit_debouncer

class Hardware:
    default_brightness= 0.1
    min_brightness = 0.01
    max_brightness = 0.5
    num_neopixels = 24
    
    def __init__(self):
        #Neopixels
        self.current_brightness = Hardware.default_brightness
        self.neopixels = neopixel.NeoPixel(board.D5, self.num_neopixels, brightness=self.current_brightness)
        #Rotary Encoder
        self.encoder = rotaryio.IncrementalEncoder(board.D13, board.D12, 4)
        #Mode Switch Button
        modeButtonPin = digitalio.DigitalInOut(board.D11)
        modeButtonPin.direction = digitalio.Direction.INPUT
        modeButtonPin.pull = digitalio.Pull.UP
        #Add debouncer to button
        self.modeButton = adafruit_debouncer.Debouncer(modeButtonPin)

        self.last_Position = 0
        self.last_modeButton_State = False

        comet = Comet(self.neopixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
        blink = Blink(self.neopixels, speed=0.5, color=JADE)
        chase = Chase(self.neopixels, speed=0.1, size=3, spacing=6, color=AMBER)
        rainbow = RainbowChase(self.neopixels, speed=0.1, size=3, spacing=2, step=12)
        self.animSequence = AnimationSequence(comet, blink, chase, rainbow)

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
        self.current_brightness = Helpers.Clamp01(self.current_brightness + steps / self.num_neopixels)
        self.neopixels.brightness = Helpers.Lerp(self.min_brightness, self.max_brightness, self.current_brightness)
        
    def ClearPixels(self):
        self.neopixels.fill(0)

    def DisplayProgress(self, progress):
        self.ClearPixels()
        fillIndex = 1+ Helpers.Clamp01(progress) * (self.neopixels.n-1)
        for i in range(fillIndex):
            lerp = i / self.neopixels.n
            self.neopixels[i] = [Helpers.Lerp(255,0,lerp), Helpers.Lerp(0, 255, lerp), 0]
        self.neopixels.show()

    def DisplayCurrentAnimation(self):
        self.animSequence.animate()

    def DisplayNextAnimation(self):
        self.ClearPixels()
        self.animSequence.next()

    def DisplayPreviousAnimation(self):
        self.ClearPixels()
        self.animSequence.previous()