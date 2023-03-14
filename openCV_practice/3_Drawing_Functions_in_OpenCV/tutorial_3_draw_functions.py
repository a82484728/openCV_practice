import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(50,100),(300,400),(255,0,200),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63), 10, (0,100,100), -1)


cv.ellipse(img,(256,256),(100,50),45,0,90,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255),2)

font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img,'Happy',(20,200), font, 4,(100,255,255),2,cv.LINE_AA)
cv.putText(img,'birthday',(20,350), font, 4,(100,255,255),2,cv.LINE_AA)

cv.imshow('img', img)

if cv.waitKey(0) == ord('q'):
    cv.destroyAllWindows()
