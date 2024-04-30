#Excuse my lack of Python knowledge..
#Is this how to do basic state machine in Python. OOP in python even used?

import Hardware

class Mode:
    def __init__(self, hardware: Hardware.Hardware):
        self.hardware = hardware
    
    def OnEnter(self):
        #init rotationdelta to avoid sudden jumps when entering state
        self.rotationDelta = self.hardware.UpdateRotaryEncoder()

    def OnExit(self):
        pass

    def OnUpdate(self):
        self.hardware.UpdateButton()
        self.rotationDelta = self.hardware.UpdateRotaryEncoder()
        