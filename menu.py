import pyautogui
from utilities import search_for_image
from config import *


class Menu:

    def __init__(self):
        self.run_module_img = os.path.join(image_path, "nhpsas_menu", "run_module_btn.PNG")
        self.submission_module_img = os.path.join(image_path, "nhpsas_menu", "submission_module.PNG")
        self.tracking_module_img = os.path.join(image_path, "nhpsas_menu", "tracking_module.PNG")
        self.product_module_img = os.path.join(image_path, "nhpsas_menu", "product_module.PNG")
        self.site_module_img = os.path.join(image_path, "nhpsas_menu", "site_module.PNG")
        self.application_user_module_img = os.path.join(image_path, "nhpsas_menu", "application_user_module.PNG")
        self.company_module_img = os.path.join(image_path, "nhpsas_menu", "company_module.PNG")
        self.ingredient_module_img = os.path.join(image_path, "nhpsas_menu", "ingredient_module.PNG")
        self.licenced_products_module_img = os.path.join(image_path, "nhpsas_menu", "licenced_products_module.PNG")
        self.lookup_module_img = os.path.join(image_path, "nhpsas_menu", "lookup_module.PNG")
        self.nmi_names_module_img = os.path.join(image_path, "nhpsas_menu", "nmi_names_module.PNG")

    def click_run_module_btn(self):
        run_module_btn_coord = search_for_image(self.run_module_img)
        pyautogui.moveTo(run_module_btn_coord)
        pyautogui.click()

    def open_submission_module(self):
        submission_module_coord = search_for_image(self.submission_module_img, grayscale=True)
        pyautogui.moveTo(submission_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_tracking_module(self):
        tracking_module_coord = search_for_image(self.tracking_module_img, grayscale=True)
        pyautogui.moveTo(tracking_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_product_module(self):
        product_module_coord = search_for_image(self.product_module_img, grayscale=True)
        pyautogui.moveTo(product_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_site_module(self):
        site_module_coord = search_for_image(self.site_module_img, grayscale=True)
        pyautogui.moveTo(site_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_application_user_module(self):
        application_user_module_coord = search_for_image(self.application_user_module_img, grayscale=True)
        pyautogui.moveTo(application_user_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_company_module(self):
        company_module_coord = search_for_image(self.company_module_img, grayscale=True)
        pyautogui.moveTo(company_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_ingredient_module(self):
        ingredient_module_coord = search_for_image(self.ingredient_module_img, grayscale=True)
        pyautogui.moveTo(ingredient_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_licenced_products_module(self):
        licenced_products_module_coord = search_for_image(self.licenced_products_module_img, grayscale=True)
        pyautogui.moveTo(licenced_products_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_lookup_module(self):
        lookup_module_coord = search_for_image(self.lookup_module_img, grayscale=True)
        pyautogui.moveTo(lookup_module_coord)
        pyautogui.click()
        self.click_run_module_btn()

    def open_nmi_names_module(self):
        nmi_names_module_coord = search_for_image(self.nmi_names_module_img, grayscale=True)
        pyautogui.moveTo(nmi_names_module_coord)
        pyautogui.click()
        self.click_run_module_btn()
