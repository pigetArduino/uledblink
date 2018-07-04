Midi file to Led
----
![Photo ULed](doc/leds2.jpg)   

* Arduino code : https://github.com/pigetArduino/uledblink/archive/master.zip
* Software : https://github.com/pigetArduino/uledblink/releases
* Upload sketch **uledblink.ino**
* Install midiLed_setup.exe
* Open midi file

Leds will sync with a drum track (1:kick/2:snare/3:toms/4:hithat/5:cymbals)

![midiled App](https://raw.githubusercontent.com/pigetArduino/uledblink/master/doc/midiled_app.png)   
You can choose 6 color for each leds. (White/Red/Green/Blue/Yellow/Orange/Purple)

# Commands
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

![Wiring_uled](https://raw.githubusercontent.com/pigetArduino/uled/master/doc/universalLed_wiring.png)

# Licences
Software by Rémi Sarrailh (madnerd.org)   
Licence: MIT
