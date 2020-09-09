# The MIT License (MIT)

# Copyright (c) 2020 Cedar Grove Studios

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
Range_Slicer 2020-09-08 v28 09:57PM
A CircuitPython class for scaling a range of input values into indexed/quantized
output values. Output slice hysteresis is used to provide dead-zone squelching.

* Author(s): Cedar Grove Studios

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

__repo__ = "https://github.com/CedarGroveStudios/Range_Slicer.git"

class Slicer:
    """range_slicer helper class."""

    def __init__(self, in_min=0, in_max=65535, out_min=0, out_max=65535,
                 slice=1.0, hyst_factor=0.25, out_integer=False, debug=False):
        # input parameters
        self._in_min = in_min
        self._in_max = in_max

        # output parameters
        self._out_min = out_min
        self._out_max = out_max

        # slice parameters
        self._slice = slice

        # hysteresis parameters
        self._hyst_factor = hyst_factor

        # output value data type parameters
        self._out_integer = out_integer

        # debug parameters
        self._debug = debug
        if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)

        self.param_updater() # Establish the parameters for range_slicer helper

    @property
    def range_min(self):
        """The range input's minimum floating or integer value.
           Default is 0."""
        return self._in_min

    @range_min.setter
    def range_min(self, in_min=0):
        self._in_min = in_min
        self.param_updater() # Update the parameters for range_slicer helper

    @property
    def range_max(self):
        """The range input's maximum floating or integer value.
           Default is 65535."""
        return self._in_max

    @range_max.setter
    def range_max(self, in_max=65535):
        self._in_max = in_max
        self.param_updater() # Update the parameters for range_slicer helper

    @property
    def index_min(self):
        """The index output minimum value. Default is 0."""
        return self._out_min

    @index_min.setter
    def index_min(self, out_min=0):
        self._out_min = out_min
        self.param_updater() # Update the parameters for range_slicer helper

    @property
    def index_max(self):
        """The index output maximum value. Default is 65535."""
        return self._out_max

    @index_max.setter
    def index_max(self, out_max=65535):
        self._out_max = out_max
        self.param_updater() # Update the parameters for range_slicer helper

    @property
    def index_type(self):
        """The index output value integer data type.
           Default is False (floating)."""
        return self._out_integer

    @index_type.setter
    def index_type(self, out_integer=False):
        self._out_integer = out_integer
        self.param_updater() # Update the parameters for range_slicer helper

    @property
    def slice(self):
        """The slice size value. Default is 1.0."""
        return self._slice

    @slice.setter
    def slice(self, size=1.0):
        if size == 0:
            raise RuntimeError("Invalid slice size; value cannot be zero")
        self._slice = size
        self.param_updater() # Update the parameters for range_slicer helper

    @property
    def hysteresis(self):
        """The hysteresis factor value. For example, a factor of 0.50 is a
        hysteresis setting of 50%. Default is 0.25"""
        return self._hyst_factor

    @hysteresis.setter
    def hysteresis(self, hyst_factor=0.25):
        self._hyst_factor = hyst_factor

    @property
    def debug(self):
        """The class debugging mode. Default is False."""
        return self._debug

    @debug.setter
    def debug(self, debug=False):
        self._debug = debug
        if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)

    def range_slicer(self, input=0):
        """Determines index output value from the range input value optionally
           truncated to an integer data type. Returns the new index value and
           a flag (True/False) indicating if the new index changed from the
           previous index value.
           This is the primary function of the Slicer class.
        """
        # map hysteresis-adjusted input and remove span minimum
        self._index_mapped = self.mapper(input - self._offset) - self._out_span_min
        # calculate the sequential slice number
        self._slice_number = ((self._index_mapped - (self._index_mapped % self._slice))
                              / self._slice)
        # quantize and add back the offset
        self._index = (self._slice_number * self._slice) + self._out_span_min
        print('*** _index_mapped, _index:', self._index_mapped, self._index)

        # Limit index value to within index span
        if self._out_min <= self._out_max:
            self._index = max(min(self._index, self._out_max), self._out_min)
        else:
            self._index = min(max(self._index, self._out_max), self._out_min)

        # this may need to be moved so that it doesn't mess with offset values
        """if self._out_integer:  # is the output value data type integer?
            self._index = int(self._index)"""

        if self._index != self._old_idx:  # did the index value change?
            self._offset = (self._hyst_factor * self.sign(input - self._old_input)
                            * self._in_span_dir * self._out_span_dir * self._in_offset)
            print('index change')

            # store index and input history values
            self._in_dir = self.sign(input - self._old_input)  # store input direction
            self._old_idx = self._index  # store index and input history values
            self._old_input = input


        else:
            # this is the section that detects input direction changes when the index value hasn't changed
            # wondering if it needs to capture the previous offset value and only calculate the new value when
            # the mapper index value satisfies the previous offset threshold.
            if self._in_dir != self.sign(input - self._old_input):
                print('input direction change: _in_dir, sign(input - _old_input):', self._in_dir, self.sign(input - self._old_input))
                print('input:', input, '_old_input:', self._old_input)

            self._offset = (self._hyst_factor * self.sign(input - self._old_input)
                            * self._in_span_dir * self._out_span_dir * self._in_offset)


            self._in_dir = self.sign(input - self._old_input)  # store input direction
            self._old_input = input  # store input history value


        if self._debug:
            print("***range_slicer ", self.__dict__)
        return self._index, False  # return index value and change flag

    def mapper(self, map_in):
        """Determines the index output value of the range input value.
           (A slightly modified version of
           Adafruit.CircuitPython.simpleio.map_range library.)
        """
        self._mapped = ((map_in - self._in_min) * (self._out_span_max - self._out_span_min)
                        / (self._in_max - self._in_min)) + self._out_span_min

        if self._out_span_min <= self._out_span_max:
            return max(min(self._mapped, self._out_span_max), self._out_span_min)
        else:
            return min(max(self._mapped, self._out_span_max), self._out_span_min)

    def sign(self, x):
        """Determines the sign of a numeric value. Zero is evaluated as a
           positive value.
        """
        if x >= 0:
            return 1
        else: return -1

    def param_updater(self):
        """ Establishes and updates parameters for the range_slicer function. """
        # input parameters
        self._in_span = (self._in_max - self._in_min)
        if self._in_span == 0:
            raise RuntimeError("Invalid Range (input) min/max setting; values cannot be equal")
        self._in_span_dir = self.sign(self._in_span)

        # output parameters
        if self._out_min > self._out_max:
            self._out_span_min = self._out_min + self._slice
            self._out_span_max = self._out_max
        else:
            self._out_span_min = self._out_min
            self._out_span_max = self._out_max + self._slice

        self._out_span = (self._out_span_max - self._out_span_min)
        if self._out_span == 0:
            raise RuntimeError("Invalid Index (output) min/max setting; values cannot be equal")
        self._out_span_dir = self.sign(self._out_span)

        # slice parameters
        self._slice_count = (int((self._out_span_max - self._out_span_min)
                             / self._slice)) + 1

        # hysteresis parameters
        #   none

        # output value data type parameters
        #   none

        # index and input parameters
        self._old_idx = 0
        self._old_input = 0
        self._in_dir = 0

        # offset parameters
        self._offset = 0
        self._in_offset = self._in_span / self._slice_count

        # debug parameters
        #   none

        return
