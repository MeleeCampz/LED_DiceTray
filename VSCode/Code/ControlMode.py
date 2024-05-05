import Hardware

class ControlMode(object):
    
    def __init__(self, hardware: Hardware.Hardware):
        self.hardware = hardware
    
    def OnEnter(self):
        #init rotationdelta to avoid sudden jumps when entering state
        self.rotationDelta = self.hardware.UpdateRotaryEncoder()
        self.hardware.ClearPixels()

    def OnExit(self):
        pass

    def OnUpdate(self):
        self.hardware.UpdateButton()
        self.rotationDelta = self.hardware.UpdateRotaryEncoder()