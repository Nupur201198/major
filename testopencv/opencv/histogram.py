import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# histogram allows you to visualize pixels distribution
img = cv.imread('Photos/bus.JPG')
cv.imshow('Bus',img)

blank = np.zeros(img.shape[:2], dtype ='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

circle = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2), 100, 255,-1)
cv.imshow('Circle', circle)
 
mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Mask', mask)


# grayscale histogram
'''
gray_hist = cv.calcHist([gray],[0], mask,[256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
'''


# colour histogram
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()





cv.waitKey(0)