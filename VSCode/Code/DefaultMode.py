import Mode

#Simple Mode that just display animation
#Turn knob to cycle through different animations
class DefaultMode(Mode):
    def OnUpdate(self):
        super.OnUpdate(self)
        if self.rotationDelta > 0:
            self.hardware.DisplayNextAnimation()
        elif self.rotationDelta < 0:
            self.hardware.DisplayPreviousAnimation()

        self.hardware.DisplayCurrentAnimation()