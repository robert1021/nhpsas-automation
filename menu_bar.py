import pyautogui
import time
from utilities import search_for_image
from config import *


class MenuBar:

    def __init__(self):
        self.action_img = os.path.join(image_path, "nhpsas_menubar", "action.PNG")
        self.action_exit_img = os.path.join(image_path, "nhpsas_menubar", "action_exit.PNG")
        self.save_img = os.path.join(image_path, "nhpsas_menubar", "save.PNG")
        self.insert_record_img = os.path.join(image_path, "nhpsas_menubar", "insert_record.PNG")

    def insert_record(self):
        insert_record_coord = search_for_image(self.insert_record_img)
        pyautogui.moveTo(insert_record_coord)
        pyautogui.click()

    def exit(self):
        action_coord = search_for_image(self.action_img)
        pyautogui.moveTo(action_coord)
        pyautogui.click()
        time.sleep(3)
        action_exit_coord = search_for_image(self.action_exit_img)
        pyautogui.moveTo(action_exit_coord)
        pyautogui.click()

    def save(self):
        save_coord = search_for_image(self.save_img)
        pyautogui.moveTo(save_coord)
        pyautogui.click()
