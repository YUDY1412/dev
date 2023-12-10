import cv2 as cv
import numpy as np

img=cv.imread("OpenCV/ken.png")
cv.imshow("Ken_Origin",img)
blank=np.zeros(img.shape,dtype='uint8')
# # Ma tran bien doi tinh tien x ,y 
# T=[[1 ,0 ,0],[0, 1, 0], [50, 50, 1]] 

# Ma tran bien doi xoay
T=[[0 ,1 ,0],[-1, 0, 0], [0,0, 1]] 
for i in range(-img.shape[1]//2,img.shape[1]//2):
    for j in range(-img.shape[1]//2,img.shape[1]//2):
        r=np.matmul([i,j,1],T)
        if r[0]>=img.shape[1] or r[0]<=0 or r[1]>=img.shape[0] or r[1]<=0:
            img[i+img.shape[0]//2,j+img.shape[1]//2]=[0,0,0]
        else:
            img[i+img.shape[0]//2,j+img.shape[1]//2]=img[r[0],r[1]]

cv.imshow("Ken_modify",img)        
cv.waitKey(0)