# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# writing format , codec , video writer object , file output

frame_width= int (cap.get(3))
frame_height=int (cap.get(4))
out = cv.VideoWriter("resources/cam_video.avi",cv.VideoWriter.fourcc('M', 'j', 'p', 'g'),10,(frame_width,frame_height))


while True:
    ret , frame = cap.read()

    if ret == True:
        out.write(frame)
        cv.imshow("cam video", frame)
        if  cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

