import ControlMode
import Hardware

class BrightnessMode(ControlMode.ControlMode):
    
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)

    def OnEnter(self):
        super().OnEnter()
        self.hardware.DisplayProgress(self.hardware.current_brightness)

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            self.hardware.UpdateBrightness(self.rotationDelta)
            self.hardware.DisplayProgress(self.hardware.current_brightness)
            
    def OnExit(self):
        super().OnExit()