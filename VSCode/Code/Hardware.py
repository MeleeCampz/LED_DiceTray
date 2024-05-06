from MPU import MPU
import board
import neopixel
import digitalio
import rotaryio
import Helpers
from Settings import Settings

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.color import PURPLE, AMBER, JADE
from adafruit_led_animation.sequence import AnimationSequence

import adafruit_debouncer

class Hardware:
    num_neopixels = 31

    default_brightness= 0.1
    min_brightness = 0.01
    max_brightness = 0.5
    
    default_sensitivity = 0.5
    min_sensitivity = 5
    max_sensitivity = 100

    def __init__(self):
        #Neopixels
        self.neopixels = neopixel.NeoPixel(board.D5, self.num_neopixels)
        self.UpdateBrightness(0)
        #Rotary Encoder
        self.encoder = rotaryio.IncrementalEncoder(board.D13, board.D12, 4)
        #Mode Switch Button
        modeButtonPin = digitalio.DigitalInOut(board.D11)
        modeButtonPin.direction = digitalio.Direction.INPUT
        modeButtonPin.pull = digitalio.Pull.UP
        #Add debouncer to button
        self.modeButton = adafruit_debouncer.Debouncer(modeButtonPin)

        #MPU
        self.mpu = MPU.MPU()
        self.UpdateSensitivity(Settings.sensitibity)

        self.last_Position = 0
        self.last_modeButton_State = False

        comet = Comet(self.neopixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
        sparkle = RainbowSparkle(self.neopixels, speed=0.1, num_sparkles=5, period=5)
        blink = Blink(self.neopixels, speed=0.5, color=JADE)
        chase = Chase(self.neopixels, speed=0.1, size=3, spacing=6, color=AMBER)
        rainbow = RainbowChase(self.neopixels, speed=0.1, size=3, spacing=2, step=12)
        self.animSequence = AnimationSequence(comet, sparkle, blink, chase, rainbow)

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
        Settings.brightness = Helpers.Clamp01(Settings.brightness + steps / self.num_neopixels)
        self.neopixels.brightness = Helpers.Lerp(Settings.min_brightness, Settings.max_brightness, Settings.brightness)
        
    def ClearPixels(self, showUpdate = False):
        self.neopixels.fill(0)
        if showUpdate:
            self.neopixels.show()

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

    def TriggerAnimation(self):
        pass

    def UpdateMPU(self):
        self.mpu.Update()

    def DetectImpact(self) -> bool:
        return self.mpu.DetectImpact()
    
    def UpdateSensitivity(self, steps):
        Settings.sensitibity = Helpers.Clamp01(Settings.sensitibity + steps / self.num_neopixels)
        self.mpu.triggerThreshhold = Helpers.Lerp(Settings.min_sensitivity , Settings.max_sensitivity, Settings.sensitibity)