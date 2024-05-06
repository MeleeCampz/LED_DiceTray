#import adafruit_json_stream as json_stream

SETTINGS_FILE_NAME = "settings.json"
BRIGHTNESS_KEY = "BRIGHTNESS"

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
    
    #def __init__(self) -> None:
    #   self.brightness = 0.1

    # def StoreSettings(self):
    #     try:
    #         with open(SETTINGS_FILE_NAME, "a") as fp:
    #             fp.write('{0}: {1:f}\n'.format(BRIGHTNESS_KEY, self.brightness))
    #             fp.flush()
    #     except OSError as e:  # Typically when the filesystem isn't writeable...
    #         print("Failed to store settings")
    #         print(e)

    # def LoadSettings(self):
    #     pass
