# -*- coding: utf-8 -*-

import cv2
import  numpy as np

cam=cv2.VideoCapture("img/car8.mp4")

kernel = np.ones((3,3),dtype=np.uint8)
while cam.isOpened():
    ret,frame=cam.read()
    
    
    
    if not ret:
        print("video bitti")
        break
    
    #boyutlar x,y =540,960  trsine işlem yap
    alan=np.array([[(90,520),(390,320),(600,320),(800,520)]],np.int32) #video larda x si y y yi x gibi düşün boyut olarak
    mask = np.zeros((540,960), dtype=np.uint8)
    
    mask = cv2.fillPoly(mask, alan, 255)
    mask = cv2.bitwise_and(frame,frame, mask=mask)
    
    img = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    img = cv2.inRange(img, 200, 255)
    img = cv2.erode(img, kernel)
    img = cv2.dilate(img, kernel)
    img = cv2.medianBlur(img, 9)
    
    edges=cv2.Canny(img,200,210)
    
    

    
    
    key=cv2.waitKey(16) & 0xff
    
    if key == ord("q"):
        print("kapatıldı")
        break
    
        
    cv2.imshow("mask",edges)

cam.release()
cv2.destroyAllWindows()
