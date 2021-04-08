import cv2 as cv

img = cv.imread('Photos/lady.JPG')
cv.imshow('Person',img)

# convert image to gray scale because img should not skin tone.
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# reading haar cascade file by giving the path

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# faces_rect is a list coordinates of face in rectangle shape
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

print(faces_rect)

for (x,y,w,h) in faces_rect:
    print(x,y,w,h)
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=1)

cv.imshow('Detected faces',img)

cv.waitKey(0)
