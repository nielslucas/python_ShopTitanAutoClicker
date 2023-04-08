import pyautogui as gui
import time
from .PopUp import PopUp
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from Models.RgbModel import RgbModel

class Crafting:

    def __init__(self):
        self.CraftPosition = (1645, 975)
        self.CraftReadyRGB = RgbModel(25, 233, 115, 40)

        #popup
        self.PopUp = PopUp()

    def Execute(self):
        if not self.ClickOnready():
            return;

        time.sleep(0.1)

        if not self.PopUp.IsPopUpOpen():
            return

        self.ClickOnCollect()

    def ClickOnready(self):
        gui.moveTo(*self.CraftPosition)
        itemIsReady = False

        for i in range(10000):
            rgb = RgbModel(*gui.pixel(*self.CraftPosition), 0)

            if rgb.r not in self.CraftReadyRGB.rRange:
                continue
            if rgb.g not in self.CraftReadyRGB.gRange:
                continue
            if rgb.b not in self.CraftReadyRGB.bRange:
                continue

            gui.click();
            return True

        return False

    def ClickOnCollect(self):
        location = (727, 773)
        rgb = (82, 44, 68)

        for i in range(100):
            i += 1
            resultRGB = gui.pixel(*location)
            gui.moveTo(*location)
            if  resultRGB == rgb:
                gui.click(*location)
                return