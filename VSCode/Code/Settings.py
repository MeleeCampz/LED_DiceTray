import storage
import json

SETTINGS_FILE_NAME = "settings.json"

ANIMATION_KEY = "ANIMATION"
BRIGHTNESS_KEY = "BRIGHTNESS"
SENSITIVITY_KEY = "SENSITIVITY"
DURATION_KEY = "DURATION"
SPEED_KEY = "SPEED"

class Settings(object):
    num_neopixels = 31

    default_brightness= 0.1
    brightness = default_brightness
    min_brightness = 0.01
    max_brightness = 0.5
    
    default_sensitivity = 0.5
    sensitivity = default_sensitivity
    min_sensitivity = 0.1
    max_sensitivity = 25
    
    duration_default = 0.1
    duration = duration_default
    min_duration = 1
    max_duration = 60
    
    speed_default = 0.5
    speed = speed_default
    min_speed = 0.1
    max_seed = 10
    
    animation = 0
    
    def LoadSettings():
        try:
            with open(SETTINGS_FILE_NAME) as fh:
                storedSettings = json.load(fh)
                Settings.animation = storedSettings[ANIMATION_KEY]
                Settings.brightness = storedSettings[BRIGHTNESS_KEY]
                Settings.sensitivity = storedSettings[SENSITIVITY_KEY]
                Settings.duration = storedSettings[DURATION_KEY]
                Settings.speed = storedSettings[SPEED_KEY]
                
        except Exception as e:
            print(e)
            
    def StoreSettings():
        if storage.getmount("/").readonly:
            print("Cannot store settings when in readonly mode!")
        else:
            print("Should be able to store settings")

            dic = dict()
            dic[ANIMATION_KEY] = Settings.animation
            dic[BRIGHTNESS_KEY] = Settings.brightness
            dic[SENSITIVITY_KEY] = Settings.sensitivity
            dic[DURATION_KEY] = Settings.duration
            dic[SPEED_KEY] = Settings.speed
        
            try:
                with open(SETTINGS_FILE_NAME, 'w') as fh:
                    json.dump(dic, fh)
            except Exception  as e:
                print(e)