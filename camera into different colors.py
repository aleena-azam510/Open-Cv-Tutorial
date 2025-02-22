# -*- coding: utf-8 -*-
# camera into different colors

import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

while True:
    ret , frame = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    thresh , binary = cv.threshold(gray_frame,127,255,cv.THRESH_BINARY)
    cv.imshow("original cam", frame)
    cv.imshow("gray cam ", gray_frame)
    cv.imshow("black and white cam ", binary)
    if  cv.waitKey(1) & 0xFF == ord('q'):
        break 
cap.release()
cv.destroyAllWindows()
    

