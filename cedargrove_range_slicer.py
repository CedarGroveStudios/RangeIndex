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
Range_Slicer 2020-09-09 v30 06:13PM
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
        """if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)"""

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
        """if self._debug:
            print("*Init:", self.__class__)
            print("*Init: ", self.__dict__)"""


    # -------------------------------------------------------------------- #
    def range_slicer(self, input=0):
        """Determines index output value from the range input value optionally
           truncated to an integer data type. Returns the new index value and
           a flag (True/False) indicating if the new index changed from the
           previous index value.
           This is the primary function of the Slicer class.
        """

        self._hyst_band = self._hyst_factor * self._slice

        if self._debug:
            print()
            print('===== fixed values =====')
            print('_in_min :', self._in_min, '_in_max :', self._in_max)
            print('_out_min:', self._out_min, '_out_max:', self._out_max)
            print('_slice:', self._slice)
            print('_hyst_band:', self._hyst_band, '_hyst_factor:', self._hyst_factor)
            print()

        # map hysteresis-adjusted input and remove _out_min bias
        self._idx_mapped = self.mapper(input)
        # calculate the sequential slice number
        self._slice_num = ((self._idx_mapped - (self._idx_mapped % self._slice))
                              / self._slice)
        # quantize and add back the _out_min bias
        self._idx_quan = (self._slice_num * self._slice) + self._out_min

        if self._debug:
            print('--- mapped values ---')
            print('input:', input)
            print('_idx_mapped:', self._idx_mapped, '_idx_quan:', self._idx_quan)
            print('_slice_num:', self._slice_num)
            print()

            print('--- hysteresis band thresolds ---')
            print('_idx_quan:', self._idx_quan)
            print('upper threshold (_idx_quan + _hyst_band):', self._idx_quan + self._hyst_band)
            print('lower threshold (_idx_quan - _hyst_band):', self._idx_quan - self._hyst_band)
            print()

        if (self._idx_mapped < (self._idx_quan + self._hyst_band)) and (self._idx_mapped > (self._idx_quan - self._hyst_band)):
            if self._debug:
                print("_idx_mapped is between upper and lower _hyst_band thresholds for _idx_quan:", self._idx_quan)
                print("in the squelch zone: don't change index value")


            if (self._index != self._idx_quan) and (self._index != self._idx_quan - self._slice):
                print('big change')
                print('_index:', self._index, '_idx_mapped', self._idx_mapped, '_idx_quan', self._idx_quan)

            else:
                print('no big change')


            index_flag = False

        if self._idx_mapped >= self._idx_quan + self._hyst_band:
            if self._debug:
                print("_idx_mapped is greater than upper _hyst_band threshold")
                print("_idx_quan is the value to use:", self._idx_quan)

            if self._index == self._idx_quan:
                index_flag = False
            else:
                index_flag = True

            self._index = self._idx_quan

        if self._idx_mapped <= self._idx_quan - self._hyst_band:
            if self._debug:
                print("_idx_mapped is less than lower _hyst_band threshold")
                print("_idx_quan - _slice is the new value to use:", self._idx_quan - self._slice)

            if self._index == self._idx_quan:
                index_flag = False
            else:
                index_flag = True

            self._index = self._idx_quan - self._slice

        if self._idx_mapped >= self._out_max:
            self._index = self._out_max

        """while True:
            pass"""

        # Limit index value to within index span
        if self._out_min <= self._out_max:
            self._index = max(min(self._index, self._out_max), self._out_min)
        else:
            self._index = min(max(self._index, self._out_max), self._out_min)

        if self._debug:
            print()
            print(' returns:', self._index, index_flag)

        if self._out_integer:  # is the output value data type integer?
            return int(self._index), index_flag
        return self._index, index_flag


    # -------------------------------------------------------------------- #
    def mapper(self, map_in):
        """Determines the index output value of the range input value.
           (from Adafruit.CircuitPython.simpleio.map_range)
        """
        self._mapped = ((map_in - self._in_min) * (self._out_max - self._out_min)
                        / (self._in_max - self._in_min)) + self._out_min

        if self._out_min <= self._out_max:
            return max(min(self._mapped, self._out_max), self._out_min)
        else:
            return min(max(self._mapped, self._out_max), self._out_min)

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
        self._index = 0
        self._old_idx = 0
        self._old_input = 0
        self._in_dir = 0

        # offset parameters
        self._offset = 0
        self._in_offset = self._in_span / self._slice_count

        # debug parameters
        #   none

        return
