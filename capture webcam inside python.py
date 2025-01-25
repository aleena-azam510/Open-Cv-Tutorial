# -*- coding: utf-8 -*-

# how to capture webcam inside python

#step 1: import libraries
import cv2 as cv
import numpy as np

#step 2: read the frames from camera
cap = cv.VideoCapture(0) # webcam = 1

#if cap.isOpened()==False:
  #  print("there is an error")

#step3:display frame by frame
while(cap.isOpened()):
    # capture frame by frame
    ret , frame = cap.read()
    if ret == True:
        # to display frames
       
        if ret == True:
            cv.imshow("video",frame)
            if  cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
#step 4: release and close windows
cap.release()
cv.destroyAllWindows()