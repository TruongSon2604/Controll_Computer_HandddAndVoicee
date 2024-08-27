import math
import pygame
import numpy as np
import pyautogui
import comtypes
import cv2
import time
def initialize_com():
    comtypes.CoInitialize()

def uninitialize_com():
    comtypes.CoUninitialize()

def control_computer(lmList):
    pygame.init()
    initialize_com()
    try:
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)
        #volume.GetMute()
        #volume.GetMasterVolumeLevel()
        volRange = volume.GetVolumeRange()
        print(f"Volrange: {volRange}")
        minvol = volRange[0]
        maxvol = volRange[1]
        widthFrame = 1280
        heightFrame = 720
        fingerId = [4, 8, 12, 16, 20]  # Các điểm ngón tay
        if len(lmList) != 0:
            mangngontay = []
            if lmList[fingerId[0]][1] <lmList[fingerId[0]-1][1] :#so sanh 4 voi 3
                mangngontay.append(1)
            else: 
                mangngontay.append(0) 
            
            for id in range(1, 5):
                if lmList[fingerId[id]][2] < lmList[fingerId[id] - 1][2]:
                    mangngontay.append(1)
                else:
                    mangngontay.append(0)
            songontay = mangngontay.count(1)

            if int(songontay) == 1:
                print('Di chuyen chuot')
                pointx, pointy = lmList[8][1], lmList[8][2]
                pygame.init()
                # Lấy thông tin về màn hình
                screen_info = pygame.display.Info()
                screen_width = screen_info.current_w 
                screen_height = screen_info.current_h 
                pX = int((screen_width // widthFrame) * pointx)
                pY = int((screen_height // heightFrame) * pointy)

                try:
                    if 0 <= pX < screen_width and 0 <= pY < screen_height:
                        pyautogui.moveTo(pX, pY)
                except pyautogui.FailSafeException:
                    print("The mouse cursor is out of the screen boundaries.")

            elif int(songontay) == 2:
                x0, y0 = lmList[8][1], lmList[8][2]
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[12][1], lmList[12][2]
                length = math.hypot(x1 - x0, y1 - y0)
                length2 = math.hypot(x1 - x2, y1 - y2)
                if length < 20:
                    print('Kich chuot trai')
                    pyautogui.click(button='left')
                    
                
                
                if length2 < 20:
                    print('kich chuot phai')
                    pyautogui.click(button='right')
                    

            elif int(songontay) == 3:
                # print('thay doi vol')
                # x1, y1 = lmList[4][1], lmList[4][2]
                # x2, y2 = lmList[8][1], lmList[8][2]
                # length = math.hypot(x2 - x1, y2 - y1)
                # vol = np.interp(length, [19, 150], [minvol, maxvol])
                # text = int(np.interp(length, [19, 150], [0, 100]))
                
                # try:
                #     pyautogui.moveTo(50, 150 + vol * 3)  # Simulate moving the volume slider
                #     pyautogui.click()  # Simulate clicking on the volume slider
                # except pyautogui.FailSafeException:
                #     print("The mouse cursor is out of the screen boundaries.")
                x1,y1=lmList[4][1], lmList[4][2]
                x2,y2=lmList[8][1], lmList[8][2]
                # cv2.circle(frame,(x1,y1),10,(0,0,0),-1)
                # cv2.circle(frame,(x2,y2),10,(0,0,0),-1)
                # cv2.line(frame,(x1,y1),(x2,y2),(0,0,0),4)
                # cx,cy= (x1+x2)//2, (y1+y2)//2
                # cv2.circle(frame,(cx,cy),10,(0,0,0),-1)

                #do dai toi thieu khi mo la 230 den khi dong la 18
                length= math.hypot(x2-x1,y2-y1)


                #amthanh  chay tu -64 den 0
                    # chuyen chieu dai cua ngon tay cai tu 20-230 bien doi theo -64 den 0
                vol= np.interp(length,[19,150],[minvol,maxvol])
                volbar= np.interp(length,[19,150],[450,150])
                text = int ( np.interp(length,[19,150],[0,100]))
                print(text)
                vb=  int(volbar)
                # autopy.mouse.move(5,5)
            
                volume.SetMasterVolumeLevel(vol, None)
                
                # if length< 25:
                #     cv2.circle(frame,(x1,y1),10,(255,0,0),-1)
                # cv2.rectangle(frame,(50,150),(100,450),(0,255,0),3)
                # cv2.rectangle(frame,(50,vb),(100,450),(0,255,0),-1)
                # cv2.putText(frame,f"{str(text)}",(100,200),3,3,(0,255,0),3)
            elif int(songontay) == 4:
                pyautogui.scroll(-100)
                # Chờ 1 giây
                time.sleep(1)
            elif int(songontay) == 5:
                pyautogui.scroll(100)
                # Chờ 1 giây
                time.sleep(1)

    finally:
        uninitialize_com()
