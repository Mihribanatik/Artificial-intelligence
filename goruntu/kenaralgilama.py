# -*- coding: utf-8 -*-

###########sobel filtreleme kenar Algılama###########

import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread("img/istenilenalan.png",0)

sobelX=cv2.Sobel(img,-1,1,0 ,ksize=5) #X eksenin kenarlarını algılar -1 İNT DÖNÜŞÜM SAGLAR
sobelY=cv2.Sobel(img,-1,0,1,ksize=5) #Y ekseninin kenarlarını algılar
sobel=cv2.Sobel(img,-1,1,1, ksize=5)  #her iki eksendede kenar algılar

sobelX1=cv2.Sobel(img,-1,1,0, ksize=-1) #-1 otomotik olarak kaç matris oldugunu belirler

sobelX2=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)# burda negatifleri de aalır
sobelX2=np.absolute(sobelX2) #mutlak degerini aldım
sobelX2=np.uint8(sobelX2) # inte çevirdim

####laflas alma

laplacian=cv2.Laplacian(img,-1,ksize=1) # default olarakta yani ksize vermedende kullanabilirim

canny=cv2.Canny(img,200,240) #max ve min degeri ve resmi giriyoruz


plt.subplot(231),plt.imshow(img,"gray"),plt.title("orginal")
plt.subplot(232),plt.imshow(sobelX,"gray"),plt.title("sobelx")
plt.subplot(233),plt.imshow(sobelY,"gray"),plt.title("sobely")
# plt.subplot(234),plt.imshow(sobel,"gray"),plt.title("sobel")
# plt.subplot(235),plt.imshow(sobelX2,"gray"),plt.title("sobelx2")
plt.subplot(236),plt.imshow(sobelX2,"gray"),plt.title("sobelx2")
plt.subplot(234),plt.imshow(laplacian,"gray"),plt.title("laplacian")
plt.subplot(235),plt.imshow(canny,"gray"),plt.title("canny")

plt.show()