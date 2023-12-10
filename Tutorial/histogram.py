import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('OpenCV/ken.png')
img=cv.resize(img,(500,500))
cv.imshow('ken',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#gray histogram

# gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])
# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('number of pixel')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram
plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('number of pixel')


color=('b','g','r')
for i,col in enumerate(color):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)