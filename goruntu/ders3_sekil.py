# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)


cv2.line(img,(0,0),(200,300),(255,0,0),5)
# cv2.rectangle(img,(220,220),(330,330),(255,250,0),15) #-1 yazarsam içini doldurur
# cv2.circle(img,(100,100),80,(250,15,0),-1)


font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"opencv",(10,400),font,4,(0,155,255),2,cv2.LINE_AA)

cv2.imshow("resim",img)

cv2.waitKey(0)

cv2.destroyAllWindows()