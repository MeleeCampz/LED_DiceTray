import Hardware
import time
import Helpers
from Settings import Settings

class ControlMode(object):
    def GetDuration() -> float:
        return Helpers.Lerp(Settings.min_duration, Settings.max_duration, Settings.duration)

    def __init__(self, hardware: Hardware.Hardware):
        self.hardware = hardware
    
    def UpdateSetting(self,currentValue: float) -> float:
        return Helpers.Clamp01(currentValue + self.rotationDelta / self.hardware.num_neopixels_outer)
    
    def OnEnter(self):
        #init rotationdelta to avoid sudden jumps when entering state
        self.rotationDelta = self.hardware.UpdateRotaryEncoder()
        self.hardware.ClearPixels(True)
        self.deltaTime = 0
        self.lastTime = time.monotonic()

    def OnExit(self):
        pass

    def OnUpdate(self):
        currentTime = time.monotonic()
        self.deltaTime = currentTime - self.lastTime
        self.lastTime = currentTime
        
        self.hardware.UpdateButton()
        self.rotationDelta = self.hardware.UpdateRotaryEncoder()
        self.hardware.UpdateMPU()