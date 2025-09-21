# CYDr Touchscreen Demo
# Tags: Micropython Cheap Yellow Device DIYmall ESP32-2432S028R
# Last Updated: June 15, 2024
# Author(s): James Tobin
# License: MIT
# https://github.com/jtobinart/MicroPython_CYD_ESP32-2432S028R

from cydr import CYD
import time

# Create an instance of CYD
cyd = CYD()

# Draw "TOUCH ME" at the top of the display.
cyd.display.draw_text8x8(cyd.display.width // 2 - 32, 10, "TOUCH ME", cyd.WHITE, background=cyd.RED)

# List of color choices
colors = [cyd.RED, cyd.GREEN, cyd.BLUE]

c = 0    # Initial color choice
r = 4    # Radius of cirlces

while True:
    time.sleep(0.05)
    x, y = cyd.touches()    #
    
    # Check that there ar new touch points (Default values are x = 0, y = 0)
    if x == 0 and y == 0:
        continue
    
    # Double tap to exit
    if cyd.double_tap(x,y):
        break

    print("Touches:", x, y)

    # Prevent circles from appearing off-screen.
    y = min(max(((cyd.display.height - 1) - y), (r+1)),(cyd.display.height-(r+1)))
    x = min(max(((cyd.display.width - 1) - x), (r+1)),(cyd.display.width-(r+1)))
    
    # Create circle
    cyd.display.fill_circle(x, y, r, cyd.GREEN)

cyd.shutdown()
