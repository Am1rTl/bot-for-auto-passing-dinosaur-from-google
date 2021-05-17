from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class autobot():
    replayBtn = (340,390)
    dinasaur = (170 ,475)
def restartGame(): 
    pyautogui.click(autobot.replayBtn)
    pyautogui.keyDown('down')
     
def pressSpase():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.08)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')
    
def imageGrab():
    
    box = (autobot.dinasaur[0] + 60,autobot.dinasaur[1],autobot.dinasaur[0] + 150,autobot.dinasaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors()) 
    return a.sum()

def main():
    restartGame()
    while True:
        if (imageGrab()!=697):
            pressSpase()
            time.sleep(0.1)
            
#restartGame()
#pressSpase()
while True :
    main()
