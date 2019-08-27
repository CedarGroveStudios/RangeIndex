# range_slicer_framebuf 2019-04-16 v00.py
# --->   works with CircuitPython 4.0.0b7   <---
#

import board
import time
import busio as io
import random as ran
from math import sin, cos, radians
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn, AnalogOut
from simpleio import map_range
import microcontroller as mcu  # for checking CPU temperature
import os  # for checking CircuitPython version and machine designator
import gc  # for checking memory capacity
import neopixel as neo  # Feather M4

import adafruit_framebuf
import adafruit_ssd1306
import rotaryio
import cedargrove_range_slicer as rs

# ### DEFINE AND INITIALIZE PINS AND DEVICES ###
buffer = bytearray(round(128 * 64 /8))
fb = adafruit_framebuf.FrameBuffer(buffer, 128, 64, buf_format=adafruit_framebuf.MVLSB)

#  set up and initialize oled display
try:
    spi = io.SPI(board.SCK, MOSI=board.MOSI)
    dc_pin = DigitalInOut(board.D6)
    reset_pin = DigitalInOut(board.D9)
    cs_pin = DigitalInOut(board.D5)
    oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, reset_pin, cs_pin)

    oled_connected = True
    print("OLED connected")
except:
    oled_connected = False  # SPI connection exception
    print("OLED NOT connected")

if oled_connected:
    oled.fill(0)
    oled.text("Range_Slicer v00", 0, 0, True)
    oled.show()

# dim the on-board RGB LED, yellow indicator
pixel = neo.NeoPixel(board.NEOPIXEL,1, brightness=0.01, auto_write=False)
pixel[0] = (200, 200, 0)
pixel.write()
time.sleep(0.1)

# set up analog inputs
cv_in_pin = AnalogIn(board.A0)
cv_in_max_pin = AnalogIn(board.A1)
cv_in_min_pin = AnalogIn(board.A2)
cv_hyst_pin = AnalogIn(board.A3)
cv_slice_pin = AnalogIn(board.A4)
cv_out_min_pin = AnalogIn(board.A5)
# cv_out_max_pin = AnalogIn(board.A6)  # uncomment for ItsyBitsy

# digital inputs and outputs
knob = rotaryio.IncrementalEncoder(board.D11, board.D10)  # ph_A, ph_B; needs to be an interrupt enabled pin

sel_sw_pin = DigitalInOut(board.D12)  # False when pressed
sel_sw_pin.direction = Direction.INPUT
sel_sw_pin.pull = Pull.UP

sel_en_pin = DigitalInOut(board.D13)
sel_en_pin.direction = Direction.OUTPUT
sel_en_pin.value = True  # disable encoder

# poll_pin = DigitalInOut(board.D5)  # uncomment for ItsyBitsy
# poll_pin.direction = Direction.OUTPUT  # uncomment for ItsyBitsy

# ### RANGE_SLICER INSTANCES ###

cv_in_range = rs.Slicer(0, 65520, 0, 10, 0.0024, 0, False, False)  # 0-65540 to 0-10v, 2.4mV resolution for CV inputs
cv_out_range = rs.Slicer(0, 10, 0, 65540, 1, 0, True, False)  # 0-10v to 0-65540 for CV output
hyst_in_range = rs.Slicer(0, 65540, 0, 100, 1, 0, True, False)  # 0-65540 to 0-100%



# Default input to output range; use input setters like 'primary_range.hysteresis(hyst_factor=hys)'
#   to modify individual parameters
pri_range = rs.Slicer(0, 10, 0, 10, 0.1, 0, False, False)

# ### LISTS AND DICTIONARIES ###

oled_lay = [  # text, legend(x,y), value(x,y)
    ("RANGE", 0, 0),
    ("max", 0, 9, 6, 18),  # in_max
    ("min", 0, 27, 6, 36),  # in_min
    ("Hyst", 0, 45, 6, 54),
    ("INDEX", 99, 0),
    ("max", 99, 9, 105, 18),  # out_max
    ("min", 99, 27, 105, 36),  # out_min
    ("Steps", 99, 45, 105, 54)
    ]

# ### HELPERS ###

def graph_frame():  # draw screen axes and labels
    oled.fill(0)
    oled.vline(94, 0, 64, 1)
    oled.pixel(95, 1, 1)
    oled.hline(32, 62, 64, 1)
    oled.pixel(33, 63, 1)
    for i in range(0, 8):
        oled.text(oled_lay[i][0], oled_lay[i][1], oled_lay[i][2], True)
    oled.show()

