import mido
import mido.backends.pygame
from lib import USB
from threading import Thread
import time
from tkinter import *
from tkinter.filedialog import *

global midifile,isSending,isPlaying
global velocityColor,randomColor,color
midifile = ""
isSending = False
isPlaying = False

#Led
velocityColor = False
randomColor = False
color = "3"

#Serial
device_name = "CH340"
device_type = "ULedBlink"
device_return_string = "OK"
device_baudrate = 115200

def led(m):
    led_t = Thread(target=led_thread,args=(m,))
    led_t.daemon = True
    led_t.start()

def led_thread(m):
    print("Send " + m)
    global isSending
    while isSending:
        print("Waiting")
    isSending = True 
    usb.write(m)
    time.sleep(0.020)
    isSending = False



#Midi
mido.set_backend('mido.backends.pygame')
output = mido.open_output()

def play_thread():
    global isPlaying,midifile
    global velocityColor,randomColor,color
    print(midifile)
    try:
        mid = mido.MidiFile(midifile)

        for message in mid.play():
            if isPlaying:
                #print(message.channel)
                if message.type == "note_on":
                    if message.channel >= 9:
                        note = message.note
                        
                        if velocityColor:
                            velocity = message.velocity
                            if velocity > 0 and velocity <= 42:
                                color="3"
                            if velocity > 42 and velocity <= 84:
                                color="5"
                            if velocity > 84 and velocity <= 127:
                                color="2"         
                            if velocity == 128:
                                color="1"
                        if randomColor:
                            color=str(random.randint(1,7))
                    
                        #print(note)
                        #Bass drums
                        if note == 35 or note == 36:
                            m = "1"+","+color

                        #Snare
                        if note == 37 or note == 38 or note == 39 or note == 40:
                            m = "2"+","+color

                        #Toms
                        if note == 41 or note == 43 or note == 45 or note == 47 or note == 58 or note == 50:
                            m = "3"+","+color
                        
                        #Hithat
                        if note == 42 or note == 44 or note == 46:
                            m = "4"+","+color

                        #Cymbals
                        if note == 49 or note == 51 or note == 52 or note == 55 or note == 57 or note == 59 or note == 53 or note == 56:
                            m = "5"+","+color
                        led(m)
                try:
                    output.send(message)
                except:
                    print("Pygame is going mad...")
            else:
                output.panic()
                break;
    except:
        print("File not readable")
        isPlaying = False
    file_label.config(fg="gray")

# GUI
def openMidi():
    global midifile
    midifile = askopenfilename(parent=root,filetypes=[(("Midi File","*.mid"))],title = "Select a midi file")
    file_label.config(text=midifile)

def play():
    global isPlaying
    if isPlaying is False:
        file_label.config(fg="red")
        isPlaying = True
        play_t = Thread(target=play_thread)
        play_t.daemon = True
        play_t.start()

def stop():
    global isPlaying
    if isPlaying:
        file_label.config(fg="gray")
        isPlaying = False

root = Tk()
Button(text="Open",command=openMidi).pack()
Button(text="Stop",command=stop).pack()
Button(text="Play",command=play).pack()

file_label = Label(text="No music loaded")
file_label.pack()
status = Label(text="Searching ...")
status.pack()

usb = USB.Device(device_name,device_type,device_return_string,device_baudrate,status)

root.mainloop()

