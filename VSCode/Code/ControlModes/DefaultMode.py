from ControlModes.ControlMode import ControlMode
import Hardware
import Helpers
from Settings import Settings

#Simple Mode that just display animation
#Turn knob to cycle through different animations
class DefaultMode(ControlMode):     
    def __init__(self, hardware: Hardware.Hardware):
        super().__init__(hardware)
        self.durationRemaining = DefaultMode.GetDuration()
        
    def OnEnter(self):
        super().OnEnter()
        self.hardware.DisplayAnimation(Settings.animation)
    
    def OnExit(self):
        super().OnExit()
        Settings.StoreSettings()

    def OnUpdate(self):
        super().OnUpdate()
        if self.rotationDelta is not 0:
            self.hardware.ClearPixels()
            Settings.animation = Helpers.Repeat(Settings.animation + self.rotationDelta, 0, len(self.hardware.animSequence._members) - 1)
            self.hardware.DisplayAnimation(Settings.animation)
            self.durationRemaining = ControlMode.GetDuration()

        if self.durationRemaining >= 0:
            self.hardware.DisplayCurrentAnimation()
            self.durationRemaining -= self.deltaTime
        else:
            #TODO: Fadeout
            self.hardware.ClearPixels(True)
            
        if self.hardware.DetectImpact():
            self.durationRemaining = ControlMode.GetDuration()
        