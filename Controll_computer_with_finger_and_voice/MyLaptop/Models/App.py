import os
import time
import fnmatch
from comtypes import CLSCTX_ALL
import subprocess
import logging
import pyautogui
logging.basicConfig(level=logging.WARNING)
#mở 1 app
def search_on_start_menu(query):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write(query)
    time.sleep(1)
    pyautogui.press('enter')


