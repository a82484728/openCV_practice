#resources 
#https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img1 = cv.imread('OpenCV_Logo.png')
#RGB in matplotlib
#BGR in cv2
#we have to convert them
b,g,r = cv.split(img1)
img1 = cv.merge((r,g,b))

BLUE = [0,0,255]


replicate = cv.copyMakeBorder(img1,100,50,25,0,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,100,50,25,0,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,100,50,25,0,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,100,50,25,0,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,100,50,25,0,cv.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant),plt.title('CONSTANT')
plt.show()