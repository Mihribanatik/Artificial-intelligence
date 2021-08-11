# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import mihriban

"""
resim=cv2.imread("OpenCV.png",0)

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)

####eşik deger belirleme#####

_,resim_tresh1=cv2.threshold(resim,20,255,cv2.THRESH_BINARY)

_,resim2_thres=modul.threshold (resim,20,255)


cv2.imshow("resim" ,resim)
cv2.imshow("resimtreh",resim_tresh)
cv2.imshow("resim2thresh",resim2_thres)





cv2.waitKey()
cv2.destroyAllWindows()
"""


"""

resim=cv2.imread("th2resim.png",0)
_,resim_tresh1=cv2.threshold(resim,20,255,cv2.THRESH_BINARY)
_,resim_tresh2=cv2.threshold(resim,20,255,cv2.THRESH_BINARY_INV)
_,resim_tresh3=cv2.threshold(resim,20,255,cv2.THRESH_TRUNC)
_,resim_tresh4=cv2.threshold(resim,20,255,cv2.THRESH_TOZERO)
_,resim_tresh5=cv2.threshold(resim,20,255,cv2.THRESH_TOZERO_INV)



resimler=[resim_tresh1,resim_tresh2,resim_tresh3,resim_tresh4,resim_tresh5,resim]
basliklar=["THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV","original"]
#subplot(satır,sutun,resimnumarası) bu tek bir grafikte butun resimleri gösteriri

for i in range(6):
    plt.subplot(2, 3,i+1),plt.imshow(resimler[i],"gray")
    plt.title(basliklar[i])
    
    
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()


"""

#^###############trecbar kullanarak eşikleme################333


resim=cv2.imread("th2resim.png",0)

def nothing(x):
    pass

cv2.namedWindow("resim")
cv2.createTrackbar("esik","resim",0,255,nothing)


while (1):
    thresh=cv2.getTrackbarPos("esik","resim")
    _,threshold_img=cv2.threshold(resim,thresh,255,cv2.THRESH_BINARY)
    
    
    cv2.imshow("resim",resim)
    cv2.imshow("treshold",threshold_img)
    
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
cv2.destroyAllWindows()










