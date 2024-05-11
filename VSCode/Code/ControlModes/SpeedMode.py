from ControlModes import ControlMode
import Hardware
from Settings import Settings
import math
import time
import Helpers

class SpeedMode(ControlMode.ControlMode):
    progressColorStart = (255,0,128)
    progressColorEnd = (255,255,0)
        
    speedColor1 = (255,0,0)
    speedColor2 = (0,0,255)
        
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)

    def OnEnter(self):
        super().OnEnter()
        self.UpdateTime()
        self.hardware.DisplayProgress(Settings.speed, SpeedMode.progressColorStart, SpeedMode.progressColorEnd)

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            Settings.speed = self.UpdateSetting(Settings.speed)
            self.hardware.UpdateSpeed()
            self.UpdateTime()
            
        self.UpdateDisplay()
        self.loopTime += self.deltaTime
        if self.loopTime > self.totalTime:
            self.loopTime = 0
        
               
    def OnExit(self):
        super().OnExit()
        Settings.StoreSettings()
        
    def UpdateTime(self):
        self.totalTime = 1.0 / Helpers.Lerp(Settings.min_speed, Settings.max_seed, Settings.speed)
        self.loopTime = 0
        
    def UpdateDisplay(self):
        self.hardware.ClearPixels()
        self.hardware.DisplayProgress(Settings.speed, SpeedMode.progressColorStart, SpeedMode.progressColorEnd)
        
        perSegment = self.totalTime / self.hardware.num_neopixels_inner
        
        for index in range(self.hardware.num_neopixels_inner):
            self.hardware.neopixels[index] = SpeedMode.speedColor1 if index * perSegment > self.loopTime else SpeedMode.speedColor2
        
        self.hardware.Show()
        
        
        