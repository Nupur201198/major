import cv2 as cv
import numpy as np

# masking allows to focus on main points in image
# like faces in image 
img = cv.imread('Photos/bus.JPG')
cv.imshow('Bus', img)


blank = np.zeros(img.shape[:2], dtype ='uint8')
cv.imshow('blank',blank)

mask = cv.rectangle(blank,(img.shape[1]//2 + 45, img.shape[0]//2 + 45),(img.shape[1]//2, img.shape[0]//2), 255, -1)
cv.imshow('Mask', mask)


masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked Image',masked)



cv.waitKey(0) 