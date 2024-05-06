from ControlModes import ControlMode
import Hardware
from Settings import Settings

class BrightnessMode(ControlMode.ControlMode):
    
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)

    def OnEnter(self):
        super().OnEnter()
        self.hardware.DisplayProgress(Settings.brightness)

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            self.hardware.UpdateBrightness(self.rotationDelta)
            self.hardware.DisplayProgress(Settings.brightness)
            
    def OnExit(self):
        super().OnExit()
        Settings.StoreSettings()