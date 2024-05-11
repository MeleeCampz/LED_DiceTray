from ControlModes.ControlMode import ControlMode
import Hardware
from Settings import Settings

class DurationMode(ControlMode):
    progressColorStart = (0,0,128)
    progressColorEnd = (0,0,255)
    tickColor = (255,0,128)
    nontickColor = (0,0,128)
        
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)

    def OnEnter(self):
        super().OnEnter()
        self.hardware.DisplayProgress(Settings.duration, DurationMode.progressColorStart, DurationMode.progressColorEnd)
        self.remainingTime = ControlMode.GetDuration()
        self.UpdateOutput()

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            self.hardware.ClearPixels()
            Settings.duration = self.UpdateSetting(Settings.duration)
            self.hardware.DisplayProgress(Settings.duration, DurationMode.progressColorStart, DurationMode.progressColorEnd)
            self.remainingTime = ControlMode.GetDuration()
            
        self.UpdateOutput()
        self.remainingTime -= self.deltaTime
        
        if self.remainingTime < 0:
            self.remainingTime = ControlMode.GetDuration()
            
    def OnExit(self):
        super().OnExit()
        Settings.StoreSettings()
        
    def UpdateOutput(self):
        percent = self.remainingTime / ControlMode.GetDuration()
        for index in range(self.hardware.num_neopixels_inner):
            isOn = percent >= (index / float(self.hardware.num_neopixels_inner))
            self.hardware.neopixels[index] = DurationMode.tickColor if isOn else DurationMode.nontickColor
        
        self.hardware.Show()