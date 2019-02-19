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
        if in_min == in_max:
            raise RuntimeError("Invalid range input; minimum and maximum values cannot be equal")
        self._in_min = in_min
        self._in_max = in_max

    @property
    def index(self):
        """The index output's minimum and maximum integer values. Defaults are 0 and 65535."""
        return self._out_min, self._out_max

    @index.setter
    def index(self, idx):
        out_min, out_max = idx
        if out_min == out_max:
            raise RuntimeError("Invalid index output; minimum and maximum values cannot be equal")
        self._out_min = out_min
        self._out_max = out_max

    @property
    def hysteresis(self):
        """The hysteresis factor value. Must be between 0 and 1.0 (0 to 100% of index value slice). Default is 0.25"""
        return self._hyst_factor

    @hysteresis.setter
    def hysteresis(self, hyst_factor):
        if not (0 <= hyst_factor <= 1.0):
            raise RuntimeError("! Invalid hysteresis factor; value must be between 0 and 1.0")
        self._hyst_factor = hyst_factor

    def range_index(self, new_input=0, old_index=0, offset=0):
        """Determines index output and hysteresis offset values from range input value.
        :param float new_input: The range input value.
        :param float old_index: The previous index output value.
        :param float offset: The previous hysteresis offset value.
        """

        if not self._in_min <= (new_input + offset) <= self._in_max:
            offset = 0

        index = int(self.map_range(new_input + offset))
        if index != old_index:
            offset = self._hyst_factor * self.sign(index - old_index) * ((self._in_max-self._in_min) / (self._out_max-self._out_min))
            return index, offset, True
        else:
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
