# -*- coding: utf-8 -*-

def threshold(src,thresh,maxval):
    
    """
    
    bu işlem ile basit eşikleme yapılır.
    
    src=resim
    thresh=eşik
    maxval=son deger
    """
    
    img=src.copy()
    
    rows,cols=img.shape[:2]
    
    for i in range(rows):
        for j in range(cols):
            if img[i,j] < thresh:
                img[i,j]=0
            else:
                img[i,j]=maxval
    
    return thresh , img