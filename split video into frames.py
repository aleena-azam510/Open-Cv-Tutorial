# -*- coding: utf-8 -*-

# split your video into frames
import cv2 as cv
cap = cv.VideoCapture("resources/video.mp4")
# seconds x frames per second = no of frames

framenum = 0
while True:
    ret,frame =cap.read()
    if ret:
        cv.imwrite(f"resources/frames/frame_{framenum}.jpg" , frame)
    else:
        break
    framenum = framenum +1
cap.release()
    
        
        


