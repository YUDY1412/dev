import cv2 as cv
import numpy as np

img=cv.imread("OpenCV/ken.png")
img=cv.resize(img,(img.shape[1]//2,img.shape[0]//2))
cv.imshow("Ken_Origin",img)
blank=np.zeros((img.shape[1]*2,img.shape[0]*2,3),dtype='uint8')

for i in range(0,img.shape[1]):
    for j in range(0,img.shape[0]):
        if i%2 !=0 and j%2!=0:
            blank[i*2,j*2]=img[i,j]
cv.imshow("balnk",blank)

blank=cv.cvtColor(blank,cv.COLOR_BGR2GRAY)
cv.imshow("gray",blank)
for i in range(0,blank.shape[1]-1):
    for j in range(0,blank.shape[0]-1):
        # a=(blank[i+1,j]+blank[i-1,j])//2
        # b=(blank[i,j+1]+blank[i,j-1])//2
        # c=(blank[i+1,j]+blank[i-1,j] + blank[i,j+1]+blank[i,j-1])//4
        # d=blank[i,j]

        blank[i,j]=(blank[i+1,j]+blank[i-1,j] + blank[i,j+1]+blank[i,j-1])//4
cv.imshow("balnk_NEW",blank)    
cv.waitKey(0)