#resources 
#https://docs.opencv.org/4.x/d3/df2/tutorial_py_basic_ops.html

import numpy as np
import cv2 as cv

img = cv.imread('messi5.png')
#accessing RED value
#img.item() only returns a scalar. B,G,R can be accessed separately.
print(img.item(10,10,0))

#modifying RED value
img.itemset((10,10,2),100)
print(img.item(10,10,2))

#img.shape can return a tuple of the number of rows, columns, and channels (if the image is color)
#If an image is grayscale, the tuple returned contains only the number of rows and columns
print( img.shape )
img_2 = cv.imread('messi5.png',cv.IMREAD_GRAYSCALE)
print( img_2.shape )

#Total number of pixels. 342*548*3=562248
print( img.size )

#image datatype
#img.dtype is very important while debugging because a large number of errors in OpenCV-Python code are caused by invalid datatype.
print( img.dtype )

#Sometimes, you will have to play with certain regions of images.
#e.g.eye detection:
#face detection is done over the entire image → search for eyes inside the face region.
#improves accuracy (eyes are always on faces) and performance (we search in a small area).
#use following codes to modify certain regions of images.
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

#Sometimes you will need to work separately on the B,G,R channels of an image.
b,g,r = cv.split(img)
img = cv.merge((b,g,r))

#all the blue(0) and grren(1) pixels to zero.
img[:,:,0] = 0
img[:,:,1] = 0


cv.imshow("img", img)
cv.waitKey(0)

