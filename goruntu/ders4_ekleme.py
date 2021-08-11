# -*- coding: utf-8 -*-
"""
import cv2
import numpy as np

img1=cv2.imread("img/ucak.png")
img2=cv2.imread("img/1.jpg")


topla=cv2.addWeighted(img1,0.2,img2,0.8,0) #(iki resmi isimlerini ve ne kadarlık ekleyecegimi verdim ve topladı)

cv2.imshow("resim",topla)

cv2.waitKey(0)
cv2.destroyAllWindows()

###############ekleme islemi###############
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt




img1=cv2.imread("img/ucak.png")
img2=cv2.imread("img/OpenCV.png")

#resmin boyutlatını shape ile ögrendim bi alanı kırpmak için kullnıcam

x,y,z=img2.shape
roi=img1[0:x,0:y]

img2gri=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) #GRİLEŞTİRDİM
#cv2.imshow("img2gri",img2gri)


ret,mask=cv2.threshold(img2gri,20,255,cv2.THRESH_BINARY) 
#threshol ile eşikleme yaptım dedimki 20 pikselin üzerindeki tüm pikselleri beyaz yap siyah beyaz yapmak için


#0 ları 1 birleri 0 tersleme işlemi bitwise_not()
mask_inv= cv2.bitwise_not(mask)


img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

toplam=cv2.add(img1_bg,img2_fg)
img1[0:x,0:y] = toplam

erosion=cv2.erode(mask,kernel)
cv2.imshow("erosion",erosion)


cv2.imshow("mask_inv",mask_inv)
cv2.imshow("mask",mask)
cv2.imshow("roi",roi)
cv2.imshow("toplamaa",toplam)


cv2.namedWindow("img1",cv2.WINDOW_NORMAL)
cv2.imshow("img1",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
