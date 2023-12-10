import cv2 as cv

img=cv.imread('OpenCV/ken.png')
cv.imshow('ken',img)
# grayscale
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# HSV
hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# lAB
lab= cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

#

cv.waitKey(0)
