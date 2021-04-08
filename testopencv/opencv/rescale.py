import cv2 as cv

# Resizing is applicable to images, Videos, and live Videos.
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
 
# This will work only on live Videos.
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


# Reading Videos
capture = cv.VideoCapture('Videos/094.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video',frame_resize)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()