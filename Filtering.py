import cv2 as cv
import numpy as np

img=cv.imread("OpenCV/ken.png")
cv.imshow("Ken_Origin",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

k=1
K=np.zeros((2*k+1,2*k+1),dtype='uint8')
blank=np.zeros((img.shape[1]+k,img.shape[0]+k),dtype='uint8')
a=np.zeros((1,2*k+1),dtype='uint8')
gray=np.row_stack((gray,a))
cv.imshow("b",gray)
K[:,:]=1/9
# for i in range(0,img.shape[1]):
#     for j in range(0,img.shape[0]):
#         for h in range()
cv.waitKey(0)