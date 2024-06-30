from PIL import ImageGrab
import time
from datetime import datetime
import keyboard

# начало рыбалки
isPressed = False
delay = 0.2
maxCatching = 5

# FUNCTION + 
def tabulate():
    # TABULATE
    keyboard.press('alt')
    time.sleep(delay)
    keyboard.press('tab')
    time.sleep(delay)
    keyboard.release('tab')
    keyboard.release('alt')
    
    # test again
    keyboard.press('e')
    time.sleep(0.01)
    keyboard.release('e')
    time.sleep(0.01)
    
    # TABULATE second time
    keyboard.press('alt')
    time.sleep(delay)
    keyboard.press('tab')
    time.sleep(delay)
    keyboard.release('tab')
    keyboard.release('alt')

print("Fishing start after 5 sec")
time.sleep(5)
for i in range(maxCatching):
    print("Start fishing")
    while(True):
        
        if(isPressed == False):
            keyboard.press('e')
            time.sleep(0.01)
            keyboard.release('e')
            time.sleep(0.01)
            isPressed = True
            tabulate()

        time.sleep(0.2)
        image = ImageGrab.grab(bbox=(955, 465, 965, 500))
        isFish = False
        for y in range(0, 34):
            for x in range(0, 9):
                color = image.getpixel((x, y))
                # print(color)
                if (color == (250,214,138)):
                    isFish = True
                elif(color == (250,216,140)):
                    isFish = True
                elif(color == (251,216,140)):
                    isFish = True
                elif(color == (251,216,140)):
                    isFish = True
        if(isFish):
            print(datetime.now(), "True")
            keyboard.press('e')
            time.sleep(0.01)
            keyboard.release('e')
            time.sleep(0.01)
            tabulate()
            isFish = False
            isPressed = False
            time.sleep(8)
            continue
        # print(datetime.now(), "False")
        
