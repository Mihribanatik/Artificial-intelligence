# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=cv2.imread("img/istenilenalan.png")


img_copy=img.copy()
gray=cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,30,50)

def nothing(x):
    pass

cv2.namedWindow("trekbar",cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("threshold","trekbar",0,300,nothing)


while(1):
    
    img_copy=img.copy()
    
    threshold=cv2.getTrackbarPos("threshold","trekbar")+1
    print(threshold)
    
    # Algılanmış kenarlar üzerindeli çizgileri  bulmak 

    lines=cv2.HoughLines(edges,1,np.pi/180,threshold)

    """
    1.par.= kenarları algılanmış resim
    2.par.=r nin çözünürlüğü px olarak. 1 den düşük olamaz (float degerler olamaz)
    3.par.=teta nın derece olarak çözünürlüğü
    4.par.=kaçtane çizginin kesişmesiyleoluşan  çizgileri belirler ne kadar çok verirsen az çizgi belirler.
    
    bu çizgiler yani lines bi dizi olarak döner.
    """


    """
    #dizinin tipi none degiğlse yani deger döndürüyorsa işlem yap
    #line içinde r ve teta degerleri var
    if not isinstance(lines, type(None)):
        for line in lines:
            for rho,theta in line:
                a=np.cos(theta)
                b=np.sin(theta)
                x0=a*rho
                y0=b*rho
                
                #iki nokta belirtim
                x1=int(x0 + 1000*(-b))
                y1=int(y0 + 1000*(a))
                x2=int(x0 - 1000*(-b))
                y2=int(y0 - 1000*(a))
                
                cv2.line(img_copy,(x1,y1),(x2,y2),(0,0,255),2)
                

    
    #################### ikinci yol ################### 
    
    """
    lines=cv2.HoughLinesP(edges,1,np.pi/180,threshold,50,10)
    #4.par=kac px birleşimini çizgi olarak algılasın 
    #5.par=ne kadar boşlugu kenar alsın örn 10 dan fazla boslugu kenr olarak almaz azaltırsan cok cizgiolur

    if not isinstance(lines, type(None)):
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(img_copy,(x1,y1),(x2,y2),(255,0,0),2)

    
    
    cv2.imshow("trekbar",img_copy)
    #cv2.imshow("edges",edges)
    
    
    if cv2.waitKey(33) & 0xff ==ord("q"):
        break
cv2.destroyAllWindows()



































           
            