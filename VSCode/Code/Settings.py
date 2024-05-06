import storage
import json

SETTINGS_FILE_NAME = "settings.json"
BRIGHTNESS_KEY = "BRIGHTNESS"
SENSITIVITY_KEY = "SENSITIVITY"

class Settings(object):
    num_neopixels = 31

    default_brightness= 0.1
    brightness = default_brightness
    min_brightness = 0.01
    max_brightness = 0.5
    
    default_sensitivity = 0.5
    sensitibity = default_sensitivity
    min_sensitivity = 5
    max_sensitivity = 100
    
    def LoadSettings():
        try:
            with open(SETTINGS_FILE_NAME) as fh:
                storedSettings = json.load(fh)
                Settings.brightness = storedSettings[BRIGHTNESS_KEY]
                Settings.sensitibity = storedSettings[SENSITIVITY_KEY]
        except Exception as e:
            print(e)
            
    def StoreSettings():
        if storage.getmount("/").readonly:
            print("Cannot store settings when in readonly mode!")
        else:
            print("Should be able to store settings")

            dic = dict()
            dic[BRIGHTNESS_KEY] = Settings.brightness
            dic[SENSITIVITY_KEY] = Settings.sensitibity
        
            try:
                with open(SETTINGS_FILE_NAME, 'w') as fh:
                    json.dump(dic, fh)
            except Exception  as e:
                print(e)