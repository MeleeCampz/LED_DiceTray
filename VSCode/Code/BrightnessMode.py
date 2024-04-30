import Mode
import Hardware

class BrightnessMode(Mode):
    def __init__(self, hardware: Hardware.Hardware):
        super.__init__(self, hardware)

    def OnEnter(self):
        super.OnEnter(self)
        self.hardware.DisplayProgress(self.hardware.current_brightness)

    def OnUpdate(self):
        super.OnUpdate(self)
        if self.rotationDelta is not 0:
            self.hardware.UpdateBrightness(self.rotationDelta)
            self.hardware.DisplayProgress(self.hardware.current_brightness)