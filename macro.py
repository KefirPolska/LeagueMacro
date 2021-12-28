#in order for this script to work you need to have python and pynput
#check if you have python already installed simplly by writing "python" in cmd
# if you do then write "pip install pynput"
# after that just doubleclick script
# !!!!! DONT SPAM KEYS LIKE CRAZY, IT TAKE A FRACTION OF A SECOND TO WRITE EVERYTHING !!!!!
# YOU CAN STILL USE IT QUITE FREQUENTLY, BUT IF YOU WILL SPAM LIKE CRAZY OR PRESS KEY AND DONT RELEASE IT YOU CAN ACCIDENTALLY USE SUMMONER SPELLS 


import pynput
from pynput import keyboard
#Getting access to keyboard library 
from pynput.keyboard import Key, Listener, Controller
#getting sleep bcoz python dosent have a fricking sleep imported in on default
import time

mess = Controller()

#Messeges that you want to be after pressing key
messages = {'1' : 'Dont push idiot', '2' : 'Play for drake', '3' : 'Play for baron', '4' : 'Play safe', '5' : 'freeze lane'}


#checkig which key was pressed and calling function
def pressed(key):
    if key == Key.f2:
        sendmessage('1')
    if key == Key.f3:
        sendmessage('2')
    if key == Key.f4:
        sendmessage('3')
    if key == Key.f5:
        sendmessage('4')
    if key == Key.f6:
        sendmessage('5')

#ending script
def released(key):
    pass


#sending message to this idiots
def sendmessage(name):
    mess.press(Key.enter)
    mess.release(Key.enter)
    time.sleep(0.01)
    for i in messages[name]:
        mess.press(i)
        mess.release(i)
    time.sleep(0.01)
    mess.press(Key.enter)
    mess.release(Key.enter)
    

#shit that makes it works 
with Listener(on_press=pressed, on_release=released) as listener:
    listener.join()
