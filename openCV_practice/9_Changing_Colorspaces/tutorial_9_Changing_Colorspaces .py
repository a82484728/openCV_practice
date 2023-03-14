#source
#https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
#import cv2 as cv
#img=cv.imread('starry_night.jpg')
#img=cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('img',img)
#cv.waitKey(0)
#cv.destroyAllWindows()


import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    # if array elements lie between the elements of lower_blue and upper_blue → RGB(255,255,255)
    # otherwise → RGB(0,0,0)
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    # if mask(I)=0, res(I)=0.
    # if mask(I)≠0, res(I)=frame(I)∧frame(I)
    res = cv.bitwise_and(frame,frame, mask= mask)

    #frame is the original video
    #mask is the range of the object(blue) that we want to extract
    #res is the object(blue) that we want to extract
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()