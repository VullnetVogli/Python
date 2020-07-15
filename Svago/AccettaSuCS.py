from PIL import ImageGrab, ImageOps
import numpy as np
import subprocess
import pyautogui
import time
import os

def premi_accetta():
    
    while True:

        screen = ImageGrab.grab(bbox = (834, 566, 1064, 654))

        grigio = ImageOps.grayscale(screen)

        print(grigio.getpixel((10, 10)))

        if grigio.getpixel((10, 10)) == 134:
    
            pyautogui.click(949, 610, 2, 0.2)

            time.sleep(19)

            controlla_startata()

        time.sleep(1)

def avvia_cs():
    
    while os.system('tasklist /FI "IMAGENAME eq csgo.exe" 2>NUL | find /I /N "csgo.exe">NUL') :

        print('CS non avviato!')

        time.sleep(5)

def controlla_startata():

    while True:

        screen = ImageGrab.grab(bbox = (1842, 566, 1906, 567))
        
        grigio = ImageOps.grayscale(screen)

        if grigio.getpixel((0, 0)) == 33:
            
            premi_accetta()
            
        else:
            
            quit()
            
        time.sleep(1)

premi_accetta()