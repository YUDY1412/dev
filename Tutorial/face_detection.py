import cv2 as cv

img=cv.imread('OpenCV/group.jpg')
img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
cv.imshow('ken',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade=cv.CascadeClassifier('haar_face.xml')
face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(face_rect)
for (x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)
cv.imshow('Detectedface',img)  
cv.waitKey(0)