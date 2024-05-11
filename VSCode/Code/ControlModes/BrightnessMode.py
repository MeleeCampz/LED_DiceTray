from ControlModes.ControlMode import ControlMode
import Hardware
from Settings import Settings

class BrightnessMode(ControlMode):
    
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)

    def OnEnter(self):
        super().OnEnter()
        self.UpdateOutput()

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            Settings.brightness = self.UpdateSetting(Settings.brightness)
            self.hardware.UpdateBrightness()
            self.UpdateOutput()
            
    def OnExit(self):
        super().OnExit()
        Settings.StoreSettings()
        
    def UpdateOutput(self):
        self.hardware.ClearPixels()
        self.hardware.DisplayProgress(Settings.brightness)
        self.hardware.SetColorInnerRing((127,127,127))
        self.hardware.Show()