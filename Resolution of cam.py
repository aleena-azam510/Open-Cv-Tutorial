# -*- coding: utf-8 -*-
# Resolution of cam

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#resolution HD (1280 X 720) , SD(640,480) , fhd(1920,1080)

cap.set(3,1280) # width
cap.set(4,720)  # height

def hd_resolution():
    cap.set(3,1280) # width
    cap.set(4,720)  # height
    
def sd_resolution():
    cap.set(3,640)
    cap.set(4,480) 
    
def fhd_resolution():
    cap.set(3,1920)
    cap.set(4,1080) 
    
#hd_resolution()
#sd_resolution()
fhd_resolution()


while True: 
    ret , frame = cap.read()
    if ret == True:
        cv.imshow("camera", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
