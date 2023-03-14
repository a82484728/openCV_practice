#source
#https://docs.opencv.org/4.x/d0/d86/tutorial_py_image_arithmetics.html
import numpy as np
import cv2 as cv

img1 = cv.imread('Python_Logo.png')
img2 = cv.imread('OpenCV_Logo_s.png')

#the shapes of img1 and img2 ar not th same.
#we use cv.resize to modify img1.
#we use (cols1,rows1) because the first value is the 'width' of output image and the second value is the 'height' of output image.

rows1,cols1,channes1=img1.shape
img2 = cv.resize(img2, (cols1,rows1))

print(img1.shape)
print(img2.shape)
dst = cv.addWeighted(img1,0.5,img2,0.5,0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.imwrite("logo_blending.png", dst)
cv.destroyAllWindows()