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
Range_Slicer 2020-09-15 v40 11:17AM
A CircuitPython class for scaling a range of input values into indexed/quantized
output values. Output slice hysteresis is used to provide dead-zone squelching.

* Author(s): Cedar Grove Studios

Implementation Notes
--------------------
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

        # output slice parameter
        self._slice = slice

        # hysteresis parameter
        self._hyst_factor = hyst_factor

        # output value data type parameter
        self._out_integer = out_integer

        # debug parameter
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
        if size <= 0:
            raise RuntimeError("Invalid Slice setting; value must be greater than zero")
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


    def range_slicer(self, input=0):
        """Determines an index (output) value from the input value. Returns new
           index value and a change flag (True/False) if the new index changed
           from the previous index. Index value can be optionally converted to
           integer data type.
           This is the primary function of the Slicer class. """

        # calculate hysteresis band size
        self._hyst_band = self._hyst_factor * self._slice
        #print('hyst_band:', self._hyst_band)
        # map hysteresis-adjusted input and add hysteresis bias
        self._idx_mapped = self.mapper(input) + self._hyst_band
        # calculate the sequential slice number (*** subtract out_min? ***)
        self._slice_num = (((self._idx_mapped - self._out_min) - ((self._idx_mapped - self._out_min) % self._slice))
                              / self._slice)
        print('slice number:', self._slice_num)
        # quantize and add back the _out_min bias to calculate slice_threshold  (*** see above ***)
        self._slice_thresh = (self._slice_num * self._slice) + self._out_min
        #print('mapped + bias:', self._idx_mapped, 'slice threshold:', self._slice_thresh)

        self._upper_zone_limit = self._slice_thresh + (2 * self._hyst_band)

        # test to see if value is in the current hysteresis zone ("in-zone") and coming from outside
        #print('zone thresholds  upper:', self._upper_zone_limit, 'lower:', self._slice_thresh)
        if (self._idx_mapped <= self._upper_zone_limit and self._idx_mapped >= self._slice_thresh):
            if self._in_zone != self._slice_thresh:  # if not from the current hysteresis zone
                self._in_zone = self._slice_thresh  # toggle in_zone "on"
                #print('in_zone:', self._in_zone)

                # if value is increasing
                if self._idx_mapped > self._old_idx_mapped:
                    self._index = self._slice_thresh

                if self._idx_mapped < self._old_idx_mapped:
                    self._index = self._slice_thresh - self._slice

        else:
            self._in_zone = None  # toggle in_zone "off"
            #print('in_zone:', self._in_zone)
            self._index = self._slice_thresh

        #if mapped value is greater than or equal to the output maximum, set index to maximum
        # *** subtract hysteresis bias from _idx_mapped first? ***
        if self._idx_mapped >= self._out_max:
            self._index = self._out_max

        # Limit index value to within index span (is this needed?)
        if self._out_min <= self._out_max:
            self._index = max(min(self._index, self._out_max), self._out_min)
        else:
            self._index = min(max(self._index, self._out_max), self._out_min)

        self._old_idx_mapped = self._idx_mapped  # save for next cycle

        if self._out_integer:  # is the output value data type integer?
            return int(self._index), False
        return self._index, False

    def mapper(self, map_in):
        """Determines the output value based on the input value.
           (from Adafruit.CircuitPython.simpleio.map_range)  """

        if (self._in_min == self._in_max) or (self._out_min == self._out_max):
            return self._out_min

        self._mapped = ((map_in - self._in_min) * (self._out_max - self._out_min)
                        / (self._in_max - self._in_min)) + self._out_min

        if self._out_min <= self._out_max:
            return max(min(self._mapped, self._out_max), self._out_min)
        else:
            return min(max(self._mapped, self._out_max), self._out_min)

    def sign(self, x):
        """Determines the sign of a numeric value. Zero is evaluated as a
           positive value.  """
        if x >= 0:
            return 1
        else: return -1

    def param_updater(self):
        """ Establishes and updates parameters for the range_slicer function. """

        # input parameters
        self._in_span = (self._in_max - self._in_min)
        self._in_span_dir = self.sign(self._in_span)

        # output parameters
        if self._out_min > self._out_max:
            self._out_span_min = self._out_min + self._slice
            self._out_span_max = self._out_max
        else:
            self._out_span_min = self._out_min
            self._out_span_max = self._out_max + self._slice

        self._out_span = (self._out_span_max - self._out_span_min)
        self._out_span_dir = self.sign(self._out_span)

        # slice parameters
        if self._slice <= 0:
            raise RuntimeError("Invalid Slice setting; value must be greater than zero")
        self._slice_count = (int((self._out_span_max - self._out_span_min)
                             / self._slice)) + 1

        # hysteresis parameters
        #   calculate output hysteresis band value based on slice size

        # output value data type parameters
        #   none

        # index and input parameters
        self._index = 0
        self._old_idx = 0
        self._old_input = 0
        self._in_dir = 0
        self._old_idx_mapped = 0
        self._slice_thresh = None
        self._in_zone = None

        # offset parameters
        self._offset = 0
        self._in_offset = self._in_span / self._slice_count

        return
