import cv2 as cv
import numpy as np

img=cv.imread("OpenCV/ken.png")
img=cv.resize(img,(img.shape[1]//2,img.shape[0]//2))
print(img.shape)
cv.imshow("Ken_Origin",img)
print(img[1,1][2])
#split
red=np.zeros(img.shape, dtype='uint8')
blue=np.zeros(img.shape, dtype='uint8')
green=np.zeros(img.shape, dtype='uint8')
for i in range(0,img.shape[1]):
    for j in range(0,img.shape[0]):
        red[i,j]=(0,0,img[i,j][2])
cv.imshow("Ken_red",red)

for i in range(0,img.shape[1]):
    for j in range(0,img.shape[0]):
        blue[i,j]=(img[i,j][0],0,0)
cv.imshow("Ken_blue",blue)

for i in range(0,img.shape[1]):
    for j in range(0,img.shape[0]):
        green[i,j]=(0,img[i,j][1],0)
cv.imshow("Ken_green",green)

#gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Ken_Gray",gray)
#hsv
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)
cv.imshow("Ken_hsv",hsv)

for i in range(0,img.shape[1]):
    for j in range(0,img.shape[0]):
        red[i,j]=(0,0,hsv[i,j][1])
cv.imshow("Ken_red_hsv",red)

cv.waitKey(0)