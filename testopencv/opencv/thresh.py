import cv2 as cv

img = cv.imread('Photos/bus.JPG')
cv.imshow('bus',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('Thresholded',thresh)

threshold, thresh_inv = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('Thresholded Inverse',thresh_inv)

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive thresholding', adaptive_thresh) 

cv.waitKey(0)

