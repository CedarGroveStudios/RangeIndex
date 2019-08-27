#  Metro M4 Joystick MIDI CC
#  for USB MIDI
#  Reads analog inputs, sends out MIDI CC values
#  written by John Park with Kattni Rembor and Jan Goolsbey for range and hysteresis code

import time
import adafruit_midi
import board
import cedargrove_range_slicer as rs
from analogio import AnalogIn
print("---Joystick MIDI CC---")

midi = adafruit_midi.MIDI(out_channel=0)  # Set the output MIDI channel (0-15)

# Instaces of range_slicer that defines the characteristics of the potentiometers
#  This list contains the input range, output range, slice size, and hysteresis value for each knob.
#   example ranges:
#   0 min, 127 max: full range control voltage
#   36 (C2) min, 84 (B5) max: 49-note keyboard
#   21 (A0) min, 108 (C8) max: 88-note grand piano
cc_range = [
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_0: 0 to 127: full range MIDI CC/control voltage for VCV Rack
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_1:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_2:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_3:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_4:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_5:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_6:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_7:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_8:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_9:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_10:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_11:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_12:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_13:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25),  # knob_14:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25)  # knob_15:
]

knob_count = 2  # Set the total number of potentiometers used

# Create the input and slicer objects list for potentiometers
knob = []
for k in range(knob_count):
    knobs = AnalogIn(getattr(board, "A{}".format(k)))  # get pin # attribute, use string formatting
    knob.append(knobs)
    cc_range[k]  # creates an object instance of the slicer

while True:
    # read each knob value, form a MIDI CC message and send it:
    # controller number is 'n', value can be 0 to 127
    for n in range(knob_count):
        midi.control_change(n, cc_range[n].range_slicer(knob[n].value))
    time.sleep(0.01)