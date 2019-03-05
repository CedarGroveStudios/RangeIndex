# Range_Slicer
## cedargrove_range_slicer
A CircuitPython class for scaling a range of input values into indexed/quantized output values. Output slice hysteresis is used to provide dead-zone squelching.
Range_Slicer is a general-purpose analog value converter that compresses or expands an input value then quantizes it into a collection of precise output slice values. The class detects input value changes and applies selectable hysteresis when slice edge thresholds are reached to eliminate dead-zone issues. Applications include converting rotary knob position to MIDI control or note values, analog signal noise processing, as well as level detection and display.

### Implementation Notes
#### Hardware:
#### Software and Dependencies:
•	Adafruit CircuitPython firmware for the supported boards: https://github.com/adafruit/circuitpython/releases

#### ```class cedargrove_range_slicer.Slicer(*, in_min=0, in_max=65535, out_min=0, out_max=65535, slice=1.0, hyst_factor=0.25, debug=False)```

Class representing the CedarGroveMaker Range_Slicer.

Parameters:	

-	`in_min` – The input range minimum. Can be any positive or negative value, smaller or larger than the input range maximum. Input range minimum and maximum values cannot be equal. Defaults to `0`.

-	`in_max` – The input range maximum. Can be any positive or negative value, smaller or larger than the input range minimum. Input range minimum and maximum values cannot be equal. Defaults to `65535`.

-	`out_min` – The output index minimum. Can be any positive or negative value, smaller or larger than the output index maximum. Output index minimum and maximum values cannot be equal. Defaults to `0`.

-	`out_max` – The output index minimum. Can be any positive or negative value, smaller or larger than the output index maximum. Output index minimum and maximum values cannot be equal. Defaults to `65535`.

-	`slice` – The size of an output index slice. Can be any positive or negative value other than zero. Defaults to `1.0`.

-	`hyst_factor` – The size of the hysteresis threshold expressed as a factor of the slice size. Can be a positive value from 0 to 1.0. Defaults to `0.25` (25% of the slice size value).

-	`debug` – Turn on debug printout. Defaults to `False`.

#### `range_slicer(input=0)`

Applies the slicer algorithm to an input value using the initialization parameters. Returns the output index value. This is the primary function of the Range_Slicer class.

Parameters:	

- `input` – The input value to convert. Can be any positive or negative numeric value. Defaults to `0`.


#### `range(min=0, max=65535)` 

Changes the default input range to new values.

Parameters:	

- `min` – The input range minimum. Can be any positive or negative value, smaller or larger than the input range maximum. Input range minimum and maximum values cannot be equal. Defaults to `0`.

- `max` – The input range maximum. Can be any positive or negative value, smaller or larger than the input range minimum. Input range minimum and maximum values cannot be equal. Defaults to `65535`.


#### `index(min=0, max=65535)` 

Changes the default output index to new values.

Parameters:	

- `min` – The index output minimum. Can be any positive or negative value, smaller or larger than the output index maximum. Output index minimum and maximum values cannot be equal. Defaults to `0`.

- `max` – The output index maximum. Can be any positive or negative value, smaller or larger than the output index minimum. Output index minimum and maximum values cannot be equal. Defaults to `65535`.


#### `slice(size=1.0)` 

Changes the default slice size to a new value.

Parameters:	

- `slice` – The size of an index output slice. Can be any positive or negative value other than zero. Defaults to `1.0`.


#### `hysteresis(hyst_factor=0.25)`

Changes the default hysteresis threshold to a new value.

Parameters:	

- `hyst_factor` – The size of the hysteresis threshold expressed as a factor of the slice size. Can be a positive value from 0 to 1.0. Defaults to `0.25` (25% of the slice size value).







________________________________________
© Copyright 2019 Cedar Grove Studios, Revision v01. 
