import cv2 as cv

img=cv.imread('OpenCV/ken.png')
cv.imshow('ken',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#simple threshholding
threshhold, thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow("simplethreshhold",thresh)

#adaptive threshhold
adaptive_theshhold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("ADAPTIVE threshold",adaptive_theshhold)
cv.waitKey(0)