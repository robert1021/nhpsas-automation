import subprocess
import shutil
import os

if __name__ == "__main__":
    try:
        process = subprocess.run([
            "pyinstaller",
            "--onefile",
            "--add-data", "images;images",
            "--add-data", r"utilities.py;.",
            "--add-data", r"config.py;.",
            "--add-data", r"login.py;.",
            "--add-data", r"menu.py;.",
            "--add-data", r"menu_bar.py;.",
            "--add-data", r"submission_module.py;.",
            "--add-data", r"tracking_module.py;.",
            "--hidden-import=openpyxl",
            "--hidden-import=pyautogui",
            "--hidden-import=pydirectinput",
            "main.py"
        ], text=True, check=True)

        shutil.rmtree("build")
        os.remove("main.spec")
        os.rename("dist/main.exe", f"NHPSAS Discontinuation Bot.exe")
        shutil.rmtree("dist")

    except Exception as e:
        print("Error:", e)