def graph_values(x_min, x_max, y_min, y_max, hys, slc):  # knob values
    oled.text(str(x_max), oled_lay[1][3], oled_lay[1][4], True)
    oled.text(str(x_min), oled_lay[2][3], oled_lay[2][4], True)
    oled.text(str(y_max), oled_lay[5][3], oled_lay[5][4], True)
    oled.text(str(y_min), oled_lay[6][3], oled_lay[6][4], True)
    oled.text(str(steps), oled_lay[7][3], oled_lay[7][4], True)
    oled.show()

def graph_line(x, y, old_x, old_y, x_min, x_max):  # current in/out value pointers
    x1, y1 = plot_xy(x, y)
    x2, y2 = plot_xy(old_x, old_y)
    if x != old_x or y != old_y:
        # plot line
        if x_min < x_max:
            if x_min < x < x_max:
                oled.line(x2,y2,x1,y1,1)  # continuous line
        elif x_min > x_max:
            if x_min > x > x_max:
                oled.line(x2,y2,x1,y1,1)  # continuous line
        # output point
        oled.vline(94, y2 - 2, 5, 1)
        oled.vline(94, y1 - 2, 5, 0)
        oled.pixel(95, y2, 0)
        oled.pixel(95, y1, 1)
        # input point
        oled.hline(x2 - 2, 62, 5, 1)
        oled.hline(x1 - 2, 62, 5, 0)
        oled.pixel(x2,63,0)
        oled.pixel(x1,63,1)
        oled.show()
    return x, y

def graph_dot(x, y, old_x, old_y, x_min, x_max):  # current in/out value pointers
    x1, y1 = plot_xy(x, y)
    x2, y2 = plot_xy(old_x, old_y)
    if x != old_x or y != old_y:
        # plot data point
        if x_min < x_max:
            if x_min < x < x_max:
                oled.pixel(x1,y1,1)  # burn point
        elif x_min > x_max:
            if x_min > x > x_max:
                oled.pixel(x1,y1,1)  # burn point
        # output point
        oled.vline(94, y2 - 2, 5, 1)
        oled.vline(94, y1 - 2, 5, 0)
        oled.pixel(95, y2, 0)
        oled.pixel(95, y1, 1)
        # input point
        oled.hline(x2 - 2, 62, 5, 1)
        oled.hline(x1 - 2, 62, 5, 0)
        oled.pixel(x2,63,0)
        oled.pixel(x1,63,1)
        oled.show()
    return x, y

def plot_xy(x, y):  # return an oled position in the plot frame
    oled_x = int((x * 5.9) + 34)
    oled_y = int(abs((y * 5.9) - 61))
    return (oled_x, oled_y)

def graph_in_min_max(x_min, x_max):  # show input min/max lines
    x_min, _ = plot_xy(x_min, 0)
    x_max, _ = plot_xy(x_max, 0)
    for y in range(0, 11):
        _, y1 = plot_xy(0, y)
        oled.pixel(x_min, y1, 1)
        oled.pixel(x_max, y1, 1)
    oled.show()

def graph_out_min_max(y_min, y_max):  # show output min/max lines
    _, y_min = plot_xy(0, y_min)
    _, y_max = plot_xy(0, y_max)
    for i in range(0, 2):
        for x in range(0, 11):
            x1, _ = plot_xy(x, 0)
            oled.pixel(x1, y_min, i)
            oled.pixel(x1, y_max, i)
    oled.show()

def clear_plot(x_min, x_max, y_min, y_max):  # erase plot area and redraw min/max lines
    for y in range(0, 62):
        oled.hline(32, y, 61, 0)
    graph_in_min_max(x_min, x_max)
    graph_out_min_max(y_min, y_max)
    return

def graph_hyst(x_min, x_max, y_min, y_max, hys, old_hys, slc):  # show hysteresis value
    oled.fill_rect(oled_lay[3][3], oled_lay[3][4], 27, 8, 0)
    oled.fill_rect(oled_lay[3][3] - 6, oled_lay[3][4], 4, 7, 1)  # draw cursor
    oled.text(str(int(hys*100))+"%", oled_lay[3][3], oled_lay[3][4], True)
    oled.show()
    time.sleep(0.1)
    oled.fill_rect(oled_lay[3][3] - 6, oled_lay[3][4], 4, 7, 0)  # erase cursor
    oled.show()

