# -*- coding: utf-8 -*-

import cv2

import numpy as np


cam = cv2.VideoCapture("0")


#EĞİM HESABI##   M<0 İSE SOL M>0 İSE SAĞ


def line_mean(lines):
    left = []
    right = []
    
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        slope = (y2-y1)/(x2-x1)
        
        if slope < 0:
            right.append((x1,y1,x2,y2))
            
        elif slope > 0:
            left.append((x1,y1,x2,y2))
            
        right_mean = np.mean(right, axis=0)
        left_mean = np.mean(left, axis=0)
        
        
    if not isinstance(right_mean, type(np.nan)):
        if not isinstance(left_mean, type(np.nan)):
            return right_mean, left_mean
        else:
            return right_mean, None
    else:
        if not isinstance(left_mean, type(np.nan)):
            return None, left_mean
        else:
            return None, None
        
    
while cam.isOpened():
    
    ret, frame = cam.read()
    if not ret:
        print("bitti")
        break
    
    
    
    img_gri=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_blur=cv2.GaussianBlur(img_gri, 5)
    
    img_canny=cv2.Canny(img_blur,10,200)
    
    
    istenilen_alan =np.array([[(10,300),(45,140),(155,140),(205,300)]],np.int32)
    
    x, y = img.shape[:2]
    
    mask = np.zeros(shape = (x,y), dtype=np.uint8) #resimle aynı boyutlarda binary görüntü oluşturma.
    
    mask = cv2.fillPoly(mask, istenilen_alan, 255) #binary görüntü istenilen alan seçme
    mask2 = cv2.bitwise_and(img_canny,mask) 
    
    lines = cv2.HoughLinesP(img, 1, np.pi/180, 20, 
                            minLineLength = 5, maxLineGap = 200)
    
    
    
    if lines is not None:
        right_line, left_line = line_mean(lines)
        if right_line is not None:
            image = draw_line(image, right_line)
        if left_line is not None:
            image = draw_line(image, left_line)
            
            line_mean(lines)
        
     

    cv2.imshow("image",frame)
    cv2.imshow("img",img)
    
    key = cv2.waitKey(16) & 0xFF
    if key == ord("q"):
        print("kapatıldı")
        break



cam.release()
cv2.destroyAllWindows()