import numpy as np
import cv2 as cv

#events = [i for i in dir(cv) if 'EVENT' in i]
#print( events )

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),10,(255,0,0),-1)


# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
print( cv.setMouseCallback )
while(1):
    cv.imshow('image',img)
    #waitKey waits for a key event.It returns the code(ASCII) of the pressed key. ESC is 27 in ASCII.
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()