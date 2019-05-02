EESchema Schematic File Version 4
LIBS:IntegraWall-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Integra wall sensor and LED board"
Date "2019-04-28"
Rev "0.1"
Comp "Nemanja Filipovic"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Raspberry_Pi_2_3 J2
U 1 1 5CC58F9C
P 1700 2500
F 0 "J2" H 1700 3978 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 1700 3887 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical" H 1700 2500 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 1700 2500 50  0001 C CNN
	1    1700 2500
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Weather_click1
U 1 1 5CC59422
P 4850 1400
F 0 "Weather_click1" H 4850 2065 50  0000 C CNN
F 1 "MikroBus" H 4850 1974 50  0000 C CNN
F 2 "Click_boards:Click_board" H 4850 1900 50  0001 C CNN
F 3 "" H 4850 1900 50  0001 C CNN
	1    4850 1400
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Air_quality_3_click1
U 1 1 5CC59592
P 6200 1400
F 0 "Air_quality_3_click1" H 6200 2065 50  0000 C CNN
F 1 "MikroBus" H 6200 1974 50  0000 C CNN
F 2 "Click_boards:Air_quality_click" H 6200 1900 50  0001 C CNN
F 3 "" H 6200 1900 50  0001 C CNN
	1    6200 1400
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Spectral_click1
U 1 1 5CC595E4
P 7500 1400
F 0 "Spectral_click1" H 7500 2065 50  0000 C CNN
F 1 "MikroBus" H 7500 1974 50  0000 C CNN
F 2 "Click_boards:Spectral_click" H 7500 1900 50  0001 C CNN
F 3 "" H 7500 1900 50  0001 C CNN
	1    7500 1400
	1    0    0    -1  
$EndComp
$Comp
L ClickBoards:MikroBus Motion_click1
U 1 1 5CC59640
P 8800 1400
F 0 "Motion_click1" H 8800 2065 50  0000 C CNN
F 1 "MikroBus" H 8800 1974 50  0000 C CNN
F 2 "Click_boards:Click_board" H 8800 1900 50  0001 C CNN
F 3 "" H 8800 1900 50  0001 C CNN
	1    8800 1400
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR02
U 1 1 5CC588DA
P 1800 1000
F 0 "#PWR02" H 1800 850 50  0001 C CNN
F 1 "+3V3" H 1815 1173 50  0000 C CNN
F 2 "" H 1800 1000 50  0001 C CNN
F 3 "" H 1800 1000 50  0001 C CNN
	1    1800 1000
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR01
U 1 1 5CC5894F
P 1500 1000
F 0 "#PWR01" H 1500 850 50  0001 C CNN
F 1 "+5V" H 1515 1173 50  0000 C CNN
F 2 "" H 1500 1000 50  0001 C CNN
F 3 "" H 1500 1000 50  0001 C CNN
	1    1500 1000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR011
U 1 1 5CC589EB
P 1300 4000
F 0 "#PWR011" H 1300 3750 50  0001 C CNN
F 1 "GND" H 1305 3827 50  0000 C CNN
F 2 "" H 1300 4000 50  0001 C CNN
F 3 "" H 1300 4000 50  0001 C CNN
	1    1300 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 1200 1500 1000
Wire Wire Line
	1800 1200 1800 1000
Wire Wire Line
	1300 3800 1300 4000
$Comp
L power:+3V3 #PWR07
U 1 1 5CC58C05
P 4050 2050
F 0 "#PWR07" H 4050 1900 50  0001 C CNN
F 1 "+3V3" H 4065 2223 50  0000 C CNN
F 2 "" H 4050 2050 50  0001 C CNN
F 3 "" H 4050 2050 50  0001 C CNN
	1    4050 2050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5CC58C5D
P 4050 2150
F 0 "#PWR08" H 4050 1900 50  0001 C CNN
F 1 "GND" H 4055 1977 50  0000 C CNN
F 2 "" H 4050 2150 50  0001 C CNN
F 3 "" H 4050 2150 50  0001 C CNN
	1    4050 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4050 2050 4300 2050
