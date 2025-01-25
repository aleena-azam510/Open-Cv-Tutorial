# -*- coding: utf-8 -*-

# converting video to gray or black white
import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")
'''
while True:
    ret , frame = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret == True:
        cv.imshow("video", grayframe)
        if  cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
'''
while True:
    ret , frame = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    thresh,binary = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
    if ret == True:
        cv.imshow("video", binary   )
        if  cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()