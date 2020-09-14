EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr USLetter 11000 8500
encoding utf-8
Sheet 1 1
Title "Schmitt Ladder"
Date "2020-09-14"
Rev "v00"
Comp "Cedar Grove Studios"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Amplifier_Operational:OPA2156xDGK U1
U 1 1 5F139E32
P 4850 1475
F 0 "U1" H 4825 1250 50  0000 L CNN
F 1 "OPA2156xDGK" H 4825 1325 50  0000 L CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 4850 1475 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 4850 1475 50  0001 C CNN
	1    4850 1475
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:OPA2156xDGK U1
U 2 1 5F13B033
P 4850 2475
F 0 "U1" H 4825 2250 50  0000 L CNN
F 1 "OPA2156xDGK" H 4825 2325 50  0000 L CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 4850 2475 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 4850 2475 50  0001 C CNN
	2    4850 2475
	1    0    0    1   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R3
U 1 1 5FC619EE
P 4300 1800
F 0 "R3" V 4375 1725 50  0000 L CNN
F 1 "100K" V 4450 1725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4300 1800 50  0001 C CNN
F 3 "" H 4300 1800 50  0001 C CNN
	1    4300 1800
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR02
U 1 1 5FC619FB
P 4100 1900
F 0 "#PWR02" H 4100 1650 50  0001 C CNN
F 1 "GND" H 4105 1727 50  0000 C CNN
F 2 "" H 4100 1900 50  0001 C CNN
F 3 "" H 4100 1900 50  0001 C CNN
	1    4100 1900
	1    0    0    -1  
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R4
U 1 1 5FC61A1D
P 4850 1800
F 0 "R4" V 4925 1725 50  0000 L CNN
F 1 "100K" V 5000 1725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4850 1800 50  0001 C CNN
F 3 "" H 4850 1800 50  0001 C CNN
	1    4850 1800
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 1800 4100 1800
Wire Wire Line
	4950 1800 5250 1800
Wire Wire Line
	5250 1800 5250 1475
Wire Wire Line
	5150 1475 5250 1475
Wire Wire Line
	4500 1575 4500 1800
Connection ~ 4500 1575
Wire Wire Line
	4500 1575 4550 1575
Wire Wire Line
	4500 1800 4750 1800
Wire Wire Line
	4400 1800 4500 1800
Connection ~ 4500 1800
Wire Wire Line
	4100 1900 4100 1800
Wire Wire Line
	3900 1575 4500 1575
Wire Wire Line
	4550 1375 3650 1375
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R6
U 1 1 5F6DF221
P 4300 2800
F 0 "R6" V 4375 2725 50  0000 L CNN
F 1 "100K" V 4450 2725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4300 2800 50  0001 C CNN
F 3 "" H 4300 2800 50  0001 C CNN
	1    4300 2800
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR03
U 1 1 5F6DF22B
P 4100 2900
F 0 "#PWR03" H 4100 2650 50  0001 C CNN
F 1 "GND" H 4105 2727 50  0000 C CNN
F 2 "" H 4100 2900 50  0001 C CNN
F 3 "" H 4100 2900 50  0001 C CNN
	1    4100 2900
	1    0    0    -1  
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R7
U 1 1 5F6DF235
P 4850 2800
F 0 "R7" V 4925 2725 50  0000 L CNN
F 1 "100K" V 5000 2725 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4850 2800 50  0001 C CNN
F 3 "" H 4850 2800 50  0001 C CNN
	1    4850 2800
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 2800 4100 2800
Wire Wire Line
	4950 2800 5250 2800
Wire Wire Line
	5250 2800 5250 2475
Wire Wire Line
	4500 2575 4500 2800
Wire Wire Line
	4500 2800 4750 2800
Wire Wire Line
	4400 2800 4500 2800
Connection ~ 4500 2800
Wire Wire Line
	4100 2900 4100 2800
Wire Wire Line
	3900 2575 4500 2575
Wire Wire Line
	4550 2375 3650 2375
Wire Wire Line
	4500 2575 4550 2575
Connection ~ 4500 2575
Wire Wire Line
	5150 2475 5250 2475
Wire Wire Line
	5250 2475 5400 2475
Connection ~ 5250 2475
Wire Wire Line
	5250 1475 5400 1475
