import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
img =cv.imread("OpenCV/ken.png")
cv.imshow('',img)
#1 tô màu cho ảnh
blank[:] = 0,255,0
cv.imshow('blank_color_green',blank)
#2 hình chữ nhật
cv.rectangle(blank,(0,0),(10,200),(255,0,255),thickness=2)
cv.imshow("rectangular",blank)
#3 hình tròn
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,150),thickness=3)
cv.imshow("circular",blank)
#4. line
cv.line(blank,(0,0),(200,200),(123,15,124),thickness=2)
cv.imshow("line",blank)
#5.text
cv.putText(blank,"hello",(200,200),cv.FONT_HERSHEY_SIMPLEX, 2.0, (255,0,0),thickness=10)
cv.imshow("texy",blank)
cv.waitKey(0)                           