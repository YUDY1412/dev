import cv2 as cv


def rescale(frame, scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame, dimension,interpolation=cv.INTER_AREA)

capture =cv.VideoCapture('video.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=rescale(frame,0.5)
    cv.imshow("video",frame)
    cv.imshow("video_resize",frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release
cv.destroyAllWindows()

