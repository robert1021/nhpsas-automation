import pyautogui
import time
import sys
import os
import openpyxl


def get_frozen_status() -> bool:
    """
    Check if the current Python environment is frozen.

    :return: True if the environment is frozen (e.g., packaged into an executable), False otherwise.
    """
    if getattr(sys, "frozen", False):
        return True
    else:
        return False


def terminate_program(message: str):
    print(message)
    sys.exit()


def search_for_image(image: str, confidence=0.85, grayscale=False, wait_time=3, times_to_search=20, quit_program=True):
    search_count = 0
    print("Searching...")
    coords = pyautogui.locateCenterOnScreen(image, confidence=confidence, grayscale=grayscale)
    search_count += 1
    if pyautogui.position() == (0, 0):
        terminate_program("Failsafe triggered...")
    while not coords:
        time.sleep(wait_time)
        print("Searching...")
        coords = pyautogui.locateCenterOnScreen(image, confidence=confidence, grayscale=grayscale)
        search_count += 1
        if pyautogui.position() == (0, 0):
            terminate_program("Failsafe triggered...")
        elif not coords and search_count == times_to_search:
            if quit_program:
                terminate_program("Exiting...")
            return coords
    print("Found!")
    return coords


def load_column_from_excel(path, column_name) -> list:
    submissions = []
    # Load the Excel file
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active  # Select the active sheet, or you can specify a sheet by name

    submission_idx = 0
    # Iterate through the rows
    for row_num, row in enumerate(sheet.iter_rows(values_only=True)):
        if row_num == 0:
            if column_name not in row:
                raise Exception(f"{column_name} column not found")

            submission_idx = row.index(column_name)
            continue

        submissions.append(row[submission_idx])

    return submissions