Wire Wire Line
	8250 2050 8250 1650
Wire Wire Line
	8250 1650 8350 1650
Wire Wire Line
	8350 1750 8300 1750
Wire Wire Line
	8300 1750 8300 2150
Wire Wire Line
	8300 2150 7000 2150
Wire Wire Line
	4400 1650 4300 1650
Wire Wire Line
	4300 1650 4300 2050
Connection ~ 4300 2050
Wire Wire Line
	4300 2050 5650 2050
Wire Wire Line
	5750 1650 5650 1650
Wire Wire Line
	5650 1650 5650 2050
Connection ~ 5650 2050
Wire Wire Line
	5650 2050 6950 2050
Wire Wire Line
	7050 1650 6950 1650
Wire Wire Line
	6950 1650 6950 2050
Connection ~ 6950 2050
Wire Wire Line
	6950 2050 8250 2050
Wire Wire Line
	4400 1750 4350 1750
Wire Wire Line
	4350 1750 4350 2150
Connection ~ 4350 2150
Wire Wire Line
	4350 2150 4050 2150
Wire Wire Line
	5750 1750 5700 1750
Wire Wire Line
	5700 1750 5700 2150
Connection ~ 5700 2150
Wire Wire Line
	5700 2150 4350 2150
Wire Wire Line
	7050 1750 7000 1750
Wire Wire Line
	7000 1750 7000 2150
Connection ~ 7000 2150
Wire Wire Line
	7000 2150 5700 2150
Text GLabel 4600 2350 0    50   Input ~ 0
SCL
Text GLabel 4600 2450 0    50   BiDi ~ 0
SDA
Wire Wire Line
	2500 1900 2600 1900
Wire Wire Line
	2500 2000 2600 2000
Wire Wire Line
	4600 2350 5400 2350
Wire Wire Line
	8050 2350 8050 1450
Wire Wire Line
	8050 1450 7950 1450
Wire Wire Line
	7950 1550 8000 1550
Wire Wire Line
	8000 1550 8000 2450
Wire Wire Line
	8000 2450 6700 2450
Wire Wire Line
	6650 1450 6750 1450
Wire Wire Line
	6750 1450 6750 2350
Connection ~ 6750 2350
Wire Wire Line
	6750 2350 8050 2350
Wire Wire Line
	6650 1550 6700 1550
Wire Wire Line
	6700 1550 6700 2450
Connection ~ 6700 2450
Wire Wire Line
	6700 2450 5350 2450
Wire Wire Line
	5300 1450 5400 1450
Wire Wire Line
	5400 1450 5400 2350
Connection ~ 5400 2350
Wire Wire Line
	5400 2350 6750 2350
Wire Wire Line
	5300 1550 5350 1550
Wire Wire Line
	5350 1550 5350 2450
Connection ~ 5350 2450
Wire Wire Line
	5350 2450 4600 2450
$Comp
L power:+3V3 #PWR03
U 1 1 5CC5CC93
P 5600 1050
F 0 "#PWR03" H 5600 900 50  0001 C CNN
F 1 "+3V3" H 5615 1223 50  0000 C CNN
F 2 "" H 5600 1050 50  0001 C CNN
F 3 "" H 5600 1050 50  0001 C CNN
	1    5600 1050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 1150 5600 1050
Wire Wire Line
	5600 1150 5750 1150
$Comp
L power:GND #PWR06
U 1 1 5CC5E2FE
P 5600 1300
F 0 "#PWR06" H 5600 1050 50  0001 C CNN
F 1 "GND" H 5605 1127 50  0000 C CNN
F 2 "" H 5600 1300 50  0001 C CNN
F 3 "" H 5600 1300 50  0001 C CNN
	1    5600 1300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 1300 5600 1250
Wire Wire Line
	5600 1250 5750 1250
Text GLabel 2600 2000 2    50   Output ~ 0
SCL
Text GLabel 2600 1900 2    50   BiDi ~ 0
SDA
Text GLabel 2600 2200 2    50   Input ~ 0
MOTION
Wire Wire Line
	2500 2200 2600 2200
