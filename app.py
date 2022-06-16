import pyautogui as pya
from time import sleep as sl
from random import randrange as rra

wid = pya.size().width
hei = pya.size().height

while 1:
    sl(rra(30, 60))
    pya.moveTo(rra(10, wid-100), rra(10, hei-100), 1)
