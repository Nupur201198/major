import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank',blank)

# 1. Paint the image a cetain colour
#blank[200:300,300:400] = 0,255,0
#cv.imshow('Green',blank)

# 2. Draw a Rectangle 
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

# 3 Draw a circle
cv.circle(blank,(250,250), 40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)

# 4 draw a line
cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('Line',blank)

# 5 Write a text on a image
cv.putText(blank, 'Hello ! My name is Nupur',(225,225),cv.FONT_HERSHEY_COMPLEX, 1.0,(255,0,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)