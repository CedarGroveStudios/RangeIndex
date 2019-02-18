# The MIT License (MIT)
# Copyright (c) 2019 Jan Goolsbey for Cedar Grove Studios
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`cedargrove_range_index`
================================================================================
A CircuitPython helper for scaling input values with hysteresis added to control noise
* Author(s): Jan Goolsbey

Implementation Notes
--------------------
**Hardware:**
**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/CedarGroveStudios/RangeIndex.git"

class range_index:
    """range_index helper class."""

    def __init__(self, in_min=0, in_max=65535, out_min=0, out_max=65535, hyst_factor=0.25, debug=False):
        self._in_min = in_min
        self._in_max = in_max
        self._out_min = out_min
        self._out_max = out_max
        self._hyst_factor = hyst_factor
        self._debug = debug

        if self._debug:
            print("*Init:", self.__class__)
            print("* ", self.__dict__)

    @property
    def range(self):
        """The range input's minimum and maximum floating or integer values. Defaults are 0 and 65535."""
        return self._in_min, self._in_max

    @range.setter
    def range(self, rng):
        in_min, in_max = rng
        if self._debug:
            print("*range.setter: ", in_min, in_max)
        if in_min == in_max:
            raise RuntimeError("Invalid range input; minimum and maximum values cannot be equal")
        self._in_min = in_min
        self._in_max = in_max

    @property
    def index(self):
        """The index output's minimum and maximum floating or integer values. Defaults are 0 and 65535."""
        return self._out_min, self._out_max

    @index.setter
    def index(self, idx):
        out_min, out_max = idx
        if self._debug:
            print("*index.setter: ", out_min, out_max)
        if out_min == out_max:
            raise RuntimeError("Invalid index output; minimum and maximum values cannot be equal")
        if out_min > out_max:
            raise RuntimeError("Invalid index output; minimum value must be smaller than maximum value")
        self._out_min = out_min
        self._out_max = out_max

    @property
    def hysteresis(self):
        """The hysteresis factor value. Must be between 0 and 1.0 (0 to 100% of index value slice). Default is 0.25"""
        return self._hyst_factor

    @hysteresis.setter
    def hysteresis(self, hyst_factor):
        if self._debug:
            print("*hysteresis.setter: ", hyst_factor)
        if not (0 <= hyst_factor <= 1.0):
            raise RuntimeError("! Invalid hysteresis factor; value must be between 0 and 1.0")
        self._hyst_factor = hyst_factor

    def range_index(self, new_input, old_index, offset):
        """Determines index output and hysteresis offset values from range input value.
        :param float new_input: The range input value.
        :param float old_index: The previous index output value.
        :param float offset: The previous hysteresis offset value.
        """
        if self._debug:
            print("*range_index")
            print("* New range input:", new_input, " Previous index output:", old_index, " Prev offset:", offset, " Hyst factor: ", self._hyst_factor)

        if not 0 <= (new_input + offset) <= 65535:
            offset = 0

        index = int(self.map_range(new_input + offset))
        if index != old_index:
            offset = int(self._hyst_factor * self.sign(index - old_index) * (self._in_max / self._out_max))
            if self._debug:
                print("* New index:", index, "New offset:", offset, "Change flag: True")
            return index, offset, True
        else:
            if self._debug:
                print("* Same index:", index, "Same offset:", offset, "Change flag: False")
            return index, offset, False

    def map_range(self, x):
        """Determines the index output value of the range input value.
        :param float x: The range input value.
        """
        mapped = (x - self._in_min) * (self._out_max - self._out_min) / (self._in_max - self._in_min) + self._out_min
        if self._out_min <= self._out_max:
            return max(min(mapped, self._out_max), self._out_min)
        else:
            return min(max(mapped, self._out_max), self._out_min)

    def sign(self, x):
        """Determines the sign of a numeric value.
        :param float x: The value.
        """
        if x >= 0: return 1
        else: return -1


key_49 = range_index(0, 1024, 0, 49, hyst_factor=0.1, debug=True)
key_88 = range_index(0, 1024, 0, 88, hyst_factor=0.2, debug=True)

print("-----")
print("key_49:", key_49.range_index(512, 24, 2))
print("-----")
print("key_88:", key_88.range_index(256, 44, 2))

print("----- change key_88 range")
key_88.range = (0,2048)
print("key_88:", key_88.range_index(256, 44, 2))

print("----- change key_88 index")
key_88.index = (34, 80)
print("key_88:", key_88.range_index(256, 44, 2))

print("----- change key_88 hysteresis factor")
key_88.hysteresis = 0.5
print("key_88:", key_88.range_index(256, 44, 2))
