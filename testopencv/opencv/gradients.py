#  Gradients & edge detection
import cv2 as cv
import numpy as np

img = cv.imread('Photos/bus.JPG')
cv.imshow('Bus',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
# np.absolute will convert negative pixel to positive
# and np.uint8 is image data type.
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

# Sobel
sobelx = cv.Sobel(gray,cv.CV_64F, 1,0)
sobely = cv.Sobel(gray,cv.CV_64F, 0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel_x',sobelx)
cv.imshow('Sobel_y',sobely)
cv.imshow('combined',combined_sobel)

canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)




cv.waitKey(0) 