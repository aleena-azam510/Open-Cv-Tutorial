# -*- coding: utf-8 -*-
import cv2 as cv

cap = cv.VideoCapture("resources/video.mp4")

# writing format , codec , video writer object , file output

frame_width= int (cap.get(3))
frame_height=int (cap.get(4))
out = cv.VideoWriter("resources/out_video.avi",cv.VideoWriter.fourcc('M', 'j', 'p', 'g'),10,(frame_width,frame_height))


while True:
    ret , frame = cap.read()
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret == True:
        out.write(frame)
        cv.imshow("video", grayframe)
        if  cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

