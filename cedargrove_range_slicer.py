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
Range_Slicer 2019-03-21 v23 12:11PM
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

    def __init__(self, in_min=0, in_max=65535, out_min=0, out_max=65535, slice=1.0, hyst_factor=0.25, out_integer=False, debug=False):
        # input parameters
        self._in_min = in_min
        self._in_max = in_max
        self._in_span = (in_max - in_min)

        # output parameters
        self._out_min = out_min
        self._out_max = out_max
        self._out_span_min = min(out_min, out_max)
        self._out_span_max = max(out_max, out_min)
        self._out_span = abs(out_max - out_min)
        self._out_direction = self.sign(out_max-out_min)

        # slice parameters
        self._slice = slice
        self._slice_count = (int(abs(self._out_span) / self._slice)) + 1

        # hysteresis parameters
        self._hyst_factor = hyst_factor

        # output value data type parameters
        self._out_integer = out_integer

        # index parameters
        self._old_idx = 0

        # offset parameters
        self._offset = 0
        self._in_offset = self._in_span / self._slice_count

        # debug parameters
        self._debug = debug
        if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)

    @property
    def range(self):
        """The range input's minimum and maximum floating or integer values. Defaults are 0 and 65535."""
        return self._in_min, self._in_max

    @range.setter
    def range(self, in_min=0, in_max=65535):
        if in_min == in_max:
            raise RuntimeError("Invalid range input; minimum and maximum values cannot be equal")
        self._in_min = in_min
        self._in_max = in_max
        self._in_span = (in_max - in_min)
        self._in_offset = self._in_span / (self._slice_count)

    @property
    def index(self):
        """The index output's minimum and maximum values and the output value data type.
           Default min and max are 0 and 65535; output data value type is floating."""
        return self._out_min, self._out_max, self._out_integer

    @index.setter
    def index(self, out_min=0, out_max=65535, out_integer=False):
        if out_min == out_max:
            raise RuntimeError("Invalid index output; minimum and maximum values cannot be equal")
        self._out_min = out_min
        self._out_max = out_max
        self._out_span_min = min(out_min, out_max)
        self._out_span_max = max(out_max, out_min)
        self._out_span = abs(out_max - out_min)
        self._out_direction = self.sign(out_max - out_min)
        self._out_integer = out_integer

    @property
    def slice(self):
        """The slice size value. Default is 1.0."""
        return self._slice

    @slice.setter
    def slice(self, size=1.0):
        if size == 0:
            raise RuntimeError("Invalid slice size; value cannot be zero")
        self._slice = size
        self._slice_count = (int(abs(self._out_span) / self._slice)) + 1
        self._in_offset = self._in_span / self._slice_count

    @property
    def hysteresis(self):
        """The hysteresis factor value. Must be between 0 and 1.0 (0 to 100% of index value slice). Default is 0.25"""
        return self._hyst_factor

    @hysteresis.setter
    def hysteresis(self, hyst_factor=0.25):
        if not (0 <= hyst_factor <= 1.0):
            raise RuntimeError("Invalid hysteresis factor; value must be between 0 and 1.0")
        self._hyst_factor = hyst_factor

    def range_slicer(self, input=0):
        """Determines index output value from the range input value optionally truncated to an integer data type.
           Returns the new index value and a flag (True/False) indicating if the new index changed from the
           previous index value.
        :param float input: The range input value.
        """
        self._index_mapped = self.mapper(input + self._offset) - self._out_span_min  # mapped with offset removed
        self._slice_number = (self._index_mapped - (self._index_mapped % self._slice)) / self._slice  # determine slice # in sequence of slices
        self._index = (self._out_direction * self._slice_number * self._slice) + self._out_min  # quantize and add back the offset

        # limit index value to within index span
        if self._index < self._out_span_min: self._index = self._out_span_min
        if self._index > self._out_span_max: self._index = self._out_span_max

        if self._out_integer:  # is the output value data type integer?
            self._index = int(self._index)

        if self._index != self._old_idx:  # did the index value change?
            self._offset = self._hyst_factor * self.sign(self._index - self._old_idx) * self._out_direction * self._in_offset
            self._old_idx = self._index

            if self._debug:
                print("** range_slicer ", self.__dict__)

            return self._index, True  # return new index value and change flag
        else:
            if self._debug:
                print("***range_slicer ", self.__dict__)

            return self._old_idx, False  # return old index value and change flag

    def mapper(self, x):
        """Determines the index output value of the range input value.
           (A slightly modified version of Adafruit.CircuitPython.simpleio.map_range.)
        :param float x: The range input value.
        """
        self._mapped = ((x - self._in_min) * (self._out_span) / self._in_span) + self._out_span_min

        if self._out_span_min <= self._out_span_max:
            return max(min(self._mapped, self._out_span_max), self._out_span_min)
        else:
            return min(max(self._mapped, self._out_span_max), self._out_span_min)

    def sign(self, x):
        """Determines the sign of a numeric value. Zero is considered to be a positive value.
        :param float x: The value.
        """
        if x >= 0: return 1
        else: return -1
