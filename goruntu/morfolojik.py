# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np

resim=cv2.imread("img/closing.png")


#-,resim=cv2.treshold(resimm)
kernel=np.ones((5,5),np.int8)
"""

kernel_rectangle=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))


kare elips vs şeklinde kernel  oluştura bilirsiniz.

"""
erosion=cv2.erode(resim,kernel) #inceltmme
delation=cv2.dilate(resim,kernel,iterations=1)#kalınlastırma

opening=cv2.morphologyEx(resim,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(resim,cv2.MORPH_CLOSE,kernel)
tophat=cv2.morphologyEx(resim,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(resim,cv2.MORPH_BLACKHAT,kernel)
gradient=cv2.morphologyEx(resim,cv2.MORPH_GRADIENT,kernel)



plt.subplot(241),plt.imshow(resim,"gray"),plt.title("orijinal")
plt.subplot(242),plt.imshow(erosion,"gray"),plt.title("erosion")
plt.subplot(243),plt.imshow(delation,"gray"),plt.title("delation")
plt.subplot(244),plt.imshow(opening,"gray"),plt.title("opening")# once erezyon sonra dileysion işlemi yarar 
plt.subplot(245),plt.imshow(closing,"gray"),plt.title("closing")
plt.subplot(246),plt.imshow(tophat,"gray"),plt.title("tophat")
plt.subplot(247),plt.imshow(blackhat,"gray"),plt.title("blackhat")
plt.subplot(248),plt.imshow(gradient,"gray"),plt.title("gradient")#AŞINAMA VE GENİŞLETMENİN FARKINI ALIR


plt.show()
cv2.waitKey()
cv2.destroyAllWindows()