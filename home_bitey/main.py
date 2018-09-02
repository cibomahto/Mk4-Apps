"""Default homescreen

This is the default homescreen for the Tilda Mk4.
It gets automatically installed when a badge is
newly activated or reset.
"""

___name___         = "Homescreen (Bitey)"
___license___      = "MIT"
___categories___   = ["Homescreens"]
___dependencies___ = ["homescreen","shared/bitey.png"]
___launchable___   = False
___bootstrapped___ = True

import ugfx
from homescreen import *
import time
from tilda import Buttons

# We ❤️ our sponsors
init()

logo_path = "shared/bitey.png"

# Maximum length of name before downscaling
max_name = 8

# Background stuff

#ugfx.clear(ugfx.html_color(0x800080))
ugfx.clear(ugfx.html_color(0xF230F2))

# Colour stuff
style = ugfx.Style()
style.set_enabled([ugfx.WHITE, ugfx.html_color(0x800080), ugfx.html_color(0x800080), ugfx.html_color(0x800080)])
style.set_background(ugfx.html_color(0x800080))
ugfx.set_default_style(style)

# Logo stuff
ugfx.display_image(
    0,
    0,
    logo_path
)

# update loop
while True:
    sleep_or_exit(0.5)
