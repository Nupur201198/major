import cv2 as cv

img = cv.imread('Photos/bus.JPG')
cv.imshow('bus',img)

# averaging - average of around pixels
avg = cv.blur(img,(3,3))
cv.imshow('average blur',avg)

# gausian blur
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('gaussian blur', gauss)

# median blur--> finda median of arounding pixels
median = cv.medianBlur(img,3)
cv.imshow('median blur', median)

# bilateral blurring
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)
