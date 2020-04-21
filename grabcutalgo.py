import numpy as np
import cv2
#from matplotlib import pyplot as plt

img = cv2.imread('217.jpg')
gray = cv2.GaussianBlur(img, (41, 41) , 0)
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
ioi=int(maxLoc[1])
ioi1=int(maxLoc[0])

rect =(ioi1-79,ioi-51,140,150)

cv2.imshow('ioi',img)
cv2.waitKey(0)
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)


cv2.grabCut(img,mask,rect,bgdModel,fgdModel,10,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]


cv2.imshow('ioi',gray)
cv2.imshow('pl11.jpg',img)
cv2.waitKey(0)
