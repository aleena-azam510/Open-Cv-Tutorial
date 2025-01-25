# -*- coding: utf-8 -*-

# coordinates of image or video

import cv2 as cv
import numpy as np

def find_coord(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
         # left mouse click
         print(x,'',y)
         # dfeine or print on the same image or window
         font = cv.FONT_HERSHEY_PLAIN
         cv.putText(img, str(x) + ',' + str(y) , (x,y) , font , 1,(255,0,0),thickness=1)
         cv.imshow("image",img)
    #for  finding numbers of color 
    if event == cv.EVENT_RBUTTONDOWN:
        print(x,',',y)
        font1 = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r) , (x,y) , font , 1,(123,0,0),thickness=2)
        cv.imshow("image", img)



    
    
# final function to read and display
if __name__ == "__main__":
    img = cv.imread("resources/warp.jpg",1)
    cv.imshow("image", img)
    cv.setMouseCallback("image", find_coord)
    
    cv.waitKey(0)
    cv.destroyAllWindows()    
                                                                                                                                                                                   
    
