import pyautogui as gui

class PopUp:

    def IsPopUpOpen(self):
        rgb = gui.pixel(1787, 919)
        result = rgb != (213, 196, 189)
        return result
