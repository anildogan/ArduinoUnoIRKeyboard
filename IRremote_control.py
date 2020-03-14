import serial
import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

list=['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18',]

COM1='COM1'
COM2='COM2'
COM3='COM3'
COM4='COM4'
COM5='COM5'
COM6='COM6'
COM7='COM7'
COM8='COM8'
COM9='COM9'
COM10='COM10'
COM11='COM11'
COM12='COM12'
COM13='COM13'
COM14='COM14'
COM15='COM15'
COM16='COM16'
COM17='COM17'
COM18='COM18'
COM19='COM19'
time.sleep(1)
ser = serial.Serial()

ser.baudrate = 9600

i = 0

while True:
    time.sleep(.2)
    ser.port = list[i]
    try:

        ser.open()
        if ser.isOpen()==True:
            print('Connected to ' + list[i])
            #print('arduino is on COMPORT'.join(i))
            break
        break

    except:
        print('Waiting for ... ' + list[i])
        i=i+1
        if i==18:
            print('Kindly remove usb cable and try again')
            break

while True:
    cc=str(ser.readline())
    key = cc[2:][:-5]
    
    #arrow keys
    if(key == "right"):
        keyboard.press(Key.right)  
        time.sleep(0.1)
        keyboard.release(Key.right)  
    
    if(key == "left"):
        keyboard.press(Key.left)  
        time.sleep(0.1)
        keyboard.release(Key.left)  
    
    if(key == "down"):
        keyboard.press(Key.down)
        time.sleep(0.1) 
        keyboard.release(Key.down)  
    
    if(key == "up"):
        keyboard.press(Key.up)  
        time.sleep(0.1)
        keyboard.release(Key.up)  
    
    #media keys
    if(key == "play"):
        keyboard.press(Key.media_play_pause)  
        keyboard.release(Key.media_play_pause)  
    
    if(key == "next"):
        keyboard.press(Key.media_next)  
        keyboard.release(Key.media_next)      
    
    if(key == "previous"):
        keyboard.press(Key.media_previous)  
        keyboard.release(Key.media_previous)  
    
    if(key == "vol_down"):
        keyboard.press(Key.media_volume_down)  
        keyboard.release(Key.media_volume_down)  
    
    if(key == "vol_up"):
        keyboard.press(Key.media_volume_up)  
        keyboard.release(Key.media_volume_up)  
    
    if(key == "mute"):
        keyboard.press(Key.media_volume_mute)  
        keyboard.release(Key.media_volume_mute)
    
    #left click 
    if(key == "click"):
        mouse.press(Button.left)
        mouse.release(Button.left)
    
    #mouse rotates
    if(key == "rightmouse"):
        mouse.move(15,0)
    
    if(key == "leftmouse"):
        mouse.move(-15,0)
    
    if(key == "downmouse"):
        mouse.move(0,15)
    
    if(key == "upmouse"):
        mouse.move(0,-15)
    
    #this script shuts down computer on Windows 10
    if(key == "kill"):
        keyboard.press(Key.cmd_l)  
        keyboard.release(Key.cmd_l)
        time.sleep(0.1)
        keyboard.press(Key.tab)  
        keyboard.release(Key.tab)
        time.sleep(0.1)
        for i in range(5):
            keyboard.press(Key.down)  
            keyboard.release(Key.down)
            time.sleep(0.1)
        keyboard.press(Key.enter)  
        keyboard.release(Key.enter) 
        time.sleep(0.1)
        keyboard.press(Key.down)  
        keyboard.release(Key.down)
        time.sleep(0.1)
        keyboard.press(Key.enter)  
        keyboard.release(Key.enter)
        time.sleep(0.1)
    
    if(key == "close"): 
        ser.close()
        break
    