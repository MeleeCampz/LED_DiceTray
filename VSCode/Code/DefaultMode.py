import ControlMode
import Hardware

#Simple Mode that just display animation
#Turn knob to cycle through different animations
class DefaultMode(ControlMode.ControlMode):
    
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)
        self.durationRemaining = 1
        
    def OnEnter(self):
        super().OnEnter()
    
    def OnExit(self):
        super().OnExit()

        
    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta > 0:
            self.hardware.DisplayNextAnimation()
        elif self.rotationDelta < 0:
            self.hardware.DisplayPreviousAnimation()

        if self.durationRemaining >= 0:
            self.hardware.DisplayCurrentAnimation()
            self.durationRemaining -= self.deltaTime
        else:
            #TODO: Fadeout
            self.hardware.ClearPixels(True)
            
        if self.hardware.DetectImpact():
            self.durationRemaining = 30
        