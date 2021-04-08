import cv2 as cv
import numpy as np

img = cv.imread('Photos/bus.JPG')
cv.imshow('Bus',img)

# Translation 
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# --x --> left
# x --> right
# --y --> up
# y --> down

translated = translate(img,-100,100)
cv.imshow('translated', translated)


# Rotation
def rotate(img,angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height //2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)


# - ve angle ---> clock-wise
# +angle --> anticlock-wise
rotated = rotate(img, -90)
cv.imshow('Rotate',rotated)

# Resize
resized = cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('resize',resized)

# FLipping

# 0 --> vertically
# 1 --> horizontally
# -1 --> both hori and vertically 
flip = cv.flip(img,-1)
cv.imshow('Flip',flip)

# Cropping
cropped = img[200:400,400:500]
cv.imshow('Cropped',cropped)


cv.waitKey(0)


