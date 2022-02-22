import subprocess
import pynput
from pynput.keyboard import Key
from pynput.mouse import Button
import time
import random

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

subprocess.Popen("mspaint")

time.sleep(0.3)

keyboard.press(Key.alt)
keyboard.release(Key.alt)
keyboard.press("C")
keyboard.release("C")
keyboard.press("C")
keyboard.release("C")
keyboard.press("2")
keyboard.release("2")
keyboard.press(Key.alt)
keyboard.release(Key.alt)
keyboard.press("C")
keyboard.release("C")
keyboard.press("T")
keyboard.release("T")
keyboard.press("2")
keyboard.release("2")
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

# listener = pynput.mouse.Listener(on_click=on_click)
# listener.start()


def change_couleur():

    keyboard.press(Key.alt)
    keyboard.release(Key.alt)
    keyboard.press("C")
    keyboard.release("C")
    keyboard.press("M")
    keyboard.release("M")
    keyboard.press("C")
    keyboard.release("C")
    time.sleep(0.1)
    keyboard.press(Key.alt)
    keyboard.press("V")
    keyboard.release(Key.alt)
    keyboard.release("V")
    saisir_mot(random.randint(0,255))
    time.sleep(0.1)
    keyboard.press(Key.alt)
    keyboard.press("R")
    keyboard.release(Key.alt)
    keyboard.release("R")
    saisir_mot(random.randint(0,255))
    time.sleep(0.1)
    keyboard.press(Key.alt)
    keyboard.press("B")
    keyboard.release(Key.alt)
    keyboard.release("B")
    saisir_mot(random.randint(0,255))
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def saisir_mot(mot):
    for x in str(mot):
        keyboard.press(str(x))
        keyboard.release(str(x))

def check_box(x,y,liste):
    if x<liste[0][0] or y<liste[0][1]:
        xx=False
    else:
        xx=True
    if x>liste[1][0] or y>liste[1][1]:
        yy=False
    else:
        yy=True
    if xx==True and yy==True:
        return True
    return False

liste = []

with pynput.mouse.Events() as events:

    for event in events:
        try:
            if event.button == pynput.mouse.Button.right:
                break
            else:
                if event.pressed:
                    print('Received event {}'.format(event))
                    liste.append([event.x,event.y])
        except:
            pass

for _ in range(300):

    # print(liste)
    # print('The current pointer position is {0}'.format(mouse.position))
    change_couleur()
    time.sleep(0.1)
    mouse.position = (random.randint(liste[0][0],liste[1][0]),random.randint(liste[0][1],liste[1][1]))
    # time.sleep(0.01)

    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(0.1)






