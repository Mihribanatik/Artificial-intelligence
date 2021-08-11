# -*- coding: utf-8 -*-
"""

import cv2

import numpy as np




img=cv2.imread("serit.png")

img_gri=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur=cv2.medianBlur(img_gri, 5)

img_canny=cv2.Canny(img_blur,10,200)


istenilen_alan =np.array([[(10,300),(45,140),(155,140),(205,300)]],np.int32)

x, y = img.shape[:2]

mask = np.zeros(shape = (x,y), dtype=np.uint8) #resimle aynı boyutlarda binary görüntü oluşturma.

mask = cv2.fillPoly(mask, istenilen_alan, 255) #binary görüntü istenilen alan seçme



mask2 = cv2.bitwise_and(img_canny,mask) 




cv2.imshow("mask",mask)
cv2.imshow("mask2",mask2)
cv2.imshow("orijinal",img)
cv2.imshow("img_canny",img_canny)


cv2.waitKey(0)

cv2.destroyAllWindows()



import cv2
import matplotlib.pyplot as plt 

img=cv2.imread("img/ucak.png")



kirp=img[500:800,500:800] #kirptiğim aln

img[107:207,207:307]=kirp

plt.subplot(121)
plt.imshow(img,"gray")

plt.subplot(122)
plt.imshow(kirp,"gray")
plt.show()


b,g,r=cv2.split(img) #renk kanallarına ayırmak

b=img[:,:,0]


plt.subplot(121)
plt.imshow(b)

img[:,:,1]=0

plt.subplot(121)
plt.imshow(img)

plt.show()
 #istediğim renk kanalından kurtukmak

#b,g,r=cv2.merge((b,g,r)) #renk kanallarına birlestirir



cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
import cv2

img1=cv2.imread("img/OpenCV.png")
img2=cv2.imread("img/ucak.png")

x,y,z=img1.shape

roi=img2[0:x,0:y]


img1_gri=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)



ret,mask= cv2.threshold(img1_gri,20,255,cv2.THRESH_BINARY)



mask_inv=cv2.bitwise_not(mask)


img_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img_fg=cv2.bitwise_and(img1,img1,mask=mask)

toplam=cv2.add(img_bg,img_fg)

img2[0:x,0:y]=toplam



cv2.imshow("roi",roi)
cv2.imshow("maskinv",mask_inv)
cv2.imshow("mask",mask)
cv2.imshow("img2",img2)
cv2.imshow("img1",img1)


cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np


cam=cv2.VideoCapture(0)


def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame",0,359,nothing)
cv2.createTrackbar("H2","frame",0,359,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,255,nothing)
cv2.createTrackbar("V2","frame",0,255,nothing)


while cam.isOpened():
    
    _,frame=cam.read()
    
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    H1=int(cv2.getTrackbarPos("H1","frame") / 2)
    H2=int(cv2.getTrackbarPos("H2","frame") / 2)
    S1=cv2.getTrackbarPos("S1","frame")
    S2=cv2.getTrackbarPos("S2","frame")
    V1=cv2.getTrackbarPos("V1","frame")
    V2=cv2.getTrackbarPos("V2","frame")
    
    lover=np.array([H1,S1,V1])
    upper=np.array([H2,S2,V2])
    
    mask=cv2.inRange(hsv,lover,upper)  #bu aralıktakileri beya diğerlerini siyah  yapar
    
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    
    



    cv2.imshow("frame",frame)
    cv2.imshow("hsv",hsv)
    cv2.imshow("res",res)
    



    if cv2.waitKey(5) & 0xff == ord("q"):
        
        print("video kapatıldı")
        break
    
cam.release()

cv2.destroyAllWindows()

"""






























