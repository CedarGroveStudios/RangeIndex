#  Metro M4 Joystick MIDI CC
#  for MIDI USB or MIDI UART
#  Reads analog inputs, sends out MIDI CC values
#  written by John Park with Kattni Rembor and Jan Goolsbey for slicer and hysteresis code

import time
import board
import busio
import cedargrove_range_slicer as rs
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.D13)  # activity indicator
led.direction = Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=31250, timeout=0.001)  # initialize UART

import adafruit_midi  # MIDI protocol encoder/decoder library
uart_midi = adafruit_midi.MIDI(midi_out=uart, midi_in=uart, out_channel=0, debug=False)  # Set the UART output MIDI channel (0-15)
usb_midi = adafruit_midi.MIDI(out_channel=0, debug=False)  # Set the USB output MIDI channel (0-15)

print("---Joystick MIDI CC for meeblip triode ---")

# Instances of range_slicer that defines the characteristics of the potentiometers
#  This list contains the input range, output range, slice size, hysteresis and
#    output data type for each knob.
#   example ranges:
#    0 min, 127 max: full range control voltage
#    36 (C2) min, 84 (B5) max: 49-note keyboard
#    21 (A0) min, 108 (C8) max: 88-note grand piano
cc_range = [
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_0: 0 to 127: full range MIDI CC/control voltage for VCV Rack
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_1:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_2:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_3:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_4:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_5:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_6:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_7:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_8:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_9:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_10:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_11:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_12:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_13:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True),  # knob_14:
    rs.Slicer(0, 65520, 0, 127, 1, 0.25, True)  # knob_15:
]

# Dictionary of meeblip triode control codes
#   the index coorelates to the knob number (0 - 15)
cc_knobs = {  # knob number : (MIDI channel, CC #, control description)
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
    # read each knob value, form a MIDI CC message, and send if changed from previous knob value.
    # send to UART and USB ports
    #  controller number is 'n', index value from range_slicer, channel
    for n in range(knob_count):
        index, flag = cc_range[n].range_slicer(knob[n].value) # read and scale knob value
        if flag:  # did the knob change positions?
            uart_midi.control_change(cc_knobs[n][1], index, cc_knobs[n][0])  # output via UART port
            usb_midi.control_change(cc_knobs[n][1], index, cc_knobs[n][0])  # output via USB port
            led.value = True  # activity indicator
            # print(hex(cc_knobs[n][1]), hex(index), hex(cc_knobs[n][0]))
    time.sleep(0.01)
    led.value = False
