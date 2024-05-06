import ControlMode
import Hardware
from Settings import Settings

class SensitivityMode(ControlMode.ControlMode):
        
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)

    def OnEnter(self):
        super().OnEnter()
        self.hardware.DisplayProgress(Settings.sensitibity)

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            self.hardware.UpdateSensitivity(self.rotationDelta)
            self.hardware.DisplayProgress(Settings.sensitibity)
            
    def OnExit(self):
        super().OnExit()