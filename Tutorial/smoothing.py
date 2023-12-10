import cv2 as cv

img=cv.imread('OpenCV/ken.png')
cv.imshow('ken',img)

#averange
aver=cv.blur(img,(5,5))
cv.imshow("aver",aver)

#gaussian
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow("gauss",gauss)

#median
median=cv.medianBlur(img,7)
cv.imshow("median",median)

#bilateral
bilateral=cv.bilateralFilter(img,5,15,15)
cv.imshow("bilateral",bilateral)
cv.waitKey(0)