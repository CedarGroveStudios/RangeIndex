# standalone lissajous generator
# lissajous 2019-04-18 v01.py
#   tested with CircuitPython 4.0.0b7

import board
import time
import busio as io
import random as ran
from math import sin, pi
from digitalio import DigitalInOut
from analogio import AnalogIn
from simpleio import map_range
import microcontroller as mcu  # for checking CPU temperature
import os  # for checking CircuitPython version and machine designator
import gc  # for checking memory capacity
import neopixel as neo  # Feather M4

import adafruit_framebuf
import adafruit_ssd1306

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

    io.try_lock()
    io.configure(baudrate=12000000)

    oled_connected = True
    print("OLED connected")
except:
    oled_connected = False  # SPI connection exception
    print("OLED NOT connected")

if oled_connected:
    oled.fill(0)
    oled.text("Lissajous", 0, 0, True)
    oled.show()

# dim the on-board RGB LED, yellow indicator
pixel = neo.NeoPixel(board.NEOPIXEL,1, brightness=0.01, auto_write=False)
pixel[0] = (200, 200, 0)
pixel.write()
time.sleep(0.1)

# ### HELPERS ###

def graph_frame():  # draw screen axes and labels
    oled.fill(0)
    oled.vline(33, 0, 64, 1)
    oled.pixel(32, 1, 1)
    oled.hline(32, 62, 64, 1)
    oled.pixel(94, 63, 1)
    oled.show()

def graph_dot(x, y, old_x, old_y, x_min, x_max, color):  # current in/out value pointers
    x1, y1 = plot_xy(x, y)
    x2, y2 = plot_xy(old_x, old_y)
    if x != old_x or y != old_y:
        # plot data point
        if x_min < x_max:
            if x_min < x < x_max:
                oled.pixel(x1,y1,color)  # burn point
        elif x_min > x_max:
            if x_min > x > x_max:
                oled.pixel(x1,y1,color)  # burn point
        # output point
        oled.vline(33, y2 - 2, 5, 1)
        oled.vline(33, y1 - 2, 5, 0)
        oled.pixel(33, y2, 0)
        oled.pixel(33, y1, 1)
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

def clear_plot(x_min, x_max, y_min, y_max):  # erase plot area and redraw min/max lines
    for y in range(0, 62):
        oled.hline(34, y, 61, 0)
    return

# ### MAIN CODE SECTION ###

# display system status
gc.collect()  # clean up memory
print("Lissajous")
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
    time.sleep(1)

x_min = 0
x_max = 10
y_min = 0
y_max = 10

old_x = 5
old_y = 5

graph_frame()  # plot axis and limit lines
clear_plot(x_min, x_max, y_min, y_max)  # clear plot area

# ### MAIN LOOP ### #

while True:
    # offset (phase) and frequency parameters
    off1 = ran.randrange(0, 5)
    freq1 = ran.randrange(1, 8)
    off2 = ran.randrange(0, 4)
    freq2 = ran.randrange(1, 8)

    size = 4
    res = 80  # number of steps in 360-degree (2pi-radians) cycle

    for i in range(0, int(2 * pi * res) + 1):
        x = (sin(i/res * freq1 + off1) * size) + 5
        y = (sin(i/res * freq2 + off2) * size) + 5
        old_x, old_y = graph_dot(x, y, old_x, old_y, x_min, x_max, 1)

    time.sleep(1)

    for i in range(int(2 * pi * res), -2, -1):
        x = (sin(i/res * freq1 + off1) * size) + 5
        y = (sin(i/res * freq2 + off2) * size) + 5
        old_x, old_y = graph_dot(x, y, old_x, old_y, x_min, x_max, 0)

    clear_plot(x_min, x_max, y_min, y_max)
    time.sleep(0.5)
    
