# range_slicer_displayio 2019-04-08 v00.py
# Range_Slicer PCB 2019-04-06 rev00 with ItsyBitsy M4

import board
import time
import random as ran
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn, AnalogOut
from simpleio import map_range
import microcontroller as mcu  # for checking CPU temperature
import gc  # for checking memory capacity
import neopixel as neo  # Feather M4

import displayio
import adafruit_ssd1306

import cedargrove_range_slicer as rs

# ### DEFINE AND INITIALIZE PINS AND DEVICES ###
#  set up and initialize oled display
while(True):
    spi = board.SPI()
    dc_pin = DigitalInOut(board.D6)
    reset_pin = DigitalInOut(board.D9)
    cs_pin = DigitalInOut(board.D5)

    displayio.release_displays()
    display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin)

    display = adafruit_ssd1306.SSD1306_SPI(128, 64, display_bus, dc_pin, reset_pin, cs_pin)

    display_connected = True
    print("display connected")

    splash = displayio.Group(max_size=10)
    display.show(splash)

    color_bitmap = displayio.Bitmap(128, 64, 1)
    color_palette = displayio.Palette(1)
    color_palette = 0xFFFFFF

    try:
        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, position=(0, 0))
    except TypeError:
        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

    splash.append(bg_sprite)

try:
        pass
except:
    display_connected = False  # if no SPI connect exception
    print("display NOT connected")

if display_connected:
    screen_pause = 1.0
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
    display.fill(0)
    display.line(93,0,93,63,1)
    display.line(93,2,95,2,1)
    display.line(32,61,95,61,1)
    display.line(33,61,33,63,1)
    display.text("IN", 0, 0)
    display.text(" max", 0, 9)
    display.text(" min", 0, 27)
    display.text("HYS", 0, 45)
    display.text(" OUT", 97, 0)
    display.text("max", 97, 9)
    display.text("min", 97, 27)
    display.text(" SLC", 97, 45)
    display.show()

def graph_values():  # knob values
    display.text(" 0.0", 0, 18)
    display.text(" 0.0", 0, 36)
    display.text("  0%", 0, 54)
    display.text("0.0", 97, 18)
    display.text("0.0", 97, 36)
    display.text("0.0", 97, 54)
    display.show()

def graph_point():  # current in/out value pointers
    size = 4  # 1/2 crosshair size
    x = 64
    y = 32
    # output axis (y)
    display.line(93,y,95,y,1)
    display.line(95,y-1,95,y+1,1)
    # input axis (x)
    display.line(x,61,x,63,1)
    display.line(x-1,63,x+1,63,1)
    # crosshair (x,y)
    display.line(x-size,y,x+size,y,1)
    display.line(x,y-size,x,y+size,1)

    display.show()

def graph_min_max():  # show min/max and hysteresis lines
    # input limits
    x1 = 44
    for y in range(4, 62-1, 4):
        display.line(x1,y,x1+1,y,1)
    x2 = 83
    for y in range(4, 62-1, 4):
        display.line(x2,y,x2+1,y,1)

    # output limits
    y1 = 10
    for x in range(35, 93-1, 4):
        display.line(x,y1,x+1,y1,1)
    y2 = 54
    for x in range(35, 93-1, 4):
        display.line(x,y2,x+1,y2,1)

    # hysteresis lines
    display.line(x1-2,y2,x2-2,y1,1)
    display.line(x1+2,y2,x2+2,y1,1)

    display.show()

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

if display_connected:
    display.fill(0)
    display.text("Range_Slicer v00", 0, 0)
    display.text("KB free", 56, 10)
    display.text(str(int(gc.mem_free()/1e2)/10), 8, 10)
    display.text("MHz", 56, 20)
    display.text(str(int(mcu.cpu.frequency/1e5)/10), 8, 20)
    display.text("C", 56, 30)
    display.text(str(int(mcu.cpu.temperature*10)/10), 16, 30)
    display.text(str(int(volt_mon*10)/10), 96, 30)
    display.text("V", 119, 30)
    display.show()
    time.sleep(screen_pause)

# ### Main Loop ###

graph_frame()


while True:
    graph_values()
    graph_point()
    graph_min_max()
    time.sleep(1)
    pass
