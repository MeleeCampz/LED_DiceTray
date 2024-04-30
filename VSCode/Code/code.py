import time
import Helpers
import Hardware

#region Modes
import DefaultMode
import BrightnessMode

#Hardware
hardware = Hardware.Hardware()

#Mode Setup
modes = []
modes.append(DefaultMode.DefaultMode(hardware))
modes.append(BrightnessMode.BrightnessMode(hardware))
current_mode_index = 0
modes[current_mode_index].OnEnter()


def UpdateMode():
    if hardware.CheckButtonPress():
        prevIndex = current_mode_index
        current_mode_index = Helpers.Repeat(current_mode_index +1, 0, len(modes) - 1)
        modes[prevIndex].OnExit()
        modes[current_mode_index].OnEter()

    modes[current_mode_index].OnUpdate()
   
#Main Loop
while True:
    UpdateMode() 
    #How much to limit here?
    time.sleep(0.1)