# -*- coding: utf-8 -*-
"""
@author: Mustafa Ünlü
@instagram: mmustafaunluu
@youtube: Kendi Çapında Mühendis
"""


import cv2
import numpy as np

cam=cv2.VideoCapture("img/car8.mp4")
sapma=100
kernel=np.ones((3,3),np.uint8)


def crop_alan(img):
    x,y=img.shape[:2]
    
    alan=np.array([[(sapma,x-sapma),(int(y*3/8),int(x*0.6)),(int(y*5/8),int(x*0.6)),(y,x-sapma)]])
    
    return alan

def crop_alan_mask(img,alan):
    
    x,y=img.shape[:2]
    
    mask=np.zeros((x,y),np.uint8)
    mask=cv2.fillPoly(mask,alan,255)
    
    mask=cv2.bitwise_and(img,img,mask=mask)
    
    return mask
    

def filt(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.inRange(img,150,255)
    img=cv2.erode(img,kernel)
    img=cv2.dilate(img,kernel)
    img=cv2.medianBlur(img,9)
    img=cv2.Canny(img,210,240)
    
    return img



def line_mean(lines):
    left=[]
    right=[]
    
    for line in lines:
        for x1,y1,x2,y2 in line:
            
            m=(y2-y1)/(x2-x1)
            
            if m < -0.2:
                right.append((x1,y1,x2,y2))
            elif m > 0.2:
                left.append((x1,y1,x2,y2))
        right_mean = np.mean(right,axis=0)       
        left_mean = np.mean(left,axis=0)
        
        if not isinstance(right_mean, type(np.nan)):
            if not isinstance(left_mean, type(np.nan)):
                return right_mean,left_mean
            else:
                return right_mean ,None
        else:
            if not isinstance(left_mean, type(np.nan)):
                return left_mean,None
            else:
                return None,None

def draw_line(img,line):
    line=np.int32(np.around(line)) #tam sayıya yuvarladım
    x1,y1,x2,y2=line
    
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),10)
    
    return img

while cam.isOpened():
    
    ret, image = cam.read()
    
    image_org=image.copy()
    
    if not ret:
        print("bitti")
        break
    cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    cv2.namedWindow("img",cv2.WINDOW_NORMAL)
    alan=crop_alan(image)
    img=crop_alan_mask(image,alan )
    img=filt(img)
    
    
    lines=cv2.HoughLinesP(img,1,np.pi/180,10,minLineLength=5, maxLineGap=100)
   
    if lines is not None:
        
        right_mean , left_mean=line_mean(lines)
        if right_mean is not None:
            image=draw_line(image,right_mean)
        if left_mean is not None:
            image=draw_line(image,left_mean)
        
        
        
        
    cv2.imshow("image",image)   
    cv2.imshow("img",img)
    
    
    key = cv2.waitKey(16) & 0xFF
    if key == ord("q"):
        print("kapatıldı")
        break


cam.release()
cv2.destroyAllWindows()