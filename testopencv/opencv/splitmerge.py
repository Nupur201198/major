import cv2 as cv
import numpy as np

img = cv.imread('Photos/Bus.JPG')
cv.imshow('Bus',img)


blank = np.zeros(img.shape[:2], dtype= 'uint8')

# seperating colour channels --> blue,green,red
b,g,r = cv.split(img)


# representing these channels in true original colour 
# not in gray format
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

'''where it is darker in gray image that means that colour is not present over there continuation after seperating channels heading'''
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging of these color channels
merged = cv.merge([b,g,r])
cv.imshow('merged',merged)



cv.waitKey(0)