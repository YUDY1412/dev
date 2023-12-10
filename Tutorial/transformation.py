import cv2 as cv
import numpy as np
img=cv.imread('OpenCV/ken.png')
cv.imshow('ken',img)

#tranlation 
def tranlation(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimension)

# -x left
# -y up
# x right
# y down
tranlated =tranlation(img,100,100)
cv.imshow("tranlation",tranlated)
#rotation 
def rotation(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)    
    rotMat =cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimension =(width,height)
    return cv.warpAffine(img, rotMat, dimension)
rotated = rotation(img,45)
cv.imshow("rotation",rotated)

#Flipping
flip=cv.flip(img, 0)
cv.imshow("flip",flip)
flip=cv.flip(img, 1)
cv.imshow("flip",flip)
flip=cv.flip(img, -1)
cv.imshow("flip",flip)
cv.waitKey(0)