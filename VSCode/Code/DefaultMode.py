import ControlMode
import Hardware

#Simple Mode that just display animation
#Turn knob to cycle through different animations
class DefaultMode(ControlMode.ControlMode):
    
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)
        
    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta > 0:
            self.hardware.DisplayNextAnimation()
        elif self.rotationDelta < 0:
            self.hardware.DisplayPreviousAnimation()

        self.hardware.DisplayCurrentAnimation()