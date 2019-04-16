`cedargrove_rs_param_updater`
# ================================================================================
# cedargrove_rs_param_updater.py 2019-04-13 v24 09:10AM
# A CircuitPython helper for establishing and updating Range_Slicer parameters.

def param_updater():
    # input parameters
    self._in_span = (self._in_max - self._in_min)

    # output parameters
    self._out_span_min = min(self._out_min, self._out_max)
    self._out_span_max = max(self._out_max, self._out_min)
    self._out_span = abs(self._out_max - self._out_min)
    self._out_direction = self.sign(self._out_max - self._out_min)

    # slice parameters
    self._slice_count = (int(abs(self._out_span) / self._slice)) + 1

    # hysteresis parameters
    #   none

    # output value data type parameters
    #   none

    # index parameters
    self._old_idx = 0

    # offset parameters
    self._offset = 0
    self._in_offset = self._in_span / self._slice_count

    # debug parameters
    #   none

    return
