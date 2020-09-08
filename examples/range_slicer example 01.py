# range_slicer example 01
# reads two potentiometer inputs and produces -1.0 to +1.0 normalized outputs,
# one with an inverted output range.

import time
import board
import cedargrove_range_slicer as rs
from analogio import AnalogIn
print("Two Normalized Outputs: Range_Slicer example 01")

# establish range_slicer instances, one for each analog potentiometer input
#   input ranges are adjusted for unique potentiometer inaccuracies and noise
#   slice size divides the output into 10 slices
#   hysteresis factor is 25% of a slice

ctrl_0 = rs.Slicer(200, 65335, -1.0, +1.0, 0.2, 0.25)
ctrl_1 = rs.Slicer(375, 65520, +1.0, -1.0, 0.2, 0.25)

# establish analog inputs
pot_0 = AnalogIn(board.A0)
pot_1 = AnalogIn(board.A1)

while True:  # read potentiometer values
    control_0 = pot_0.value
    control_1 = pot_1.value

    # calculate output values and print (or plot in Mu)
    out_0 = ctrl_0.range_slicer(control_0)
    out_1 = ctrl_1.range_slicer(control_1)
    print( (control_0 / 65535, control_1 / 65535, out_0, out_1) )

    time.sleep(0.1)  # pause for 0.1 second