Connection ~ 5250 1475
Wire Wire Line
	3900 2575 3900 2025
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R5
U 1 1 5F6E3ED6
P 3650 2800
F 0 "R5" H 3500 2750 50  0000 L CNN
F 1 "10K" H 3450 2825 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 3650 2800 50  0001 C CNN
F 3 "" H 3650 2800 50  0001 C CNN
	1    3650 2800
	-1   0    0    1   
$EndComp
Wire Wire Line
	3650 1375 3650 1700
Wire Wire Line
	3650 2900 3650 3400
Wire Wire Line
	3650 2375 3650 2700
$Comp
L Amplifier_Operational:OPA2156xDGK U2
U 1 1 5F6ECD8D
P 4850 3500
F 0 "U2" H 4825 3275 50  0000 L CNN
F 1 "OPA2156xDGK" H 4825 3350 50  0000 L CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 4850 3500 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 4850 3500 50  0001 C CNN
	1    4850 3500
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:OPA2156xDGK U2
U 2 1 5F6ECD97
P 4850 4500
F 0 "U2" H 4825 4275 50  0000 L CNN
F 1 "OPA2156xDGK" H 4825 4350 50  0000 L CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 4850 4500 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 4850 4500 50  0001 C CNN
	2    4850 4500
	1    0    0    1   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R9
U 1 1 5F6ECDA1
P 4300 3825
F 0 "R9" V 4375 3750 50  0000 L CNN
F 1 "100K" V 4450 3750 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4300 3825 50  0001 C CNN
F 3 "" H 4300 3825 50  0001 C CNN
	1    4300 3825
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR04
U 1 1 5F6ECDAB
P 4100 3925
F 0 "#PWR04" H 4100 3675 50  0001 C CNN
F 1 "GND" H 4105 3752 50  0000 C CNN
F 2 "" H 4100 3925 50  0001 C CNN
F 3 "" H 4100 3925 50  0001 C CNN
	1    4100 3925
	1    0    0    -1  
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R10
U 1 1 5F6ECDB5
P 4850 3825
F 0 "R10" V 4925 3750 50  0000 L CNN
F 1 "100K" V 5000 3750 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4850 3825 50  0001 C CNN
F 3 "" H 4850 3825 50  0001 C CNN
	1    4850 3825
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R8
U 1 1 5F6ECDBF
P 3650 3825
F 0 "R8" H 3500 3775 50  0000 L CNN
F 1 "10K" H 3450 3850 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 3650 3825 50  0001 C CNN
F 3 "" H 3650 3825 50  0001 C CNN
	1    3650 3825
	-1   0    0    1   
$EndComp
Wire Wire Line
	4200 3825 4100 3825
Wire Wire Line
	4950 3825 5250 3825
Wire Wire Line
	5250 3825 5250 3500
Wire Wire Line
	5150 3500 5250 3500
Wire Wire Line
	4500 3600 4500 3825
Connection ~ 4500 3600
Wire Wire Line
	4500 3600 4550 3600
Wire Wire Line
	4500 3825 4750 3825
Wire Wire Line
	4400 3825 4500 3825
Connection ~ 4500 3825
Wire Wire Line
	4100 3925 4100 3825
Wire Wire Line
	3900 3600 4500 3600
Wire Wire Line
	4550 3400 3650 3400
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R12
U 1 1 5F6ECDD6
P 4300 4825
F 0 "R12" V 4375 4750 50  0000 L CNN
F 1 "100K" V 4450 4750 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4300 4825 50  0001 C CNN
F 3 "" H 4300 4825 50  0001 C CNN
	1    4300 4825
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR05
U 1 1 5F6ECDE0
P 4100 4925
F 0 "#PWR05" H 4100 4675 50  0001 C CNN
F 1 "GND" H 4105 4752 50  0000 C CNN
F 2 "" H 4100 4925 50  0001 C CNN
F 3 "" H 4100 4925 50  0001 C CNN
	1    4100 4925
	1    0    0    -1  
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R13
U 1 1 5F6ECDEA
P 4850 4825
F 0 "R13" V 4925 4750 50  0000 L CNN
F 1 "100K" V 5000 4750 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4850 4825 50  0001 C CNN
F 3 "" H 4850 4825 50  0001 C CNN
	1    4850 4825
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 4825 4100 4825
Wire Wire Line
	4950 4825 5250 4825
Wire Wire Line
	5250 4825 5250 4500
Wire Wire Line
	4500 4600 4500 4825
