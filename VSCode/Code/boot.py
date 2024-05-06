import storage
import board
import digitalio

disableWriteButton = digitalio.DigitalInOut(board.D11)
disableWriteButton.direction = digitalio.Direction.INPUT
disableWriteButton.pull = digitalio.Pull.UP

readonly = not disableWriteButton.value

storage.remount("/", readonly= readonly)
print("Storage is readonly is {0}".format(readonly))

#in case storage cannot be mounted - 
#first BACKUP EVERYTHING then
# connect to REPL using serial monitor and ececute
#import storage
#storage.erase_fileystem()