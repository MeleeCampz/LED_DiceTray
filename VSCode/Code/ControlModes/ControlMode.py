import Hardware
import time

class ControlMode(object):

    def __init__(self, hardware: Hardware.Hardware):
        self.hardware = hardware
    
    def OnEnter(self):
        #init rotationdelta to avoid sudden jumps when entering state
        self.rotationDelta = self.hardware.UpdateRotaryEncoder()
        self.hardware.ClearPixels()
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