# -*- coding: utf-8 -*-


import cv2
import numpy  as  np


cam=cv2.VideoCapture(0)


def nothing(x):
    pass

cv2.namedWindow("frame")

cv2.createTrackbar("h1","frame",0,255,nothing)
cv2.createTrackbar("h2","frame",0,255,nothing)
cv2.createTrackbar("s1","frame",0,255,nothing)
cv2.createTrackbar("s2","frame",0,255,nothing)
cv2.createTrackbar("v1","frame",0,255,nothing)
cv2.createTrackbar("v2","frame",0,255,nothing)


while cam.isOpened():
    
    _,frame=cam.read()
    
    
    
    
    
   #hangi rengi geçirsinnnn    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   
    h1=cv2.getTrackbarPos("h1","frame")
    h2=cv2.getTrackbarPos("h2","frame")
    s1=cv2.getTrackbarPos("s1","frame")
    s2=cv2.getTrackbarPos("s2","frame")
    v1=cv2.getTrackbarPos("v1","frame")
    v2=cv2.getTrackbarPos("v2","frame")
    
    
    lower=np.array([h1,s1,v1])
    upper=np.array([h2,s2,v2])
    
    mask= cv2.inRange(hsv,lower,upper)
    
    
    """
    renlerin aralıklarını bulma terminele yaz
    
    yesil=np.uint8([[[0,255,0]]])
    yesil_hsv=cv2.cvtColor(yesil,cv2.COLOR_BGR2HSV)
    """
    cv2.imshow("goruntu",frame)
    cv2.imshow("HSV",mask)
   
    
    
    
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        print("görüntü kapandı")
        break


cam.release()
cv2.destroyAllWindow()



















"""    
# ########resim üzerinden hsv###############

import cv2
from  matplotlib import pyplot as plt
import numpy as np

resim=cv2.imread("ucak.png")  #resmi acar 0 siyah beyaz açar

hsv=cv2.cvtColor(resim,cv2.COLOR_BGR2HSV)
    
cv2.imshow("ucak",resim)
    
lower=np.array([50,200,150])
upper=np.array([90,255,255])
    
mask= cv2.inRange(hsv,lower,upper)
res=cv2.bitwise_and(resim,resim,mask=mask)

#cv2.imshow("hsv",hsv)
cv2.imshow("mask",mask)
cv2.imshow("res",res)


k=cv2.waitKey()

if k==ord("q"):
    print("resim kapandı")
    

cv2.destroyAllWindows()
"""