Text GLabel 9350 1150 2    50   Output ~ 0
MOTION
Wire Wire Line
	9250 1150 9350 1150
$Comp
L ClickBoards:MikroBus ADC_2_click1
U 1 1 5CC619CB
P 8800 2800
F 0 "ADC_2_click1" H 8800 3465 50  0000 C CNN
F 1 "MikroBus" H 8800 3374 50  0000 C CNN
F 2 "Click_boards:Click_board" H 8800 3300 50  0001 C CNN
F 3 "" H 8800 3300 50  0001 C CNN
	1    8800 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 2150 8300 3150
Wire Wire Line
	8300 3150 8350 3150
Connection ~ 8300 2150
Wire Wire Line
	8250 2050 8250 3050
Wire Wire Line
	8250 3050 8350 3050
Connection ~ 8250 2050
Wire Wire Line
	2500 2300 2600 2300
Text GLabel 2600 2300 2    50   Input ~ 0
ADC_CS
Text GLabel 8200 2650 0    50   Input ~ 0
ADC_CS
Wire Wire Line
	8200 2650 8350 2650
Text GLabel 2600 2800 2    50   Input ~ 0
MISO
Text GLabel 2600 2900 2    50   Output ~ 0
MOSI
Text GLabel 2600 3000 2    50   Output ~ 0
SCK
Wire Wire Line
	2500 2800 2600 2800
Wire Wire Line
	2500 2900 2600 2900
Wire Wire Line
	2500 3000 2600 3000
Text GLabel 8200 2750 0    50   Input ~ 0
SCK
Text GLabel 8200 2850 0    50   Output ~ 0
MISO
Wire Wire Line
	8200 2750 8350 2750
Wire Wire Line
	8200 2850 8350 2850
Text GLabel 850  3200 0    50   Output ~ 0
LED_bck
Text GLabel 850  2000 0    50   Output ~ 0
LED_CO2
Text GLabel 2600 2400 2    50   Output ~ 0
LED_dust
Text GLabel 850  2700 0    50   Output ~ 0
LED_O2
Wire Wire Line
	850  2000 900  2000
Wire Wire Line
	850  2700 900  2700
Wire Wire Line
	850  3200 900  3200
Wire Wire Line
	2500 2400 2600 2400
Text GLabel 2600 3300 2    50   Output ~ 0
LED_bckup
Wire Wire Line
	2500 3300 2600 3300
$Comp
L Transistor_BJT:MJE13009G Q1
U 1 1 5CC7D492
P 4800 3700
F 0 "Q1" H 4992 3746 50  0000 L CNN
F 1 "MJE15030" H 4992 3655 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 5050 3625 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/MJE13009-D.PDF" H 4800 3700 50  0001 L CNN
	1    4800 3700
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5CC7F1FA
P 4450 3700
F 0 "R1" V 4243 3700 50  0000 C CNN
F 1 "100R" V 4334 3700 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 4380 3700 50  0001 C CNN
F 3 "~" H 4450 3700 50  0001 C CNN
	1    4450 3700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR09
U 1 1 5CC7F469
P 4900 3900
F 0 "#PWR09" H 4900 3650 50  0001 C CNN
F 1 "GND" H 4905 3727 50  0000 C CNN
F 2 "" H 4900 3900 50  0001 C CNN
F 3 "" H 4900 3900 50  0001 C CNN
	1    4900 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x06 J3
U 1 1 5CC83021
P 7800 3950
F 0 "J3" H 7880 3942 50  0000 L CNN
F 1 "Screw_Terminal_01x06" H 7880 3851 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_bornier-6_P5.08mm" H 7800 3950 50  0001 C CNN
F 3 "~" H 7800 3950 50  0001 C CNN
	1    7800 3950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 5CC8B3B5
P 4450 4750
F 0 "R3" V 4243 4750 50  0000 C CNN
F 1 "100R" V 4334 4750 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 4380 4750 50  0001 C CNN
F 3 "~" H 4450 4750 50  0001 C CNN
	1    4450 4750
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR013
U 1 1 5CC8B3BD
P 4900 4950
F 0 "#PWR013" H 4900 4700 50  0001 C CNN
F 1 "GND" H 4905 4777 50  0000 C CNN
F 2 "" H 4900 4950 50  0001 C CNN
F 3 "" H 4900 4950 50  0001 C CNN
	1    4900 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5CC8D940
