import eel
import os
import threading
from queue import Queue
import time
import json
import numpy as np
class ChatBot:
    started = False
    userinputQueue = Queue()

    @staticmethod
    def isUserInput():
        return not ChatBot.userinputQueue.empty()

    @staticmethod
    def popUserInput():
        return ChatBot.userinputQueue.get()

    @staticmethod
    def close_callback(route, websockets):
        exit()
    @staticmethod
    def close():
        ChatBot.started = False
    @staticmethod
    @eel.expose
    def postDataToSetting():
        with open('Resource/dict_website.json', encoding='utf-8') as file:
            data = json.load(file)
        return data
        
    @staticmethod
    def start():
        path = os.path.dirname(os.path.abspath(__file__))
        eel.init(path + r'\web', allowed_extensions=['.js', '.html'])
        try:
            eel.start('Setting.html', mode='chrome',
                                    host='localhost',
                                    port=27006,
                                    block=False,
                                    size=(350, 480),
                                    position=(10,100),
                                    disable_cache=True,
                                    close_callback=ChatBot.close_callback)
            ChatBot.started = True
            while ChatBot.started:
                try:
                    eel.sleep(10.0)
                except:
                    #main thread exited
                    break
        
        except:
            pass

if __name__ == "__main__":
    ChatBot.start()
