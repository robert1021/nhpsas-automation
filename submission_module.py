import pyautogui
import pydirectinput
from utilities import search_for_image
import time
from menu_bar import MenuBar
from config import *


class SubmissionModule:

    def __init__(self):
        self.menubar = MenuBar()
        self.forms_error_company_contact_img = os.path.join(image_path, "nhpsas_modules", "submission", "forms_error_company_contact.PNG")
        self.forms_error_ok_btn_img = os.path.join(image_path, "nhpsas_modules", "submission", "forms_error_ok_btn.PNG")
        self.error_img = os.path.join(image_path, "nhpsas_modules", "submission", "error.PNG")
        self.submission_id_img = os.path.join(image_path, "nhpsas_modules", "submission", "submission_id_field.PNG")
        self.attributes_tab_img = os.path.join(image_path, "nhpsas_modules", "submission", "attributes_tab.PNG")
        self.attribute_type_empty_field_img = os.path.join(image_path, "nhpsas_modules", "submission", "attributes_tab_attribute_type_empty_field.PNG")
        self.cancelled_by_licensee_search_img = os.path.join(image_path, "nhpsas_modules", "submission", "cancelled_by_licensee_search.PNG")
        self.cancelled_notice_search_img = os.path.join(image_path, "nhpsas_modules", "submission", "cancelled_notice_search.PNG")
        self.attribute_search_ok_btn_img = os.path.join(image_path, "nhpsas_modules", "submission", "attribute_type_search_ok_btn.PNG")
        self.user_role_img = os.path.join(image_path, "nhpsas_modules", "submission", "user_role.PNG")
        self.date_value_img = os.path.join(image_path, "nhpsas_modules", "submission", "date_value.PNG")
        self.date_value_ok_btn_img = os.path.join(image_path, "nhpsas_modules", "submission", "date_value_ok_btn.PNG")
        self.long_text_img = os.path.join(image_path, "nhpsas_modules", "submission", "long_text.PNG")

    def ignore_errors(self):
        # Check for forms error company contact
        for i in range(2):
            print("Checking for error...")
            error_coords = pyautogui.locateCenterOnScreen(self.error_img, confidence=0.9)
            if error_coords:
                pydirectinput.press("esc")
                break
            time.sleep(1)

    def enter_submission_id(self, submission_id):
        submission_id_coord = search_for_image(self.submission_id_img)
        pyautogui.moveTo(submission_id_coord)
        pyautogui.move(0, 25)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(1)
        pydirectinput.press("f7")
        time.sleep(1)
        pyautogui.write(submission_id, interval=0.1)
        time.sleep(1)
        pydirectinput.press("f8")
        time.sleep(1)

    def click_attributes_tab(self):
        attributes_tab_coord = search_for_image(self.attributes_tab_img)
        pyautogui.moveTo(attributes_tab_coord)
        time.sleep(0.25)
        pyautogui.click()

    def add_attribute_type_cancelled_by_licensee(self, discontinuation_date: str, isGowling: bool):
        empty_field_coord = search_for_image(self.attribute_type_empty_field_img)
        pyautogui.moveTo(empty_field_coord)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        pyautogui.move(75, 0)
        time.sleep(0.25)
        pyautogui.click()
        cancelled_by_licensee_search_coord = search_for_image(self.cancelled_by_licensee_search_img)
        pyautogui.moveTo(cancelled_by_licensee_search_coord)
        time.sleep(0.25)
        pyautogui.click()
        ok_btn_coord = search_for_image(self.attribute_search_ok_btn_img)
        pyautogui.moveTo(ok_btn_coord)
        time.sleep(0.25)
        pyautogui.click()
        user_role_coord = search_for_image(self.user_role_img)
        pyautogui.moveTo(user_role_coord)
        time.sleep(0.25)
        pyautogui.move(0, 25)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        pyautogui.write("Coordinator", interval=0.1)
        date_value_coord = search_for_image(self.date_value_img)
        pyautogui.moveTo(date_value_coord)
        time.sleep(0.25)
        pyautogui.move(0, 30)
        time.sleep(0.25)
        pyautogui.click()
        pyautogui.move(120, 0)
        time.sleep(0.25)
        pyautogui.click()
        date_value_ok_btn_coord = search_for_image(self.date_value_ok_btn_img)
        pyautogui.moveTo(date_value_ok_btn_coord)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        long_text_coord = search_for_image(self.long_text_img)
        pyautogui.moveTo(long_text_coord)
        time.sleep(0.25)
        pyautogui.move(0, 25)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.5)
        if isGowling:
            pyautogui.write(f"Discontinuation requested by licensee on {discontinuation_date}. Notice sent via Titan.", interval=0.05)
        else:
            pyautogui.write(f"Discontinuation requested by licensee on {discontinuation_date}. Notice sent via ePost.", interval=0.05)
        self.menubar.save()

    def add_attribute_type_cancellation_notice(self, discontinuation_date, isGowling: bool):
        empty_field_coord = search_for_image(self.attribute_type_empty_field_img)
        pyautogui.moveTo(empty_field_coord)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        pyautogui.move(75, 0)
        time.sleep(0.25)
        pyautogui.click()
        cancelled_notice_search_coord = search_for_image(self.cancelled_notice_search_img)
        pyautogui.moveTo(cancelled_notice_search_coord)
        time.sleep(0.25)
        pyautogui.click()
        ok_btn_coord = search_for_image(self.attribute_search_ok_btn_img)
        pyautogui.moveTo(ok_btn_coord)
        time.sleep(0.25)
        pyautogui.click()
        user_role_coord = search_for_image(self.user_role_img)
        pyautogui.moveTo(user_role_coord)
        time.sleep(0.25)
        pyautogui.move(0, 25)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        pyautogui.write("Coordinator", interval=0.1)
        date_value_coord = search_for_image(self.date_value_img)
        pyautogui.moveTo(date_value_coord)
        time.sleep(0.25)
        pyautogui.move(0, 30)
        time.sleep(0.25)
        pyautogui.click()
        pyautogui.move(120, 0)
        time.sleep(0.25)
        pyautogui.click()
        date_value_ok_btn_coord = search_for_image(self.date_value_ok_btn_img)
        pyautogui.moveTo(date_value_ok_btn_coord)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        long_text_coord = search_for_image(self.long_text_img)
        pyautogui.moveTo(long_text_coord)
        time.sleep(0.25)
        pyautogui.move(0, 25)
        time.sleep(0.25)
        pyautogui.click()
        if isGowling:
            pyautogui.write(f"Discontinuation requested by licensee on {discontinuation_date}. Notice sent via Titan.", interval=0.05)
        else:
            pyautogui.write(f"Discontinuation requested by licensee on {discontinuation_date}. Notice sent via ePost.", interval=0.05)
        self.menubar.save()




