# -*- coding: utf-8 -*-
import cv2

cam=cv2.VideoCapture(0)  #kamerayı aç


if not cam.isOpened(): 
    print("kamera tanınmadı")
    

while True:
    ret,frame=cam.read() #oku
    
    if not ret:
        print("kamera çalışmıyor")
        break
    
    cv2.imshow("video",frame) #göster 
    
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        print("video sonlandırıldı")
        break

cam.release()
cv2.destroyAllWindows()




import  cv2


cam=cv2.VideoCapture(0)  #kamerayı aç


if not cam.isOpened(): 
    print("kamera tanınmadı")
    exit()

print(cam.get(3)) #get istediğin vido özelliğini alır 
print(cam.get(4))

cam.set(3,320)
cam.set(4,320)
while True:
    ret,frame=cam.read() #oku
    
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #videoyu grileştirir
    
    
    if not ret:
        print("kamera çalışmıyor")
        break
      
    
    cv2.imshow("video",frame) #göster 
    

    
    
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        print("video sonlandırıldı")
        break

cam.release()
cv2.destroyAllWindows()


#################VAR OLAN VİDEOYU AÇMA#################
import cv2

cam=cv2.VideoCapture("video.avi")

while cam.isOpened():
    ret,frame=cam.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if not ret:
        print("görüntü alınamıyor")
        break
    
    cv2.imshow("video",frame)



    if cv2.waitKey(1) & 0xff == ord("q"):
        print("video kapandı")
        break
    
cam.release()
cv2.destroyAllWindows()
                                    
######### video cekme##############

import cv2

cam=cv2.VideoCapture(0)

fourrc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter("video.avi",fourrc,30.0,(640,480)) 
#boş ir sablon olusturup videonun adını boyutunu  taımlamayı  yazdım..
#yani 2 satir ile şablonu olustrup out.write ile kaydediyorsun
while cam.isOpened():
    ret,frame=cam.read()
    
    
    if not ret :
        print("görüntü alınamadı")
        break
    
    cv2.imshow("görüntü",frame)
    
    out.write(frame)
    
    
    if cv2.waitKey(1)==ord("q"):
        print("video kapandı")
        break
    
cam.release()
cv2.destroyAllWindows()





