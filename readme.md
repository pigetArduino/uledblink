[Version française / French version](https://github.com/pigetArduino/utest/blob/master/README.fr.MD)

![Photo ULed](https://github.com/pigetArduino/uled/raw/master/doc/universalLed_photo.jpg)   
Universal Led is an USB device based on an Arduino nano (clone) to easily control 5 leds on Windows    
Demo: https://www.youtube.com/watch?v=hgvi46x4oaE


![ULed App](https://github.com/pigetArduino/uled/raw/master/doc/ul_app11.png)   
You can choose 6 color for each leds. (White/Red/Green/Blue/Yellow/Orange/Purple)

# Usage
* Install drivers for arduino nano (clone ch340g) : http://nano.madnerd.org
* Download arduino/python code : http://uled.madnerd.org
* Upload sketch **uled.ino**
* Download application : http://uledapp.madnerd.org    

How to install drivers : https://www.youtube.com/watch?v=m3CsftsfiQU

# Components
* Arduino nano CH340G: 2€
* 30 leds WS2812B : 4.50€ ( 5 leds :0.75€)
* Resistor pack 400pcs (3€) (1 resistor: 0.0071€)
* Total : 9.5€ (2.75€)

# Wiring
Wiring / How to make it: https://www.youtube.com/watch?v=hgvi46x4oaE

Do not used more than 5 leds without a dedicated power supply or this can damage the leds   
Each led can draw up to **60ma** at full brightness   
An Arduino can provided up to **500ma** (on 5v/Gnd pin)   
```5 leds = 5x60ma = 300ma ```  
Source:
https://learn.adafruit.com/adafruit-neopixel-uberguide/basic-connections

* D6 --> RESISTOR (470Ohm) DI
* +5V --> 5V
* GND --> GND

![Wiring_uled](https://github.com/pigetArduino/uled/raw/master/doc/universalLed_wiring.png)

# 3D printing
This model is an all purpose case for arduino nano projects    
Models by Olivier Sarrailh : https://github.com/pigetArduino/uled/tree/master/3D    
You will need to fill a hole for the led strip (see wiring instructions)

# Create your own applications
* Check out: http://github.com/pigetArduino/utest   
* The source code is available in **apps/utest**

# Commands available
You can test the device in Arduino Serial Monitor   
Baudrate : 115200 / No Line Ending   

* ULed --------> Check if device is correct (turn off all led)
* X:Y -------> (Where X is the led and Y the color)
* 1:3 -------> (led 1 Green)

# Color
* 0 : OFF
* 1 : White/ON
* 2 : Red
* 3 : Green
* 4 : Blue
* 5 : Yellow
* 6 : Orange
* 7 : Purple

# Licences
Icon by jpapun
Creative Commons Attribution (by)   
Link : http://findicons.com/icon/158595/device_and_hardware

Software by Rémi Sarrailh (madnerd.org)   
Licence: MIT
