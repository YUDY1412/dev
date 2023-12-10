import cv2 as cv
import numpy as np
img=cv.imread('OpenCV/ken.png')
cv.imshow('ken',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combine=cv.bitwise_or(sobelx,sobely)


cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('combine',combine)

#Canny
canny=cv.Canny(gray,80,175)
cv.imshow('Canny',canny)


cv.waitKey(0)