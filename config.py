from utilities import get_frozen_status
import os
import sys


image_path = os.path.join(sys._MEIPASS, "images") if get_frozen_status() is True else "images"
