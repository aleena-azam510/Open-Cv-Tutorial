# -*- coding: utf-8 -*-
# setting of camera or video

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

cap.set(10, 100)   #10 is the key to brightness
cap.set(3,640)     # 3 is the key to width
cap.set(4,480)     #4 is the key to length

while True:
    ret , frame = cap.read()
    if ret == True:
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
