# range_slicer example 02
# reads one potentiometer input and produces an indexed output,
# simulating a 5-position rotary selection switch

import time
import board
import cedargrove_range_slicer as rs
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
print("Rotary Switch: Range_Slicer example 02")

# establish a range_slicer instance for the analog potentiometer input
#   input range is adjusted for unique potentiometer inaccuracies and noise
#   slice size divides the output into 5 slices (switch positions 0 through 4)
#   hysteresis factor is 25% of a slice (adjust this for switch feel)
pot = rs.Slicer(400, 65000, 0, 4, 1, 0.25, True, debug=False)

# set up analog potentiometer input pin
pot_input = AnalogIn(board.A0)

# set up led digital output
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
led.value = False  # turn off led

# list of switch positions
position = [
    "Off",
    "Sine Wave",
    "Square Wave",
    "Triangle Wave",
    "Sawtooth Wave"
]

old_index = -1  # initialize the switch index value

while True:
    new_index = int(pot.range_slicer(pot_input.value))  # read pot and determine the index value

    if new_index != old_index:  # compare old and new; did the index value change?
        print(new_index, position[new_index]) # print switch selection name
        old_index = new_index

        led.value = True  # flash the LED when index value changes
        time.sleep(0.1)
        led.value = False

    time.sleep(0.1)  # pause for 0.1 second
