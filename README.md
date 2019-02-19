# RangeIndex
A CircuitPython helper for scaling input values with hyseresis added to control noise. UNTESTED

# test of range_index library (class)
import cedargrove_range_index as ri

# instantiate range_index classes
key_49 = ri.range_index(0, 4096, 0, 49, hyst_factor=0.5, debug=False)
key_88 = ri.range_index(0, 4096, 0, 88, hyst_factor=0.2, debug=False)
cv_128 = ri.range_index(0, 4096, 0, 10, hyst_factor=0.5, debug=False)

# initialize variables for each instance
idx_kb_0, offset_kb_0, flag_kb_0 = key_49.range_index(0, 0, 0)
idx_kb_1, offset_kb_1, flag_kb_1 = key_88.range_index(0, 0, 0)
idx_cv_0, offset_cv_0, flag_cv_0 = cv_128.range_index(0, 0, 0)

# set new range, index, and hysteresis values for the cv_128 instance
cv_128.range = (0, 4000)
cv_128.index = (0, 11)
cv_128.hysteresis = 0.5

# calculate the index an offset values the value x within the cv_128 instance
idx_cv_0, offset_cv_0, flag_cv_0 = cv_128.range_index(x, idx_cv_0, offset_cv_0)
