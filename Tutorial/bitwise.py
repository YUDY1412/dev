import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype='uint8')
# blank[:]=0,0,255
cv.imshow("blank",blank)
rectangle=cv.rectangle(blank.copy(), (30,30),  (470,470) ,255,-1)
circle=cv.circle(blank.copy(),(250,250),250,255,-1)
cv.imshow("circle",circle)
cv.imshow("rectang",rectangle)

#bitwise and
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("and",bitwise_and)

#bitwise_or
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("or",bitwise_or)

#bitwise_xor --> non intersecting region
bitwise_xor=cv.bitwise_xor(rectangle,circle)

#bitwise not
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow("not",bitwise_not)

cv.imshow("xor",bitwise_xor)
cv.waitKey(0)