Wire Wire Line
	4500 4825 4750 4825
Wire Wire Line
	4400 4825 4500 4825
Connection ~ 4500 4825
Wire Wire Line
	4100 4925 4100 4825
Wire Wire Line
	3900 4600 4500 4600
Wire Wire Line
	4550 4400 3650 4400
Wire Wire Line
	4500 4600 4550 4600
Connection ~ 4500 4600
Wire Wire Line
	5150 4500 5250 4500
Wire Wire Line
	5250 4500 5400 4500
Connection ~ 5250 4500
Wire Wire Line
	5250 3500 5400 3500
Connection ~ 5250 3500
Wire Wire Line
	3900 4600 3900 3600
Wire Wire Line
	3650 3400 3650 3725
Wire Wire Line
	3650 3925 3650 4400
Connection ~ 3650 4400
Connection ~ 3650 2375
Connection ~ 3650 3400
Wire Wire Line
	3650 4925 3650 5425
$Comp
L Amplifier_Operational:OPA2156xDGK U3
U 1 1 5F7058BC
P 4850 5525
F 0 "U3" H 4825 5300 50  0000 L CNN
F 1 "OPA2156xDGK" H 4825 5375 50  0000 L CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 4850 5525 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 4850 5525 50  0001 C CNN
	1    4850 5525
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:OPA2156xDGK U3
U 2 1 5F7058C6
P 4850 6525
F 0 "U3" H 4825 6300 50  0000 L CNN
F 1 "OPA2156xDGK" H 4825 6375 50  0000 L CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 4850 6525 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 4850 6525 50  0001 C CNN
	2    4850 6525
	1    0    0    1   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R15
U 1 1 5F7058D0
P 4300 5850
F 0 "R15" V 4375 5775 50  0000 L CNN
F 1 "100K" V 4450 5775 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4300 5850 50  0001 C CNN
F 3 "" H 4300 5850 50  0001 C CNN
	1    4300 5850
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR06
U 1 1 5F7058DA
P 4100 5950
F 0 "#PWR06" H 4100 5700 50  0001 C CNN
F 1 "GND" H 4105 5777 50  0000 C CNN
F 2 "" H 4100 5950 50  0001 C CNN
F 3 "" H 4100 5950 50  0001 C CNN
	1    4100 5950
	1    0    0    -1  
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R16
U 1 1 5F7058E4
P 4850 5850
F 0 "R16" V 4925 5775 50  0000 L CNN
F 1 "100K" V 5000 5775 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4850 5850 50  0001 C CNN
F 3 "" H 4850 5850 50  0001 C CNN
	1    4850 5850
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R14
U 1 1 5F7058EE
P 3650 5850
F 0 "R14" H 3600 5800 50  0000 R CNN
F 1 "10K" H 3600 5875 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 3650 5850 50  0001 C CNN
F 3 "" H 3650 5850 50  0001 C CNN
	1    3650 5850
	-1   0    0    1   
$EndComp
Wire Wire Line
	4200 5850 4100 5850
Wire Wire Line
	4950 5850 5250 5850
Wire Wire Line
	5250 5850 5250 5525
Wire Wire Line
	5150 5525 5250 5525
Wire Wire Line
	4500 5625 4500 5850
Connection ~ 4500 5625
Wire Wire Line
	4500 5625 4550 5625
Wire Wire Line
	4500 5850 4750 5850
Wire Wire Line
	4400 5850 4500 5850
Connection ~ 4500 5850
Wire Wire Line
	4100 5950 4100 5850
Wire Wire Line
	3900 5625 4500 5625
Wire Wire Line
	4550 5425 3650 5425
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R17
U 1 1 5F705905
P 4300 6850
F 0 "R17" V 4375 6775 50  0000 L CNN
F 1 "100K" V 4450 6775 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4300 6850 50  0001 C CNN
F 3 "" H 4300 6850 50  0001 C CNN
	1    4300 6850
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5F70590F
P 4100 6950
F 0 "#PWR08" H 4100 6700 50  0001 C CNN
F 1 "GND" H 4105 6777 50  0000 C CNN
F 2 "" H 4100 6950 50  0001 C CNN
F 3 "" H 4100 6950 50  0001 C CNN
	1    4100 6950
	1    0    0    -1  
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R18
U 1 1 5F705919
P 4850 6850
F 0 "R18" V 4925 6775 50  0000 L CNN
F 1 "100K" V 5000 6775 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4850 6850 50  0001 C CNN
F 3 "" H 4850 6850 50  0001 C CNN
	1    4850 6850
	0    1    1    0   
