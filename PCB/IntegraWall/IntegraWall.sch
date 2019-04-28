EESchema Schematic File Version 4
LIBS:IntegraWall-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 5CC58F9C
P 2600 5650
F 0 "J1" H 2600 7128 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 2600 7037 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical" H 2600 5650 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 2600 5650 50  0001 C CNN
	1    2600 5650
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Weather_click
U 1 1 5CC59422
P 4400 2900
F 0 "Weather_click" H 4400 3565 50  0000 C CNN
F 1 "MikroBus" H 4400 3474 50  0000 C CNN
F 2 "" H 4400 3400 50  0001 C CNN
F 3 "" H 4400 3400 50  0001 C CNN
	1    4400 2900
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Air_quality_3_click
U 1 1 5CC59592
P 5750 2900
F 0 "Air_quality_3_click" H 5750 3565 50  0000 C CNN
F 1 "MikroBus" H 5750 3474 50  0000 C CNN
F 2 "" H 5750 3400 50  0001 C CNN
F 3 "" H 5750 3400 50  0001 C CNN
	1    5750 2900
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Spectral_click
U 1 1 5CC595E4
P 7050 2900
F 0 "Spectral_click" H 7050 3565 50  0000 C CNN
F 1 "MikroBus" H 7050 3474 50  0000 C CNN
F 2 "" H 7050 3400 50  0001 C CNN
F 3 "" H 7050 3400 50  0001 C CNN
	1    7050 2900
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Motion_click
U 1 1 5CC59640
P 8350 2900
F 0 "Motion_click" H 8350 3565 50  0000 C CNN
F 1 "MikroBus" H 8350 3474 50  0000 C CNN
F 2 "" H 8350 3400 50  0001 C CNN
F 3 "" H 8350 3400 50  0001 C CNN
	1    8350 2900
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR?
U 1 1 5CC588DA
P 2700 4150
F 0 "#PWR?" H 2700 4000 50  0001 C CNN
F 1 "+3V3" H 2715 4323 50  0000 C CNN
F 2 "" H 2700 4150 50  0001 C CNN
F 3 "" H 2700 4150 50  0001 C CNN
	1    2700 4150
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5CC5894F
P 2400 4150
F 0 "#PWR?" H 2400 4000 50  0001 C CNN
F 1 "+5V" H 2415 4323 50  0000 C CNN
F 2 "" H 2400 4150 50  0001 C CNN
F 3 "" H 2400 4150 50  0001 C CNN
	1    2400 4150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5CC589EB
P 2200 7150
F 0 "#PWR?" H 2200 6900 50  0001 C CNN
F 1 "GND" H 2205 6977 50  0000 C CNN
F 2 "" H 2200 7150 50  0001 C CNN
F 3 "" H 2200 7150 50  0001 C CNN
	1    2200 7150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 4350 2400 4150
Wire Wire Line
	2700 4350 2700 4150
Wire Wire Line
	2200 6950 2200 7150
$Comp
L power:+3V3 #PWR?
U 1 1 5CC58C05
P 3600 3550
F 0 "#PWR?" H 3600 3400 50  0001 C CNN
F 1 "+3V3" H 3615 3723 50  0000 C CNN
F 2 "" H 3600 3550 50  0001 C CNN
F 3 "" H 3600 3550 50  0001 C CNN
	1    3600 3550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5CC58C5D
P 3600 3650
F 0 "#PWR?" H 3600 3400 50  0001 C CNN
F 1 "GND" H 3605 3477 50  0000 C CNN
F 2 "" H 3600 3650 50  0001 C CNN
F 3 "" H 3600 3650 50  0001 C CNN
	1    3600 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 3550 3850 3550
Wire Wire Line
	7800 3550 7800 3150
Wire Wire Line
	7800 3150 7900 3150
Wire Wire Line
	7900 3250 7850 3250
Wire Wire Line
	7850 3250 7850 3650
Wire Wire Line
	7850 3650 6550 3650
Wire Wire Line
	3950 3150 3850 3150
Wire Wire Line
	3850 3150 3850 3550
Connection ~ 3850 3550
Wire Wire Line
	3850 3550 5200 3550
Wire Wire Line
	5300 3150 5200 3150
Wire Wire Line
	5200 3150 5200 3550
Connection ~ 5200 3550
Wire Wire Line
	5200 3550 6500 3550
Wire Wire Line
	6600 3150 6500 3150
Wire Wire Line
	6500 3150 6500 3550
Connection ~ 6500 3550
Wire Wire Line
	6500 3550 7800 3550
Wire Wire Line
	3950 3250 3900 3250
Wire Wire Line
	3900 3250 3900 3650
Connection ~ 3900 3650
Wire Wire Line
	3900 3650 3600 3650
Wire Wire Line
	5300 3250 5250 3250
Wire Wire Line
	5250 3250 5250 3650
Connection ~ 5250 3650
Wire Wire Line
	5250 3650 3900 3650
Wire Wire Line
	6600 3250 6550 3250
Wire Wire Line
	6550 3250 6550 3650
Connection ~ 6550 3650
Wire Wire Line
	6550 3650 5250 3650
Text GLabel 4150 3850 0    50   BiDi ~ 0
SCL
Text GLabel 4150 3950 0    50   Input ~ 0
SDA
Wire Wire Line
	3400 5050 3500 5050
Wire Wire Line
	3400 5150 3500 5150
Wire Wire Line
	4150 3850 4950 3850
Wire Wire Line
	7600 3850 7600 2950
Wire Wire Line
	7600 2950 7500 2950
Wire Wire Line
	7500 3050 7550 3050
Wire Wire Line
	7550 3050 7550 3950
Wire Wire Line
	7550 3950 6250 3950
Wire Wire Line
	6200 2950 6300 2950
Wire Wire Line
	6300 2950 6300 3850
Connection ~ 6300 3850
Wire Wire Line
	6300 3850 7600 3850
Wire Wire Line
	6200 3050 6250 3050
Wire Wire Line
	6250 3050 6250 3950
Connection ~ 6250 3950
Wire Wire Line
	6250 3950 4900 3950
Wire Wire Line
	4850 2950 4950 2950
Wire Wire Line
	4950 2950 4950 3850
Connection ~ 4950 3850
Wire Wire Line
	4950 3850 6300 3850
Wire Wire Line
	4850 3050 4900 3050
Wire Wire Line
	4900 3050 4900 3950
Connection ~ 4900 3950
Wire Wire Line
	4900 3950 4150 3950
$Comp
L power:+3V3 #PWR?
U 1 1 5CC5CC93
P 6450 2550
F 0 "#PWR?" H 6450 2400 50  0001 C CNN
F 1 "+3V3" H 6465 2723 50  0000 C CNN
F 2 "" H 6450 2550 50  0001 C CNN
F 3 "" H 6450 2550 50  0001 C CNN
	1    6450 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 2650 6450 2550
Wire Wire Line
	6450 2650 6600 2650
$Comp
L power:GND #PWR?
U 1 1 5CC5E2FE
P 6450 2800
F 0 "#PWR?" H 6450 2550 50  0001 C CNN
F 1 "GND" H 6455 2627 50  0000 C CNN
F 2 "" H 6450 2800 50  0001 C CNN
F 3 "" H 6450 2800 50  0001 C CNN
	1    6450 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 2800 6450 2750
Wire Wire Line
	6450 2750 6600 2750
$EndSCHEMATC
