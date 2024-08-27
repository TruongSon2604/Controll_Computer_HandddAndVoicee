import sys
import re
import json
import threading
import cv2
sys.path.insert(0,'Model')
import hand as htm
import os
import numpy as np
import speech_recognition as sr
import socket
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_audio():
    print('STart :')
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=3) # thu âm trong 5 giây
        try:
            text = r.recognize_google(audio, language="vi-VN") # chuyển âm thanh thành văn bản
            print(text)
            return text
        except:
            return None 
def AnalysisSound(request):
    # mở website
    with open('Resource/requestWebsite.json', encoding='utf-8') as file:
        data = json.load(file)

    for website, phrases in data.items():
            for p in phrases[0]:
                if p in request and phrases[1][0] in request:
                    if len(phrases[2]) != 0:
                        HasCancel = False
                        Cancel = ''
                        for cancel in phrases[2]:
                            if cancel in request:
                                print(cancel)
                                HasCancel = True
                                Cancel = cancel
                        if HasCancel :
                            return 'mở '+website+" và tìm kiếm" + request.split(Cancel)[1]
                        else :
                            return 'mở web '+website 
                    else :
                        return 'mở web '+website 
                    
    # mở cài đặt 
    with open('Resource/requestCMD.json', encoding='utf-8') as file:
        dataSetting = json.load(file)
    for app, phrases in dataSetting.items():
            for p in phrases[0]:
                if p in request and phrases[1][0] in request:
                    return app
    # ứng dụng và chức năng trên máy 
    with open('Resource/requestFunction.json', encoding='utf-8') as file:
        dataFunction= json.load(file)
    for function, phrases in dataFunction.items():
            if len(phrases[1]) != 0 :
                for p in phrases[0]:
                    if p in request :
                        for idx in phrases[1]:
                            if idx in request:
                                numbers = re.findall(r'\d+', request)
                                number =  [int(num) for num in numbers]
                                return f"{function} {number}".replace("[", "").replace("]", "")
            else :
                for p in phrases[0]:
                    if p in request :
                        return function
    return "Error"

def request_chatbot(client_socket):
    while True:
        try:
            request = get_audio()
            while request == "" or request == None:
                request = get_audio()
            request = request.lower()
            message = AnalysisSound(request) +" Message "+request
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print("Tin nhắn từ server:", data)
        except:
            print('')

def request_hand(client_socket):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    ul="http://192.168.137.228:5000"
    cap= cv2.VideoCapture(0)
    FolderPath="Fingers"
    lst=os.listdir(FolderPath)
    lst2=[]
    for i in lst:
        image=cv2.imread(f"{FolderPath}/{i}")
        lst2.append(image)
    detector=htm.handDetector(detectionCon=1) # tạo một đối tượng detector từ lớp hand.py
# Phát hiện và gửi dữ liệu
    while True:
        ret, frame = cap.read()
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame, draw=False)  # phát hiện vị trí
        print(lmList)
        if len(lmList) != 0:
            # Chuyển lmList thành chuỗi JSON
            lmList_json = json.dumps(lmList)
            # Gửi chuỗi JSON qua client_socket
            client_socket.send(lmList_json.encode())
        # cv2.imshow("cuaso",frame)

        # print(lmList)   
    
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
print('da ket noi toi server')
rq_chatbot = threading.Thread(target=request_chatbot, args=(client_socket,))
rq_chatbot.start()
rq_hand  = threading.Thread(target=request_hand(client_socket))
rq_hand.start()


client_socket.close()
            

