#import OpenCV python library
import cv2 as cv

##not necessary?
#import sys

#read the image "starry_night.jpg" 
#cv.IMREAD_GRAYSCALE convert image to the single channel grayscale image
img = cv.imread(cv.samples.findFile("starry_night.jpg"),cv.IMREAD_GRAYSCALE)

##not necessary?
#if img is None:
#    sys.exit("Could not read the image.")

#show image 
#"Display window" is the title
cv.imshow("Display window", img)

#how long should it wait for a user input (ms). Zero means to wait forever.
#the following code is not executed until we press a key.
#It waits for a key event.It returns the code(ASCII) of the pressed key.
k = cv.waitKey(0)

#the image is written to a file if the pressed key was the "s"-key.
#ord can get ASCII of the pressed key
if k == ord("s"):
    cv.imwrite("starry_night.png", img)