def get_knob_position(old_sel_position):
    while not sel_sw_pin.value:
        time.sleep(0.1)
    knob.position = old_sel_position
    while sel_sw_pin.value:
        time.sleep(0.01)
    return knob.position

# ### MAIN CODE SECTION ###

# display system status
gc.collect()  # clean up memory
print("Range_Slicer v00")
print("GC.mem_free:    %0.3f" % float(gc.mem_free()/1000), "KB")
print("CPU.freqency:    %0.1f" % float(mcu.cpu.frequency/1000000), "MHz")
print("CPU.temperature: %0.1f" % mcu.cpu.temperature, "C")
volt_mon = map_range(AnalogIn(board.VOLTAGE_MONITOR).value, 0, 65520, 0, 6.6)
print("Voltage Monitor: %0.1f" % volt_mon, "V")
print(os.uname()[4])
print(os.uname()[3])

if oled_connected:
    oled.fill(0)
    oled.text("Range_Slicer v00", 0, 0, True)
    oled.text("KB free", 56, 10, True)
    oled.text(str(int(gc.mem_free()/1e2)/10), 8, 10, True)
    oled.text("MHz", 56, 20, True)
    oled.text(str(int(mcu.cpu.frequency/1e5)/10), 8, 20, True)
    oled.text("C", 56, 30, True)
    oled.text(str(int(mcu.cpu.temperature*10)/10), 16, 30, True)
    oled.text(str(int(volt_mon*10)/10), 96, 30, True)
    oled.text("V", 119, 30, True)
    oled.text("CircuitPython " + os.uname()[2], 0, 50, True)
    oled.show()

# ### Main Loop ###

graph_frame()
old_x = 64
old_y = 32
old_sel_position = None

while True:
    x_min = 1.0
    x_max = 9.0
    y_min = 1.0
    y_max = 9.0
    hys = 0.25
    steps = 5
    slc = abs(y_max - y_min) / steps
    print("slc=", slc)
    d = 50  # set magnifier
    plot_mode = True  # dot = False; line = True

    pri_range.range_min = x_min
    pri_range.range_max = x_max
    pri_range.index_min = y_min
    pri_range.index_max = y_max
    pri_range.hysteresis = hys
    pri_range.slice = slc

    graph_values(x_min, x_max, y_min, y_max, hys, slc)
    clear_plot(x_min, x_max, y_min, y_max)
    graph_hyst(x_min, x_max, y_min, y_max, hys, hys, slc)

    while True:
        while sel_sw_pin.value:
            sel_en_pin.value = True  # disable encoder
            while True:
                off1 = ran.randrange(0, 5)
                freq1 = ran.randrange(1, 8)
                off2 = ran.randrange(0, 4)
                freq2 = ran.randrange(1, 8)
                size = 3
                res = 60
                for i in range(0, int(2 * 3.14159 * res)+1):
                    x = (sin(i/res * freq1 + off1) * size) + 5
                    y = (sin(i/res * freq2 + off2) * size) + 5
                    # print(i, x, y)
                    old_x, old_y = graph_dot(x, y, old_x, old_y, x_min, x_max)
                time.sleep(0.5)
                clear_plot(1,9,1,9)

            if not plot_mode:  # scatter dot mode
                x = ran.randrange(0,10 * d)
                y, _ = pri_range.range_slicer(x/d)
                old_x, old_y = graph_dot(x/d, y, old_x, old_y, x_min, x_max)
            if plot_mode:  # line mode
                for x in range(0 , 10 * d +1):
                    y, _ = pri_range.range_slicer(x/d)
                    old_x, old_y = graph_line(x/d, y, old_x, old_y, x_min, x_max)
                for x in range(10 * d , -1, -1):
                    y, _ = pri_range.range_slicer(x/d)
                    old_x, old_y = graph_line(x/d, y, old_x, old_y, x_min, x_max)
            sel_en_pin.value = False  # enable encoder
        while not sel_sw_pin.value:
            time.sleep(0.1)
        knob.position = int(hys * 100)
        while sel_sw_pin.value:
            old_hys = hys
            hys = knob.position / 100
            if hys < -1:
                hys = -1
                knob.position = int(hys * 100)
            if hys >2:
                hys = 2
                knob.position = int(hys * 100)
            pri_range.hysteresis = hys
            graph_hyst(x_min, x_max, y_min, y_max, hys, old_hys, slc)
        sel_en_pin.value = True  # disable encoder
        clear_plot(x_min, x_max, y_min, y_max)
        time.sleep(0.1)
    pass
