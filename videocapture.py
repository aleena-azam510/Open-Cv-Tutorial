# -*- coding: utf-8 -*-
import cv2
cap = cv2.VideoCapture("D:\video.mp4")
print("capture",cap)
'''
while True:
    ret,frame = capture.read()
    resized_frame = cv2.resize(frame, (700, 450))  # Adjust dimensions as needed

    cv2.imshow("frame",resized_frame)
    k = cv2.waitKey(25)
    if k == ord('s'):
        break
        
capture.release()
cv2.destroyAllWindows()
'''


while True:
    ret, frame = cap.read()   #here read the frame
    #get height and width of frame
    print("Width ==>",cv2.CAP_PROP_FRAME_WIDTH)
    print("Height==>",cv2.CAP_PROP_FRAME_HEIGHT)
    
    frame = cv2.resize(frame,(700,450))
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,-1) 
    cv2.imshow('Colorframe',frame)
    cv2.imshow("Gray Frame",gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):   #press to exit
        break
   
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()