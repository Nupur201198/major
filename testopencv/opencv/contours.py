import cv2 as cv
import numpy as np
img = cv.imread('Photos/bus.JPG')
cv.imshow('Bus',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)


# threhshold --> binarazing the image , i.e turning image either in black and white.
#ret, thresh = cv.threshold(gray,125,225,cv.THRESH_BINARY)
#cv.imshow('THresh',thresh)


# Finding contours
# contours -- > list of coordinates of edges
# hierarchies --> find the hierarchy contours
contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

# Drawing contours over blank image for better detection of contours.
blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

# third parameter is how many edges you want
# -1 --> all of the edges
cv.drawContours(blank,contours, -1 , (0,0,255), thickness=1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