$EndComp
Wire Wire Line
	4200 6850 4100 6850
Wire Wire Line
	4950 6850 5250 6850
Wire Wire Line
	5250 6850 5250 6525
Wire Wire Line
	4500 6625 4500 6850
Wire Wire Line
	4500 6850 4750 6850
Wire Wire Line
	4400 6850 4500 6850
Connection ~ 4500 6850
Wire Wire Line
	4100 6950 4100 6850
Wire Wire Line
	3900 6625 4500 6625
Wire Wire Line
	4550 6425 3650 6425
Wire Wire Line
	4500 6625 4550 6625
Connection ~ 4500 6625
Wire Wire Line
	5150 6525 5250 6525
Wire Wire Line
	5250 6525 5400 6525
Connection ~ 5250 6525
Wire Wire Line
	5250 5525 5400 5525
Connection ~ 5250 5525
Wire Wire Line
	3900 6625 3900 5625
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R1
U 1 1 5F705935
P 3650 1175
F 0 "R1" H 3500 1125 50  0000 L CNN
F 1 "10K" H 3450 1200 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 3650 1175 50  0001 C CNN
F 3 "" H 3650 1175 50  0001 C CNN
	1    3650 1175
	-1   0    0    1   
$EndComp
Wire Wire Line
	3650 5425 3650 5750
Wire Wire Line
	3650 5950 3650 6425
Connection ~ 3650 6425
Connection ~ 3650 5425
$Comp
L power:+10V #PWR01
U 1 1 5F7A0E19
P 3650 975
F 0 "#PWR01" H 3650 825 50  0001 C CNN
F 1 "+10V" H 3665 1148 50  0000 C CNN
F 2 "" H 3650 975 50  0001 C CNN
F 3 "" H 3650 975 50  0001 C CNN
	1    3650 975 
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 1375 3650 1275
Connection ~ 3650 1375
Wire Wire Line
	3650 1075 3650 975 
$Comp
L power:GND #PWR07
U 1 1 5F7AFEE0
P 3650 6950
F 0 "#PWR07" H 3650 6700 50  0001 C CNN
F 1 "GND" H 3655 6777 50  0000 C CNN
F 2 "" H 3650 6950 50  0001 C CNN
F 3 "" H 3650 6950 50  0001 C CNN
	1    3650 6950
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 6425 3650 6950
Wire Wire Line
	3900 2025 3150 2025
Connection ~ 3900 2025
Wire Wire Line
	3900 2025 3900 1575
Text GLabel 3150 2025 0    50   Input ~ 0
INPUT
Text GLabel 5400 1475 2    50   Output ~ 0
SLICE_n
Text GLabel 5400 2475 2    50   Output ~ 0
SLICE_n-1
Text GLabel 5400 3500 2    50   Output ~ 0
SLICE_n-2
Text GLabel 5400 4500 2    50   Output ~ 0
SLICE_n-3
Text GLabel 5400 5525 2    50   Output ~ 0
SLICE_n-4
Wire Wire Line
	3650 1900 3650 2375
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R2
U 1 1 5F6CF316
P 3650 1800
F 0 "R2" H 3500 1750 50  0000 L CNN
F 1 "10K" H 3450 1825 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 3650 1800 50  0001 C CNN
F 3 "" H 3650 1800 50  0001 C CNN
	1    3650 1800
	-1   0    0    1   
$EndComp
Wire Wire Line
	3650 4400 3650 4725
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R11
U 1 1 5F6ECE06
P 3650 4825
F 0 "R11" H 3450 4775 50  0000 L CNN
F 1 "10K" H 3450 4850 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 3650 4825 50  0001 C CNN
F 3 "" H 3650 4825 50  0001 C CNN
	1    3650 4825
	-1   0    0    1   
$EndComp
Text GLabel 5400 6525 2    50   Output ~ 0
SLICE_0
Wire Wire Line
	3900 2575 3900 3600
Connection ~ 3900 2575
Connection ~ 3900 3600
Wire Wire Line
	3900 4600 3900 5625
Connection ~ 3900 4600
Connection ~ 3900 5625
$EndSCHEMATC
