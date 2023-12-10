import cv2 as cv
import numpy as np 
img=cv.imread('OpenCV/ken.png')
cv.imshow('ken',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
b,g,r=cv.split(img)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow("blue chanel",blue)
cv.imshow("greed chanel",green)
cv.imshow("red",red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge=cv.merge([b,g,r])
cv.imshow("merge",merge)

cv.waitKey(0)