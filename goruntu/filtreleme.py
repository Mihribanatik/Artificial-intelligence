# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:28:17 2021

@author: User
"""

import cv2
import numpy as np


img=cv2.imread("img/kizkulesi.jpg")

# cv2.namedWindow("kendi filtrem",cv2.WINDOW_NORMAL)
# cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
# cv2.namedWindow("keskinlestirme",cv2.WINDOW_NORMAL)

kernel=np.ones((5,5),np.float32)/25  # 5 5 oldugu için 3 3 için 9 böl
dst=cv2.filter2D(img,-1,kernel)

"""
#######  bulanıklastırır 1. yöntem #####
-1 biz kernele 25 böldük sonuç float olabilir ve görüntüyle çarparsak yine float olur 
görüntümüzün  veri türünün eski haline dönüstürmek için -1 kullanırız
"""

dst1=cv2.blur(img,(10,10)) #bulanıklastırır 2.yüntem

gauss=cv2.GaussianBlur(img,(5,5),0)  #bu da hepsini yumuatmaz komşuları yapar kenarları yapmaz 0 ise otomotik yapar

dst2=cv2.medianBlur(img,7)#verdiğin byt kadar küçükten büyüge sıralar ortalam alır ve yerleştiri,

##############KESKİNLEŞTİRME#############

filter=np.array([[-1,-1,-1],
                  [-1,9.99,-1],
                  [-1,-1,-1]])

dst3=cv2.filter2D(img,-1,filter)

##############kendi filtre uygulama :) ##########
filter=np.array([[0.3,-1,-1],
                  [-1,3,1],
                  [-1,3,-1]])

dst4=cv2.filter2D(img,-1,filter) 


filter =np.array([[0.272, 0.534, 0.131], #her matris sutunu bi rengi bgr belirliyo
                  [0.349, 0.686, 0.168],
                  [0.393, 0.769, 0.189]])

dst5=cv2.transform(img,filter) #sepya filtresi

"""
b,g,r=cv2.split(img)


r_new=r*0.393+g*0,769+b*0,189
g_new=r*0.349+g*0,686+b*0,168
b_new=r*0.272+g*0,534+b*0,131

"""
cv2.imshow("resim",img)

# cv2.imshow("gauss",gauss)
#cv2.imshow("filter2d",dst)
 
# cv2.imshow("blur",dst1)
# cv2.imshow("medianblur",dst2)
# cv2.imshow("keskinlestirme",dst3)
cv2.imshow("kendi filtrem",dst4)
cv2.imshow("sepya filtesi",dst5)



cv2.waitKey(0)
cv2.destroyAllWindows()

