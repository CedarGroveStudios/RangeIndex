# range_slicer_module 2019-04-07 v00.py
# --->   works only with CircuitPython 3.1.1   <---
# Range_Slicer PCB 2019-04-06 rev00 with ItsyBitsy M4

import board
import busio as io
import time
import random as ran
import pulseio
import array
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn, AnalogOut
from simpleio import map_range
import microcontroller as mcu  # for checking CPU temperature
import gc  # for checking memory capacity
import neopixel as neo  # Feather M4
import adafruit_ssd1306
import cedargrove_range_slicer as rs

# ### DEFINE AND INITIALIZE PINS AND DEVICES ###
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
    oled_connected = False  # if no i2C connect exception
    print("OLED NOT connected")

if oled_connected:
    screen_pause = 0.0
    oled.fill(0)
    oled.text("Range_Slicer v00", 0, 8)
    oled.show()
    time.sleep(screen_pause)

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
sel_ph_a_pin = DigitalInOut(board.D11)
sel_ph_a_pin.direction = Direction.INPUT
sel_ph_a_pin.pull = Pull.UP
sel_ph_b_pin = DigitalInOut(board.D10)
sel_ph_b_pin.direction = Direction.INPUT
sel_ph_b_pin.pull = Pull.UP

sel_sw_pin = DigitalInOut(board.D12)
sel_sw_pin.direction = Direction.INPUT
sel_sw_pin.pull = Pull.UP

rot_en_pin = DigitalInOut(board.D13)
rot_en_pin.direction = Direction.OUTPUT

# poll_pin = DigitalInOut(board.D5)  # uncomment for ItsyBitsy
# poll_pin.direction = Direction.OUTPUT  # uncomment for ItsyBitsy

# ### LISTS AND DICTIONARIES ###

# ### HELPERS ###

def graph_frame():  # draw screen axes and labels
    oled.fill(0)
    oled.line(93,0,93,63,1)
    oled.line(93,2,95,2,1)
    oled.line(32,61,95,61,1)
    oled.line(33,61,33,63,1)
    oled.text(" IN", 0, 0)
    oled.text("max", 0, 9)
    oled.text("min", 0, 27)
    oled.text(" HYS", 0, 45)
    oled.text(" OUT", 97, 0)
    oled.text("max", 97, 9)
    oled.text("min", 97, 27)
    oled.text(" SLC", 97, 45)
    oled.show()

def graph_values(x_min, x_max, y_min, y_max, hys, slc):  # knob values
    oled.text(str(x_max)+".0", 0, 18)
    oled.text(str(x_min)+".0", 0, 36)
    oled.text(str(hys)+"%", 0, 54)
    oled.text(str(y_max)+".0", 97, 18)
    oled.text(str(y_min)+".0", 97, 36)
    oled.text(str(slc)+".0", 97, 54)
    oled.show()

def graph_point(x,y,cross_size):  # current in/out value pointers
    # output axis (y)
    oled.line(93,y,95,y,1)
    oled.line(95,y-1,95,y+1,1)
    # input axis (x)
    oled.line(x,61,x,63,1)
    oled.line(x-1,63,x+1,63,1)
    # crosshair (x,y)
    oled.line(x-cross_size,y,x+cross_size,y,1)
    oled.line(x,y-cross_size,x,y+cross_size,1)

    oled.show()

def graph_in_min_max(x1, x2):  # show min/max and hysteresis lines
    for y in range(4, 62-1, 4):
        oled.line(x1,y,x1+1,y,1)
    for y in range(4, 62-1, 4):
        oled.line(x2,y,x2+1,y,1)
    oled.show()

def graph_out_min_max(y1, y2):  # show output min/max lines
    for x in range(35, 93-1, 4):
        oled.line(x,y1,x+1,y1,1)
    for x in range(35, 93-1, 4):
        oled.line(x,y2,x+1,y2,1)
    oled.show()

def graph_hyst(x_min, x_max, y_min, y_max, hys):  # show hysteresis lines
    oled.line(x_min-hys,y_max,x_max-hys,y_min,1)
    oled.line(x_min+hys,y_max,x_max+hys,y_min,1)
    oled.show()

# ### MAIN CODE SECTION ###

# initialize voice selection index and offset
dsp_voice_idx = 0
dsp_voice_idx_old = 0
dsp_voice_offset = 0

# display system status
gc.collect()  # clean up memory
print("Range_Slicer v00")
print("GC.mem_free:    %0.3f" % float(gc.mem_free()/1000), "KB")
print("CPU.freqency:    %0.1f" % float(mcu.cpu.frequency/1000000), "MHz")
print("CPU.temperature: %0.1f" % mcu.cpu.temperature, "C")
volt_mon = map_range(AnalogIn(board.VOLTAGE_MONITOR).value, 0, 65520, 0, 6.6)
print("Voltage Monitor: %0.1f" % volt_mon, "V")

if oled_connected:
    oled.fill(0)
    oled.text("Range_Slicer v00", 0, 0)
    oled.text("KB free", 56, 10)
    oled.text(str(int(gc.mem_free()/1e2)/10), 8, 10)
    oled.text("MHz", 56, 20)
    oled.text(str(int(mcu.cpu.frequency/1e5)/10), 8, 20)
    oled.text("C", 56, 30)
    oled.text(str(int(mcu.cpu.temperature*10)/10), 16, 30)
    oled.text(str(int(volt_mon*10)/10), 96, 30)
    oled.text("V", 119, 30)
    oled.show()
    time.sleep(screen_pause)

# ### Main Loop ###

graph_frame()


while True:
    x = 64
    y = 32
    x_min = x - 20
    x_max = x + 20
    y_min = y - 20
    y_max = y + 20
    hys = 5
    slc = 1
    cross_size = 3

    graph_values(x_min, x_max, y_min, y_max, hys, slc)
    graph_point(x, y, cross_size)
    graph_in_min_max(x_min, x_max)
    graph_out_min_max(y_min, y_max)
    graph_hyst(x_min, x_max, y_min, y_max, hys)
    time.sleep(1)
    pass
