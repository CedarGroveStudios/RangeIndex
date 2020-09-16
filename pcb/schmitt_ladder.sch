EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr USLetter 11000 8500
encoding utf-8
Sheet 1 1
Title "Analog Schmitt Quantizer"
Date "2020-09-15"
Rev "v00"
Comp "Cedar Grove Studios"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R6
U 1 1 5F6DF221
P 4575 2175
F 0 "R6" V 4650 2100 50  0000 L CNN
F 1 "100K" V 4725 2100 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4575 2175 50  0001 C CNN
F 3 "" H 4575 2175 50  0001 C CNN
	1    4575 2175
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R10
U 1 1 5F6DF235
P 5200 2400
F 0 "R10" V 5275 2325 50  0000 L CNN
F 1 "100K" V 5350 2325 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5200 2400 50  0001 C CNN
F 3 "" H 5200 2400 50  0001 C CNN
	1    5200 2400
	0    1    1    0   
$EndComp
Wire Wire Line
	5300 2400 5600 2400
Wire Wire Line
	5600 2400 5600 2075
Wire Wire Line
	4850 2175 4850 2400
Wire Wire Line
	4850 2400 5100 2400
Wire Wire Line
	4675 2175 4850 2175
Wire Wire Line
	4900 1975 4000 1975
Wire Wire Line
	4850 2175 4900 2175
Wire Wire Line
	5500 2075 5600 2075
Connection ~ 5600 2075
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R2
U 1 1 5F6E3ED6
P 4000 2400
F 0 "R2" H 3850 2350 50  0000 L CNN
F 1 "1K" H 3850 2425 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4000 2400 50  0001 C CNN
F 3 "" H 4000 2400 50  0001 C CNN
	1    4000 2400
	-1   0    0    1   
$EndComp
Wire Wire Line
	4000 2500 4000 3000
Wire Wire Line
	4000 1975 4000 2300
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R7
U 1 1 5F6ECDA1
P 4575 3200
F 0 "R7" V 4650 3125 50  0000 L CNN
F 1 "100K" V 4725 3125 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4575 3200 50  0001 C CNN
F 3 "" H 4575 3200 50  0001 C CNN
	1    4575 3200
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R11
U 1 1 5F6ECDB5
P 5200 3425
F 0 "R11" V 5275 3350 50  0000 L CNN
F 1 "100K" V 5350 3350 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5200 3425 50  0001 C CNN
F 3 "" H 5200 3425 50  0001 C CNN
	1    5200 3425
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R3
U 1 1 5F6ECDBF
P 4000 3425
F 0 "R3" H 3850 3375 50  0000 L CNN
F 1 "1K" H 3850 3450 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4000 3425 50  0001 C CNN
F 3 "" H 4000 3425 50  0001 C CNN
	1    4000 3425
	-1   0    0    1   
$EndComp
Wire Wire Line
	5300 3425 5600 3425
Wire Wire Line
	5600 3425 5600 3100
Wire Wire Line
	5500 3100 5600 3100
Wire Wire Line
	4850 3200 4850 3425
Wire Wire Line
	4850 3200 4900 3200
Wire Wire Line
	4850 3425 5100 3425
Wire Wire Line
	4900 3000 4000 3000
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R8
U 1 1 5F6ECDD6
P 4575 4200
F 0 "R8" V 4650 4125 50  0000 L CNN
F 1 "100K" V 4725 4125 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4575 4200 50  0001 C CNN
F 3 "" H 4575 4200 50  0001 C CNN
	1    4575 4200
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R12
U 1 1 5F6ECDEA
P 5200 4425
F 0 "R12" V 5275 4350 50  0000 L CNN
F 1 "100K" V 5350 4350 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5200 4425 50  0001 C CNN
F 3 "" H 5200 4425 50  0001 C CNN
	1    5200 4425
	0    1    1    0   
$EndComp
Wire Wire Line
	5300 4425 5600 4425
