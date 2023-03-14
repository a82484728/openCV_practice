#source
#https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#Scaling
img = cv.imread('starry_night.jpg')
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
#OR
#height, width = img.shape[:2]
#res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)


cv.imshow('res',res)
cv.waitKey(0)

#Translation
#unpacking. we do not need the channels of img. img.shape[:2] only returns  rows and columns.
rows,cols = img.shape[:2]
#ontice that the Size of cv.warpAffine is (x,y) so we use (cols,rows) ,do not use (rows,cols).
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#Rotation
# cols-1 and rows-1 are the coordinate limits.why?
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#Affine Transformation
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

#Perspective Transformation
img = cv.imread('before_perspective_transformation.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[700,946],[2280,870],[30,3430],[2960,3360]])
pts2 = np.float32([[0,0],[300,0],[0,400],[300,400]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,400))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

