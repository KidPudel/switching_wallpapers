# outer logic:
# - trigger on planned time for example 6 day, 19 night
# inner logic:
# - get the time to determine which wallpaper to set
# - change the image
#   - use apple scripts, to get the desktop picture 
# (the full dictionary of AppleScript is in the Script Editor program)
#   - replace it with new

from appscript import app, mactypes
import os
import time

LIGHT = "/Users/iggysleepy/SavedImages/evergreen-hobbit.jpg"
DARK = "/Users/iggysleepy/SavedImages/inthedark.jpg"

def set_wallpaper():
    # set a wallpaper, specific to the time
    current_time = time.localtime()
    finder = app("Finder")
    finder.desktop_picture.set(mactypes.File(LIGHT if current_time.tm_hour < 19 and current_time.tm_hour >= 6 else DARK))

if __name__ == "__main__":
    if os.access(path=LIGHT, mode=os.F_OK) and os.access(path=DARK, mode=os.F_OK):
        set_wallpaper()
    else:
        print("file does not exist")


