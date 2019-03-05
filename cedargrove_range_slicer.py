# The MIT License (MIT)

# Copyright (c) 2019 Jan Goolsbey, Cedar Grove Studios

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
`cedargrove_range_slicer`
================================================================================
Range_Slicer 2019-03-03 v01
A CircuitPython class for scaling a range of input values into indexed/quantized
output values. Output slice hysteresis is used to provide dead-zone squelching.

* Author(s): Jan Goolsbey

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/CedarGroveStudios/Range_Slicer.git"

class Slicer:
    """range_slicer helper class."""

    def __init__(self, in_min=0, in_max=65535, out_min=0, out_max=65535, slice=1.0, hyst_factor=0.25, debug=False):
        self._in_min = in_min
        self._in_max = in_max
        self._out_min = out_min
        self._out_max = out_max
        self._slice = slice
        self._hyst_factor = hyst_factor
        self._old_idx = 0
        self._offset = 0
        self._debug = debug

        if self._debug:
            print("*Init:", self.__class__)
            print("* ", self.__dict__)

    @property
    def range(self):
        """The range input's minimum and maximum floating or integer values. Defaults are 0 and 65535."""
        return self._in_min, self._in_max

    @range.setter
    def range(self, min=0, max=65535):
        if min == max:
            raise RuntimeError("Invalid range input; minimum and maximum values cannot be equal")
        self._in_min = min
        self._in_max = max

    @property
    def index(self):
        """The index output's minimum and maximum integer values. Defaults are 0 and 65535."""
        return self._out_min, self._out_max

    @index.setter
    def index(self, min, max):
        if min == max:
            raise RuntimeError("Invalid index output; minimum and maximum values cannot be equal")
        self._out_min = min
        self._out_max = max

    @property
    def slice(self):
        """The slice size value. Default is 1."""
        return self._slice

    @slice.setter
    def slice(self, size=1.0):
        if slice == 0:
            raise RuntimeError("Invalid slice size; slice size value cannot be zero")
        self._slice = size

    @property
    def hysteresis(self):
        """The hysteresis factor value. Must be between 0 and 1.0 (0 to 100% of index value slice). Default is 0.25"""
        return self._hyst_factor

    @hysteresis.setter
    def hysteresis(self, hyst_factor=0.25):
        if not (0 <= hyst_factor <= 1.0):
            raise RuntimeError("! Invalid hysteresis factor; value must be between 0 and 1.0")
        self._hyst_factor = hyst_factor

    def range_slicer(self, input=0):
        """Determines index output value from the range input value.
        :param float input: The range input value.
        """
        if not self._in_min <= (input + self._offset) <= self._in_max:
            self._offset = 0  # if input + offset is outside input range

        index = int((self.map_range(input + self._offset)) / self._slice) * self._slice  # determine index value
        if index != self._old_idx:
            self._offset = self._hyst_factor * self.sign(index - self._old_idx) * ((self._in_max - self._in_min) / (self._out_max - self._out_min))
            self._old_idx = index
            return index  # return new index value
        else:
            return self._old_idx  # return old index value

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