Wire Wire Line
	5600 4425 5600 4100
Wire Wire Line
	4850 4200 4850 4425
Wire Wire Line
	4850 4425 5100 4425
Wire Wire Line
	4900 4000 4000 4000
Wire Wire Line
	4850 4200 4900 4200
Wire Wire Line
	5500 4100 5600 4100
Connection ~ 5600 4100
Connection ~ 5600 3100
Wire Wire Line
	4000 3000 4000 3325
Wire Wire Line
	4000 3525 4000 4000
Connection ~ 4000 4000
Connection ~ 4000 3000
Wire Wire Line
	4000 4525 4000 5025
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R9
U 1 1 5F7058D0
P 4575 5225
F 0 "R9" V 4650 5150 50  0000 L CNN
F 1 "100K" V 4725 5150 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4575 5225 50  0001 C CNN
F 3 "" H 4575 5225 50  0001 C CNN
	1    4575 5225
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R13
U 1 1 5F7058E4
P 5200 5450
F 0 "R13" V 5275 5375 50  0000 L CNN
F 1 "100K" V 5350 5375 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5200 5450 50  0001 C CNN
F 3 "" H 5200 5450 50  0001 C CNN
	1    5200 5450
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R5
U 1 1 5F7058EE
P 4000 5450
F 0 "R5" H 3950 5400 50  0000 R CNN
F 1 "1K" H 3950 5475 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4000 5450 50  0001 C CNN
F 3 "" H 4000 5450 50  0001 C CNN
	1    4000 5450
	-1   0    0    1   
$EndComp
Wire Wire Line
	5300 5450 5600 5450
Wire Wire Line
	5600 5450 5600 5125
Wire Wire Line
	5500 5125 5600 5125
Wire Wire Line
	4850 5225 4850 5450
Wire Wire Line
	4850 5225 4900 5225
Wire Wire Line
	4850 5450 5100 5450
Wire Wire Line
	4900 5025 4000 5025
Connection ~ 5600 5125
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R1
U 1 1 5F705935
P 4000 1625
F 0 "R1" H 3850 1575 50  0000 L CNN
F 1 "1K" H 3850 1650 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4000 1625 50  0001 C CNN
F 3 "" H 4000 1625 50  0001 C CNN
	1    4000 1625
	-1   0    0    1   
$EndComp
Wire Wire Line
	4000 5025 4000 5350
Connection ~ 4000 5025
$Comp
L power:+10V #PWR03
U 1 1 5F7A0E19
P 4000 1425
F 0 "#PWR03" H 4000 1275 50  0001 C CNN
F 1 "+10V" H 4015 1598 50  0000 C CNN
F 2 "" H 4000 1425 50  0001 C CNN
F 3 "" H 4000 1425 50  0001 C CNN
	1    4000 1425
	1    0    0    -1  
$EndComp
Wire Wire Line
	4000 1525 4000 1425
$Comp
L power:GND #PWR04
U 1 1 5F7AFEE0
P 4000 5850
F 0 "#PWR04" H 4000 5600 50  0001 C CNN
F 1 "GND" H 4005 5677 50  0000 C CNN
F 2 "" H 4000 5850 50  0001 C CNN
F 3 "" H 4000 5850 50  0001 C CNN
	1    4000 5850
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 2175 3450 2175
Text GLabel 1750 2275 0    50   Input ~ 0
INPUT
Text GLabel 9225 1975 2    50   Output ~ 0
OUTPUT
Wire Wire Line
	4000 4000 4000 4325
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R4
U 1 1 5F6ECE06
P 4000 4425
F 0 "R4" H 3850 4375 50  0000 L CNN
F 1 "1K" H 3850 4450 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 4000 4425 50  0001 C CNN
F 3 "" H 4000 4425 50  0001 C CNN
	1    4000 4425
	-1   0    0    1   
