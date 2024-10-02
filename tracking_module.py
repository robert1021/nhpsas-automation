import pyautogui
import time
import pydirectinput
from utilities import search_for_image
from menu_bar import MenuBar
import datetime
from config import *


class TrackingModule:

    def __init__(self):
        self.menubar = MenuBar()
        self.submission_active_id_img = os.path.join(image_path, "nhpsas_modules", "tracking", "submission_active_id.PNG")
        self.workflow_roles_role_type_decision_img = os.path.join(image_path, "nhpsas_modules", "tracking", "workflow_roles_role_type_decision.PNG")
        self.first_name_img = os.path.join(image_path, "nhpsas_modules", "tracking", "first_name.PNG")
        self.surname_img = os.path.join(image_path, "nhpsas_modules", "tracking", "surname.PNG")
        self.telephone_img = os.path.join(image_path, "nhpsas_modules", "tracking", "telephone.PNG")
        self.find_img = os.path.join(image_path, "nhpsas_modules", "tracking", "find.PNG")
        self.find_find_btn_img = os.path.join(image_path, "nhpsas_modules", "tracking", "find_find_btn.PNG")
        self.find_ok_btn_img = os.path.join(image_path, "nhpsas_modules", "tracking", "find_ok_btn.PNG")
        self.end_img = os.path.join(image_path, "nhpsas_modules", "tracking", "end.PNG")
        self.calendar_ok_btn_img = os.path.join(image_path, "nhpsas_modules", "tracking", "calendar_ok_btn.PNG")
        self.tracking_tab_img = os.path.join(image_path, "nhpsas_modules", "tracking", "tracking_tab.PNG")
        self.tracking_status_area_img = os.path.join(image_path, "nhpsas_modules", "tracking", "tracking_status_area.PNG")
        self.tracking_status_error_img = os.path.join(image_path, "nhpsas_modules", "tracking", "error_frm_40102.PNG")
        self.tracking_status_status_type_empty_field_img = os.path.join(image_path, "nhpsas_modules", "tracking", "tracking_status_status_type_empty_field.PNG")
        self.tracking_status_status_type_cancellation_of_licence_img = os.path.join(image_path, "nhpsas_modules", "tracking", "tracking_status_status_type_find_cancellation_of_licence.PNG")
        self.notes_img = os.path.join(image_path, "nhpsas_modules", "tracking", "notes.PNG")

    def enter_submission_id(self, submission_id):
        submission_id_coord = search_for_image(self.submission_active_id_img)
        pyautogui.moveTo(submission_id_coord)
        pyautogui.move(25, 25)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(1)
        pydirectinput.press("f7")
        time.sleep(1)
        pyautogui.write(submission_id, interval=0.1)
        time.sleep(1)
        pydirectinput.press("f8")

    def add_role_type_decision(self, user_id):
        decision_coord = search_for_image(self.workflow_roles_role_type_decision_img)
        pyautogui.moveTo(decision_coord)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        d1 = datetime.datetime.now()
        first_name_coord = search_for_image(self.first_name_img)
        pyautogui.moveTo(first_name_coord)
        time.sleep(0.25)
        pyautogui.move(0, 25)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        pyautogui.move(100, 0)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        find_coord = search_for_image(self.find_img)
        pyautogui.moveTo(find_coord)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        pyautogui.write(user_id, interval=0.1)
        find_btn = search_for_image(self.find_find_btn_img)
        pyautogui.moveTo(find_btn)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        ok_btn = search_for_image(self.find_ok_btn_img)
        pyautogui.moveTo(ok_btn)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        telephone_coord = search_for_image(self.telephone_img)
        pyautogui.moveTo(telephone_coord)
        time.sleep(0.25)
        pyautogui.move(400, 25)
        time.sleep(0.25)
        pyautogui.click()
        calendar_ok_btn_coord = search_for_image(self.calendar_ok_btn_img)
        pyautogui.moveTo(calendar_ok_btn_coord)
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)
        self.menubar.save()

    def click_tracking_tab(self):
        tracking_tab_coord = search_for_image(self.tracking_tab_img)
        pyautogui.moveTo(tracking_tab_coord)
        time.sleep(0.25)
        pyautogui.click()

    def add_status_type_cancellation_of_licence(self, discontinuation_date: str, isGowling: bool):
        tracking_status_area_coord = search_for_image(self.tracking_status_area_img)
        # empty_field_coord = search_for_image(self.tracking_status_status_type_empty_field_img, confidence=0.96)
        pyautogui.moveTo(tracking_status_area_coord)
        time.sleep(0.5)
        pyautogui.move(0, 35)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)

        while True:
            tracking_status_error_coord = search_for_image(self.tracking_status_error_img, times_to_search=2, quit_program=False, wait_time=1)
            if tracking_status_error_coord is None:
                pyautogui.press("down")
            else:
                pydirectinput.press("enter")
                break

        d1 = datetime.datetime.now()
        time.sleep(0.5)
        pyautogui.write("Cancellation of licence", interval=0.05)
        pydirectinput.press("enter")
        time.sleep(0.5)
        pydirectinput.press("tab")
        time.sleep(0.5)
        pydirectinput.press("tab")
        time.sleep(0.5)
        d2 = datetime.datetime.now()
        print(d2)
        # Need to wait so at least 1 minute has gone by between start and end date
        while str(d1).split(" ")[1][:5] == str(d2).split(" ")[1][:5]:
            time.sleep(5)
            d2 = datetime.datetime.now()
        time.sleep(1)

        split_time = str(d2).split(" ")
        formatted_time = f"{split_time[0]}/{split_time[1][:5]}"
        pyautogui.write(formatted_time, interval=0.05)
        time.sleep(0.5)
        pydirectinput.press("tab")
        time.sleep(0.5)

        if isGowling:
            pyautogui.write(f"Discontinuation requested by licensee on {discontinuation_date}. Notice sent via Titan.", interval=0.05)
        else:
            pyautogui.write(f"Discontinuation requested by licensee on {discontinuation_date}. Notice sent via ePost.", interval=0.05)
        self.menubar.save()