P 6050 3700
F 0 "R2" V 5843 3700 50  0000 C CNN
F 1 "100R" V 5934 3700 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 5980 3700 50  0001 C CNN
F 3 "~" H 6050 3700 50  0001 C CNN
	1    6050 3700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR010
U 1 1 5CC8D948
P 6500 3900
F 0 "#PWR010" H 6500 3650 50  0001 C CNN
F 1 "GND" H 6505 3727 50  0000 C CNN
F 2 "" H 6500 3900 50  0001 C CNN
F 3 "" H 6500 3900 50  0001 C CNN
	1    6500 3900
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 5CC8D95C
P 6050 4750
F 0 "R4" V 5843 4750 50  0000 C CNN
F 1 "100R" V 5934 4750 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 5980 4750 50  0001 C CNN
F 3 "~" H 6050 4750 50  0001 C CNN
	1    6050 4750
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR014
U 1 1 5CC8D964
P 6500 4950
F 0 "#PWR014" H 6500 4700 50  0001 C CNN
F 1 "GND" H 6505 4777 50  0000 C CNN
F 2 "" H 6500 4950 50  0001 C CNN
F 3 "" H 6500 4950 50  0001 C CNN
	1    6500 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R5
U 1 1 5CC90F78
P 5200 5800
F 0 "R5" V 4993 5800 50  0000 C CNN
F 1 "100R" V 5084 5800 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder" V 5130 5800 50  0001 C CNN
F 3 "~" H 5200 5800 50  0001 C CNN
	1    5200 5800
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR015
U 1 1 5CC90F80
P 5650 6000
F 0 "#PWR015" H 5650 5750 50  0001 C CNN
F 1 "GND" H 5655 5827 50  0000 C CNN
F 2 "" H 5650 6000 50  0001 C CNN
F 3 "" H 5650 6000 50  0001 C CNN
	1    5650 6000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 3100 7450 3100
Wire Wire Line
	7450 3100 7450 3750
Wire Wire Line
	7450 3750 7600 3750
Wire Wire Line
	7400 3200 7400 3850
Wire Wire Line
	7400 3850 7600 3850
Wire Wire Line
	6500 3200 7400 3200
Wire Wire Line
	4900 4150 7400 4150
Wire Wire Line
	7400 4150 7400 3950
Wire Wire Line
	7400 3950 7600 3950
Wire Wire Line
	6500 4200 7450 4200
Wire Wire Line
	7450 4200 7450 4050
Wire Wire Line
	7450 4050 7600 4050
Wire Wire Line
	5650 5200 7500 5200
Wire Wire Line
	7500 5200 7500 4150
Wire Wire Line
	7500 4150 7600 4150
$Comp
L power:GND #PWR012
U 1 1 5CCA038F
P 7600 4300
F 0 "#PWR012" H 7600 4050 50  0001 C CNN
F 1 "GND" H 7605 4127 50  0000 C CNN
F 2 "" H 7600 4300 50  0001 C CNN
F 3 "" H 7600 4300 50  0001 C CNN
	1    7600 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	7600 4250 7600 4300
Text GLabel 5000 5800 0    50   Input ~ 0
LED_bckup
Text GLabel 5850 3700 0    50   Input ~ 0
LED_bck
Text GLabel 4250 4750 0    50   Input ~ 0
LED_O2
Text GLabel 5850 4750 0    50   Input ~ 0
LED_dust
Text GLabel 4250 3700 0    50   Input ~ 0
LED_CO2
Wire Wire Line
	4250 3700 4300 3700
Wire Wire Line
	5850 3700 5900 3700
Wire Wire Line
	4250 4750 4300 4750
Wire Wire Line
	5850 4750 5900 4750
Wire Wire Line
	5000 5800 5050 5800