$EndComp
$Comp
L Comparator:LM339 U2
U 1 1 5F61B10D
P 5200 5125
F 0 "U2" H 5300 4925 50  0000 C CNN
F 1 "LM339" H 5350 5000 50  0000 C CNN
F 2 "" H 5150 5225 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/lm139.pdf" H 5250 5325 50  0001 C CNN
	1    5200 5125
	1    0    0    1   
$EndComp
$Comp
L Comparator:LM339 U2
U 2 1 5F61BF6E
P 5200 4100
F 0 "U2" H 5300 3900 50  0000 C CNN
F 1 "LM339" H 5350 3975 50  0000 C CNN
F 2 "" H 5150 4200 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/lm139.pdf" H 5250 4300 50  0001 C CNN
	2    5200 4100
	1    0    0    1   
$EndComp
$Comp
L Comparator:LM339 U2
U 3 1 5F61CAE4
P 5200 3100
F 0 "U2" H 5275 2900 50  0000 C CNN
F 1 "LM339" H 5325 2975 50  0000 C CNN
F 2 "" H 5150 3200 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/lm139.pdf" H 5250 3300 50  0001 C CNN
	3    5200 3100
	1    0    0    1   
$EndComp
$Comp
L Comparator:LM339 U2
U 4 1 5F61E14E
P 5200 2075
F 0 "U2" H 5275 1875 50  0000 C CNN
F 1 "LM339" H 5325 1950 50  0000 C CNN
F 2 "" H 5150 2175 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/lm139.pdf" H 5250 2275 50  0001 C CNN
	4    5200 2075
	1    0    0    1   
$EndComp
$Comp
L Comparator:LM339 U2
U 5 1 5F61F42E
P 2125 7200
F 0 "U2" H 2083 7246 50  0000 L CNN
F 1 "LM339" H 2083 7155 50  0000 L CNN
F 2 "" H 2075 7300 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/lm139.pdf" H 2175 7400 50  0001 C CNN
	5    2125 7200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4000 5850 4000 5550
Wire Wire Line
	4000 1975 4000 1725
Connection ~ 4000 1975
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R16
U 1 1 5F64D1F4
P 5600 3850
F 0 "R16" H 5400 3800 50  0000 L CNN
F 1 "1K" H 5450 3875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5600 3850 50  0001 C CNN
F 3 "" H 5600 3850 50  0001 C CNN
	1    5600 3850
	-1   0    0    1   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R17
U 1 1 5F64E3D3
P 5600 4875
F 0 "R17" H 5400 4825 50  0000 L CNN
F 1 "1K" H 5450 4900 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5600 4875 50  0001 C CNN
F 3 "" H 5600 4875 50  0001 C CNN
	1    5600 4875
	-1   0    0    1   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R15
U 1 1 5F64FEE5
P 5600 2850
F 0 "R15" H 5400 2800 50  0000 L CNN
F 1 "1K" H 5450 2875 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5600 2850 50  0001 C CNN
F 3 "" H 5600 2850 50  0001 C CNN
	1    5600 2850
	-1   0    0    1   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R14
U 1 1 5F650EEA
P 5600 1825
F 0 "R14" H 5400 1775 50  0000 L CNN
F 1 "1K" H 5450 1850 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 5600 1825 50  0001 C CNN
F 3 "" H 5600 1825 50  0001 C CNN
	1    5600 1825
	-1   0    0    1   
$EndComp
$Comp
L Reference_Voltage:LM4125IM5-2.0 U3
U 1 1 5F6524A2
P 2700 7175
F 0 "U3" H 3025 7075 50  0000 R CNN
F 1 "LM4125IM5-2.0" H 3525 7000 50  0000 R CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5" H 2700 6925 50  0001 L CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm4125.pdf" H 2700 7175 50  0001 C CIN
	1    2700 7175
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 5F65970F
P 2025 7600
F 0 "#PWR02" H 2025 7350 50  0001 C CNN
F 1 "GND" H 2030 7427 50  0000 C CNN
F 2 "" H 2025 7600 50  0001 C CNN
F 3 "" H 2025 7600 50  0001 C CNN
	1    2025 7600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2025 7600 2025 7550
