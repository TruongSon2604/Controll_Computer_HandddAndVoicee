import cv2
import time
import os
import Main.hand as htm
import autopy
import mouse
import math
import pygame
import numpy as np
import  pyautogui


from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()
print(f"Volrange:{volRange}")
minvol= volRange[0]
maxvol=volRange[1]

pTime=0
# url="http://127.0.0.1:5000/"
url="http://192.168.137.161:5000"
cap= cv2.VideoCapture(url)
FolderPath="Fingers"
lst=os.listdir(FolderPath)
lst2=[]
for i in lst:
    image=cv2.imread(f"{FolderPath}/{i}")
    lst2.append(image)

detector=htm.handDetector(detectionCon=1) #tao mot doi tuong detector tu lop hand.py
fingerId= [4,8,12,16,20] #cac dau ngon tay

while True:
    ret,frame=cap.read()
    heighFrame,widthFrame,_=frame.shape
    frame=detector.findHands(frame)
    lmList= detector.findPosition(frame,draw=False) #phat hien vi tri
    if len(lmList) != 0 :
        x0,y0 = lmList[8][1],lmList[8][2]
        x1,y1 = lmList[4][1],lmList[4][2]
        length = math.hypot(x1-x0,y1-y0)
        if length<20:
            mouse.click('left')


    print(lmList)

   



   
    if len(lmList)!=0:
        # autopy.mouse.move(0,0)
        mangngontay=[]
         #viet cho cac ngon cai 
        # if lmList[fingerId[0]][1] <lmList[fingerId[0]-1][1] :#so sanh 4 voi 3
        #     mangngontay.append(1)
        # else: mangngontay.append(0)
         #viet cho ngon dai  , (0-4) ngon cai , (5-8) tro,9-12 ngon giua ,13-16 ngon ke , 17-20 ngon ut mang lmlist la 3 chieu (sothutungon,toa do x tang tu trai sang phai, toa do y huong xuong tang dan)
        for id in range(1,5):
            if  lmList[fingerId[id]][2] <lmList[fingerId[id]-1][2] :  
                mangngontay.append(1)
            else:
                mangngontay.append(0)      
        songontay=mangngontay.count(1)


        if(int(songontay)==1):
            h, w, c = lst2[int(songontay - 1)].shape
            cv2.putText(frame,"Chuc nang di chuyen chuot",(150,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3)
            h, w, c = lst2[int(songontay - 1)].shape
            frame[0:h, 0:w] = lst2[int(songontay - 1)]
            pointx,pointy=lmList[8][1],lmList[8][2]
            pygame.init()

            # Lấy thông tin về màn hình
            screen_info = pygame.display.Info()
            screen_width = screen_info.current_w-100
            screen_height = screen_info.current_h-100

            pX= int((screen_width//widthFrame)*pointx)
            pY=int((screen_height//heighFrame)*pointy)
            #1500,850

            if(pX<1500 and pY<850  and pY>=0 and pX>=0):
                autopy.mouse.move(pX,pY)
            else:
                cv2.putText(frame,"Xin vui long di chuyen tay vao camera",(150,70),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),3)



            # cv2.rectangle(frame, (0, h + 20), (150, 400), (0, 255, 0), -1)
            # cv2.putText(frame, str(songontay), (30, 200), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 0, 0), 3)

        elif int(songontay)==2:

            h, w, c = lst2[int(songontay - 1)].shape
            cv2.putText(frame, "Chuc nang click", (150, 70), cv2.Formatter_FMT_MATLAB, 2,(0,255,0),3)
            frame[0:h, 0:w] = lst2[int(songontay - 1)]


            x0,y0 = lmList[8][1],lmList[8][2]
            x1,y1 = lmList[4][1],lmList[4][2]
            length = math.hypot(x1-x0,y1-y0)
            if length<20:
                mouse.click('left')
            x2,y2 = lmList[12][1],lmList[12][2]
            length2= math.hypot(x1-x2,y1-y2)
            print(f"Day la leng2:{length2}")
            if length2<20 :
                pyautogui.rightClick()
            # cv2.rectangle(frame, (0, h + 20), (150, 400), (0, 255, 0), -1)
            # cv2.putText(frame, str(songontay), (30, 200), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 0, 0), 3)
        elif int(songontay)==3:
            x1,y1=lmList[4][1], lmList[4][2]
            x2,y2=lmList[8][1], lmList[8][2]
            cv2.circle(frame,(x1,y1),10,(0,0,0),-1)
            cv2.circle(frame,(x2,y2),10,(0,0,0),-1)
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,0),4)
            cx,cy= (x1+x2)//2, (y1+y2)//2
            cv2.circle(frame,(cx,cy),10,(0,0,0),-1)

            #do dai toi thieu khi mo la 230 den khi dong la 18
            length= math.hypot(x2-x1,y2-y1)


            #amthanh  chay tu -64 den 0
                # chuyen chieu dai cua ngon tay cai tu 20-230 bien doi theo -64 den 0
            vol= np.interp(length,[19,150],[minvol,maxvol])
            volbar= np.interp(length,[19,150],[450,150])
            text = int ( np.interp(length,[19,150],[0,100]))
            print(text)
            vb=  int(volbar)
            
        
            volume.SetMasterVolumeLevel(vol, None)
            
            if length< 25:
                cv2.circle(frame,(x1,y1),10,(255,0,0),-1)
            cv2.rectangle(frame,(50,150),(100,450),(0,255,0),3)
            cv2.rectangle(frame,(50,vb),(100,450),(0,255,0),-1)
            cv2.putText(frame,f"{str(text)}",(100,200),3,3,(0,255,0),3)
        # h,w,c= lst2[int(songontay-1)].shape
        # frame[0:h,0:w]=lst2[int(songontay-1)]
        # cv2.rectangle(frame,(0,h+20),(150,400),(0,255,0),-1)
        # cv2.putText(frame,str(songontay),(30,200),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,0,0),3)
    #show fps
    cTime=time.time()
    fps= 1/(cTime-pTime) #tinh fps tren khung hinh 
    pTime=cTime

    #show fps tren man hinh'
    # cv2.putText(frame,f"FPS:{int(fps)}",(150,70),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),3)



    cv2.imshow("cuaso",frame)
    if(cv2.waitKey(1) == ord("q")) : break

cap.release
cv2.destroyAllWindows    

