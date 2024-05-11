import time
import Helpers
import Hardware
import Settings

# Modes
from ControlModes import BrightnessMode
from ControlModes import DefaultMode
from ControlModes import SensitivityMode
from ControlModes import DurationMode
from ControlModes import SpeedMode

#Load Settings before anything else
Settings.Settings.LoadSettings()

#Hardware
hardware = Hardware.Hardware()

#Mode Setup
modes = []
modes.append(DefaultMode.DefaultMode(hardware))
modes.append(BrightnessMode.BrightnessMode(hardware))
modes.append(SensitivityMode.SensitivityMode(hardware))
modes.append(DurationMode.DurationMode(hardware))
modes.append(SpeedMode.SpeedMode(hardware))

current_mode_index = 0
modes[current_mode_index].OnEnter()

sleepTime = 0.02
lastImpact = time.monotonic()

#Main Loop
while True:
    if hardware.CheckButtonPress():
        prevIndex = current_mode_index
        current_mode_index = Helpers.Repeat(current_mode_index + 1, 0, len(modes) - 1)
        modes[prevIndex].OnExit()
        modes[current_mode_index].OnEnter()

    modes[current_mode_index].OnUpdate()
    #How much to limit here?
    time.sleep(sleepTime)
    
    currentTime = time.monotonic()
    if hardware.DetectImpact() and currentTime - lastImpact > 0.1:
        hardware.TriggerAnimation()
        lastImpact = currentTime
        
#find i2c address
#import board
# i2c = board.I2C()  # uses board.SCL and board.SDA
# while not i2c.try_lock():
#     pass

# try:
#     while True:
#         print(
#             "I2C addresses found:",
#             [hex(device_address) for device_address in i2c.scan()],
#         )
#         time.sleep(2)

# finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
#     i2c.unlock()