Wire Wire Line
	2700 7475 2700 7550
Connection ~ 2025 7550
Wire Wire Line
	2025 7550 2025 7500
Wire Wire Line
	2025 6900 2025 6800
Wire Wire Line
	2700 6800 2700 6875
$Comp
L power:+10V #PWR01
U 1 1 5F667346
P 2025 6700
F 0 "#PWR01" H 2025 6550 50  0001 C CNN
F 1 "+10V" H 2040 6873 50  0000 C CNN
F 2 "" H 2025 6700 50  0001 C CNN
F 3 "" H 2025 6700 50  0001 C CNN
	1    2025 6700
	1    0    0    -1  
$EndComp
Wire Wire Line
	2025 6700 2025 6800
Text Label 3475 7175 2    50   ~ 0
2vREF
Wire Wire Line
	3000 7175 3475 7175
Text Label 5925 1400 2    50   ~ 0
2vREF
Wire Wire Line
	5600 1725 5600 1600
Wire Wire Line
	5600 1600 5925 1600
Wire Wire Line
	5600 2750 5600 2625
Wire Wire Line
	5600 2625 5925 2625
Wire Wire Line
	5600 3750 5600 3625
Wire Wire Line
	5600 3625 5925 3625
Wire Wire Line
	5600 4775 5600 4650
Wire Wire Line
	5600 4650 5925 4650
Wire Wire Line
	5600 5125 5600 4975
Wire Wire Line
	5600 4100 5600 3950
Wire Wire Line
	5600 3100 5600 2950
Wire Wire Line
	5600 2075 5600 1925
Wire Wire Line
	5925 1400 5925 1600
Wire Wire Line
	5925 1600 5925 2625
Connection ~ 5925 1600
Wire Wire Line
	5925 2625 5925 3625
Connection ~ 5925 2625
Connection ~ 5925 3625
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R19
U 1 1 5F69BE8E
P 6675 3100
F 0 "R19" V 6750 3025 50  0000 L CNN
F 1 "100K" V 6825 3025 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 6675 3100 50  0001 C CNN
F 3 "" H 6675 3100 50  0001 C CNN
	1    6675 3100
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R18
U 1 1 5F69EA42
P 6675 2075
F 0 "R18" V 6750 2000 50  0000 L CNN
F 1 "100K" V 6825 2000 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 6675 2075 50  0001 C CNN
F 3 "" H 6675 2075 50  0001 C CNN
	1    6675 2075
	0    1    1    0   
$EndComp
Wire Wire Line
	5925 3625 5925 4650
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R20
U 1 1 5F699169
P 6675 4100
F 0 "R20" V 6750 4025 50  0000 L CNN
F 1 "100K" V 6825 4025 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 6675 4100 50  0001 C CNN
F 3 "" H 6675 4100 50  0001 C CNN
	1    6675 4100
	0    1    1    0   
$EndComp
$Comp
L schmitt_ladder-rescue:R_Small-device-2019-04-06_Range_Slicer_PCB-rescue-Range_Slicer_PCB-rescue R21
U 1 1 5F68E3AE
P 6675 5125
F 0 "R21" V 6750 5050 50  0000 L CNN
F 1 "100K" V 6825 5050 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric" H 6675 5125 50  0001 C CNN
F 3 "" H 6675 5125 50  0001 C CNN
	1    6675 5125
	0    1    1    0   