$Comp
L Transistor_BJT:MJE13009G Q2
U 1 1 5CCC1A53
P 6400 3700
F 0 "Q2" H 6592 3746 50  0000 L CNN
F 1 "MJE15030" H 6592 3655 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 6650 3625 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/MJE13009-D.PDF" H 6400 3700 50  0001 L CNN
	1    6400 3700
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:MJE13009G Q4
U 1 1 5CCC1AD3
P 6400 4750
F 0 "Q4" H 6592 4796 50  0000 L CNN
F 1 "MJE15030" H 6592 4705 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 6650 4675 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/MJE13009-D.PDF" H 6400 4750 50  0001 L CNN
	1    6400 4750
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:MJE13009G Q3
U 1 1 5CCC1B3F
P 4800 4750
F 0 "Q3" H 4992 4796 50  0000 L CNN
F 1 "MJE15030" H 4992 4705 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 5050 4675 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/MJE13009-D.PDF" H 4800 4750 50  0001 L CNN
	1    4800 4750
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:MJE13009G Q5
U 1 1 5CCC1BCD
P 5550 5800
F 0 "Q5" H 5742 5846 50  0000 L CNN
F 1 "MJE15030" H 5742 5755 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 5800 5725 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/MJE13009-D.PDF" H 5550 5800 50  0001 L CNN
	1    5550 5800
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J1
U 1 1 5CCC225A
P 3400 1150
F 0 "J1" H 3479 1142 50  0000 L CNN
F 1 "OxygenSensPwr" H 3479 1051 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Horizontal" H 3400 1150 50  0001 C CNN
F 3 "~" H 3400 1150 50  0001 C CNN
	1    3400 1150
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR04
U 1 1 5CCC23AF
P 3100 1100
F 0 "#PWR04" H 3100 950 50  0001 C CNN
F 1 "+5V" H 3115 1273 50  0000 C CNN
F 2 "" H 3100 1100 50  0001 C CNN
F 3 "" H 3100 1100 50  0001 C CNN
	1    3100 1100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR05
U 1 1 5CCC2472
P 3100 1300
F 0 "#PWR05" H 3100 1050 50  0001 C CNN
F 1 "GND" H 3105 1127 50  0000 C CNN
F 2 "" H 3100 1300 50  0001 C CNN
F 3 "" H 3100 1300 50  0001 C CNN
	1    3100 1300
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 1100 3100 1150
Wire Wire Line
	3100 1150 3200 1150
Wire Wire Line
	3100 1300 3100 1250
Wire Wire Line
	3100 1250 3200 1250
Wire Wire Line
	4900 3100 4900 3500
Wire Wire Line
	6500 3200 6500 3500
Wire Wire Line
	4900 4150 4900 4550
Wire Wire Line
	6500 4200 6500 4550
Wire Wire Line
	5650 5200 5650 5600
$Comp
L Mechanical:MountingHole H1
U 1 1 5CCE581A
P 1000 4500
F 0 "H1" H 1100 4546 50  0000 L CNN
F 1 "MountingHole" H 1100 4455 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 1000 4500 50  0001 C CNN
F 3 "~" H 1000 4500 50  0001 C CNN
	1    1000 4500
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 5CCE5967
P 1000 4700
F 0 "H2" H 1100 4746 50  0000 L CNN
F 1 "MountingHole" H 1100 4655 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 1000 4700 50  0001 C CNN
F 3 "~" H 1000 4700 50  0001 C CNN
	1    1000 4700
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 5CCE59A3
P 1000 4900
F 0 "H3" H 1100 4946 50  0000 L CNN
F 1 "MountingHole" H 1100 4855 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 1000 4900 50  0001 C CNN
F 3 "~" H 1000 4900 50  0001 C CNN
	1    1000 4900
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 5CCE59E1
P 1000 5100
F 0 "H4" H 1100 5146 50  0000 L CNN
F 1 "MountingHole" H 1100 5055 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3_Pad" H 1000 5100 50  0001 C CNN
F 3 "~" H 1000 5100 50  0001 C CNN
	1    1000 5100
	1    0    0    -1  
$EndComp
$EndSCHEMATC
