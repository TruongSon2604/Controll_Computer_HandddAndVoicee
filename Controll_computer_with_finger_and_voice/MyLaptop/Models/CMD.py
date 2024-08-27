import subprocess
import tkinter as tk
import os
import logging
import json
logging.basicConfig(level=logging.WARNING)

def getCMD(value):
    with open('Resource/dict_cmd.json', encoding='utf-8') as file:
        data = json.load(file)

    if value in data:
        query = data[value]
        if " " in query[0]:
            query = query[0].split(" ")
        else:
            query = query[0]
    return query

def OpenSetting(value):
    value = value.lower()
    value = getCMD(value)
    try:
        if len(value) == 2:
            subprocess.run([value[0], value[1]], shell=True)
        else :
            subprocess.run(value, shell=True)
    except Exception as e:
        logging.warning('Error : open setting')
