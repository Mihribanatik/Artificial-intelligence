# -*- coding: utf-8 -*-

import cv2
from  matplotlib import pyplot as plt
import numpy as np

resim=cv2.imread("img/ucak.png",0)  #resmi acar 0 siyah beyaz açar

cv2.imshow("ilk resim",resim) #1.parametre resmin ismi ne olsun 2.neyi göstericek

plt.imshow(resim)  #boyutlu halini aldım
plt.show()


cv2.namedWindow("bos pencereye aktarılan resim",cv2.WINDOW_NORMAL)#BOŞ BİR PENCERE

cv2.imshow("bos pencereye aktarılan resim",resim)#RESMİ BOS CERECEVEYE AKTAAR

k=cv2.waitKey() #görüntüyü bekletir

if k==ord("q"):
    print("resim kapandı")
    cv2.imwrite("griresim.jpg",resim)
    

cv2.destroyAllWindows()


bir=np.ones([300,300])
sifir=np.zeros([300,300])

print(bir)