$EndComp
$Comp
L Amplifier_Operational:OPA2156xDGK U1
U 2 1 5F6CA994
P 8125 1975
F 0 "U1" H 8225 1775 50  0000 C CNN
F 1 "OPA2156xDGK" H 8425 1850 50  0000 C CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 8125 1975 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 8125 1975 50  0001 C CNN
	2    8125 1975
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:OPA2156xDGK U1
U 1 1 5F6CB2DC
P 2825 2175
F 0 "U1" H 2925 1975 50  0000 C CNN
F 1 "OPA2156xDGK" H 3125 2050 50  0000 C CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 2825 2175 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 2825 2175 50  0001 C CNN
	1    2825 2175
	1    0    0    1   
$EndComp
$Comp
L Amplifier_Operational:OPA2156xDGK U1
U 3 1 5F6CC200
P 1450 7200
F 0 "U1" H 1408 7246 50  0000 L CNN
F 1 "OPA2156xDGK" H 1408 7155 50  0000 L CNN
F 2 "Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm" H 1450 7200 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/opa2156.pdf" H 1450 7200 50  0001 C CNN
	3    1450 7200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1350 6900 1350 6800
Wire Wire Line
	1350 6800 2025 6800
Connection ~ 2025 6800
Wire Wire Line
	1350 7500 1350 7550
Wire Wire Line
	1350 7550 2025 7550
Wire Wire Line
	8425 1975 8750 1975
Wire Wire Line
	7825 1875 7700 1875
Wire Wire Line
	7700 1875 7700 1575
Wire Wire Line
	7700 1575 8750 1575
Wire Wire Line
	8750 1575 8750 1975
Wire Wire Line
	2400 1775 3450 1775
Wire Wire Line
	3450 1775 3450 2175
Wire Wire Line
	2525 2075 2400 2075
Wire Wire Line
	2400 2075 2400 1775
Connection ~ 3450 2175
Wire Wire Line
	3450 2175 3125 2175
Wire Wire Line
	2525 2275 1750 2275
Text Label 6350 5125 2    50   ~ 0
SLICE_1
Wire Wire Line
	7225 5125 7225 4100
Wire Wire Line
	6775 5125 7225 5125
Connection ~ 7225 2075
Wire Wire Line
	7225 2075 7825 2075
Wire Wire Line
	6775 2075 7225 2075
Wire Wire Line
	6775 3100 7225 3100
Connection ~ 7225 3100
Wire Wire Line
	7225 3100 7225 2075
Wire Wire Line
	6775 4100 7225 4100
Connection ~ 7225 4100
Wire Wire Line
	7225 4100 7225 3100
Text Label 6350 4100 2    50   ~ 0
SLICE_2
Text Label 6350 3100 2    50   ~ 0
SLICE_3
Text Label 7225 2075 0    50   ~ 0
SLICE_SUM
Text Label 6350 2075 2    50   ~ 0
SLICE_4
Wire Wire Line
	5600 2075 6575 2075
Wire Wire Line
	5600 3100 6575 3100
Wire Wire Line
	5600 4100 6575 4100
Wire Wire Line
	5600 5125 6575 5125
Wire Wire Line
	2025 6800 2700 6800
Wire Wire Line
	2025 7550 2700 7550
Wire Wire Line
	8750 1975 9225 1975
Connection ~ 8750 1975
Connection ~ 4850 2175
Wire Wire Line
	4250 2175 4475 2175
Connection ~ 4250 2175
Wire Wire Line
	4250 2175 4250 3200
Wire Wire Line
	4675 3200 4850 3200
Connection ~ 4850 3200
Wire Wire Line
	4475 3200 4250 3200
Connection ~ 4250 3200
Wire Wire Line
	4250 3200 4250 4200
Wire Wire Line
	4675 4200 4850 4200
Connection ~ 4850 4200
Wire Wire Line
	4250 4200 4475 4200
Connection ~ 4250 4200
Wire Wire Line
	4250 4200 4250 5225
Wire Wire Line
	4675 5225 4850 5225
Connection ~ 4850 5225
Wire Wire Line
	4250 5225 4475 5225
$EndSCHEMATC
