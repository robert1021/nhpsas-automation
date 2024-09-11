import pyautogui
from utilities import search_for_image
from config import *


class Login:
    """ Class used to log into NHPSAS.

    """

    def __init__(self, username: str, password: str, database: str):
        self.username = username
        self.password = password
        self.database = database

        self.username_img = os.path.join(image_path, "nhpsas_login", "username.PNG")
        self.password_img = os.path.join(image_path, "nhpsas_login", "password.PNG")
        self.database_img = os.path.join(image_path, "nhpsas_login", "database.PNG")
        self.connect_img = os.path.join(image_path, "nhpsas_login", "connect.PNG")

    def enter_username(self):
        username_coord = search_for_image(self.username_img)
        pyautogui.moveTo(username_coord)
        pyautogui.move(50, 0)
        pyautogui.click()
        pyautogui.write(self.username, interval=0.2)

    def enter_password(self):
        password_coord = search_for_image(self.password_img)
        pyautogui.moveTo(password_coord)
        pyautogui.move(50, 0)
        pyautogui.click()
        pyautogui.write(self.password, interval=0.2)

    def enter_database(self):
        database_coord = search_for_image(self.database_img)
        pyautogui.moveTo(database_coord)
        pyautogui.move(50, 0)
        pyautogui.click()
        pyautogui.write(self.database, interval=0.2)

    def click_connect_button(self):
        connect_coord = search_for_image(self.connect_img)
        pyautogui.moveTo(connect_coord)
        pyautogui.click()

    def submit(self):
        self.enter_username()
        self.enter_password()
        self.enter_database()
        self.click_connect_button()



