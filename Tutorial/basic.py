import cv2 as cv 
 
img=cv.imread('OpenCV/ken.png')
cv.imshow("ken",img)

# Converting to grayscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#blur
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Gblur",blur)

#edge cascade
canny= cv.Canny(blur, 125,175)
cv.imshow("Canny",canny)

#dilating image
dilated=cv.dilate(canny,(3,3), iterations=1)
cv.imshow("dilated", dilated)

#eroding
erode=cv.erode(dilated,(3,3), iterations=1)
cv.imshow("erode",erode)

# resize
resize=cv.resize(img,(300,300),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resize)

# CROP
crop=img[200:400,200:400]
cv.imshow("Crop",crop)
cv.waitKey(0)