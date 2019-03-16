#  Metro M4 Joystick MIDI CC
#  for MIDI USB or MIDI UART
#  Reads analog inputs, sends out MIDI CC values
#  written by John Park with Kattni Rembor and Jan Goolsbey for range and hysteresis code

import time
import board
import cedargrove_range_slicer as rs
from analogio import AnalogIn

# uncomment for MIDI_USB
# import adafruit_midi
# midi = adafruit_midi.MIDI(out_channel=0, debug=False)  # Set the output MIDI channel (0-15)

# uncomment for MIDI_UART
import cedargrove_midi_uart
midi = cedargrove_midi_uart.MIDI(midi_out=board.TX, midi_in = board.RX, out_channel=0, debug=False)

print("---Joystick MIDI CC for meeblip triode ---")

# Instances of range_slicer that defines the characteristics of the potentiometers
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

# Dictionary of meeblip triode control codes
#   the index coorelates to the knob number (0 - 15)
cc_knobs = {  #   (MIDI channel, CC #, control description)
    1 : (0, 48, 'triode LFO Depth'),
    0 : (5, 49, 'triode LFO Rate'),
    2 : (0, 50, 'triode Oscillator Detune'),
    3 : (0, 51, 'triode Note Glide (Portamento)'),
    4 : (0, 52, 'triode Filter Resonance'),
    5 : (0, 53, 'triode Filter Cutoff'),
    6 : (0, 54, 'triode Filter Decay'),
    7 : (0, 55, 'triode Amplitude Decay'),
    # Knobs only accessible via MIDI:
    8 : (0, 56, 'triode Filter Accent'),
    9 : (0, 57, 'triode Filter Envelope Modulation'),
    10 : (0, 58, 'triode Oscillator Pulse Width'),
    11 : (0, 59, 'triode Filter Attack'),
    12 : (0, 60, 'triode Amplitude Attack'),
    #  Switches
    13 : (0, 64, 'triode Envelope Sustain'),
    14 : (0, 65, 'triode Sub-oscillator'),
    15 : (0, 66, 'triode PWM Sweep'),
    16 : (0, 67, 'triode LFO Destination (osc/filter)'),
    17 : (0, 68, 'triode Oscillator Wave (pulse/sawtooth)'),
    #  Since switches are either in one position or another, any CC with a value from 0-63 will correspond to
    #  “off”; any value from 64-127 will result in “on.”
    #  Switches only accessible via MIDI:
    18 : (0, 69, 'triode LFO Randomize'),
    19 : (0, 70, 'triode LFO Note Retrigger (default ON)'),
}

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
        midi.out_channel = (cc_knobs[n][0])
        midi.control_change(cc_knobs[n][1], int(cc_range[n].range_slicer(knob[n].value)))
    time.sleep(0.01)
