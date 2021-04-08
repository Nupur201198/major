# colour spaces are the spaces of colour
# meaning grayscale & rgb is a colour space
# system representing colour of images

import cv2 as cv
# import Matplotlib.pyplot as plt

img = cv.imread('Photos/bus.JPG')
cv.imshow('Bus', img)
 
#BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# BGR to HSV(HUge stauration value)
# is based on how human see and thinks its colour
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L * a* b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

'''Matplot library reads image in RGB value
that is , inversion of colour of image.
Matplotlib.pyplot is used for inversion.
plt.imshow(img)
plt.show()
'''
# BGR to RGB using open cv
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

''' we can convert above images vise versa
like hsv to bgr , lab to bgr but not hsv to direct gray
first you will convert hsv to bgr then bgr to gray.'''

cv.waitKey(0)