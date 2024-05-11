from ControlModes import ControlMode
import Hardware
from Settings import Settings
import time

class SensitivityMode(ControlMode.ControlMode):
    progressColorStart = (0,0,255)
    progressColorEnd = (0,255,0)
     
    colorNoImpact = (255,0,0)
    colorImpact = (0,255,0)
     
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)
        self.lastImpact = time.monotonic()

    def OnEnter(self):
        super().OnEnter()
        self.UpdateOutput()

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            Settings.sensitivity = self.UpdateSetting(Settings.sensitivity)
            self.hardware.UpdateSensitivity()
            self.UpdateOutput()
            
        if self.hardware.DetectImpact():
            self.lastImpact = time.monotonic()

        self.hardware.SetColorInnerRing(SensitivityMode.colorImpact if (time.monotonic() - self.lastImpact) < 0.5 else SensitivityMode.colorNoImpact)
        self.hardware.Show()   
            
    def OnExit(self):
        super().OnExit()
        Settings.StoreSettings()
        
    def UpdateOutput(self):
        self.hardware.ClearPixels()
        self.hardware.DisplayProgress(Settings.sensitivity, SensitivityMode.progressColorStart, SensitivityMode.progressColorEnd)
        self.hardware.Show()