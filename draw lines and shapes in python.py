# -*- coding: utf-8 -*-

# How to draw lines and shapes in python

import cv2 as cv
import numpy as np

# Draw a canvas , 0 is for black
img_black= np.zeros((600,600))
img_white=np.ones((600,600))

# print size
print("the size of our canvas is ",img_black.shape)
print(img_black)

# adding colors to the canvas
colored_img = np.zeros((600,600,3),np.uint8) # color channel addition
colored_img[:]= 0, 102, 0                   # color complete canvas
colored_img[150:230,100:207]=255,0,0         # part of canvas to be colored

# adding line
cv.line(colored_img,(0,0),(colored_img.shape[0],colored_img.shape[1]),(153, 102, 0),3)
cv.line(colored_img,(100,100),(123,123),(255, 204, 0),3)

# adding rectangle
cv.rectangle(colored_img,(50,100),(300,400), (0,0,0),3)
cv.rectangle(colored_img,(50,100),(300,400), (0,0,0),cv.FILLED)

# adding circle
cv.circle(colored_img,(50,100),50, (255,255,255),5)
cv.circle(colored_img,(50,100),50, (23,255,23),cv.FILLED)

# adding text
cv.putText(colored_img, "computer vision crash course", (100,300), cv.FONT_HERSHEY_DUPLEX, 1, (255,255,0))





#cv.imshow("black canvas", img_black)
#cv.imshow("white canvas", img_white)
cv.imshow("colored canvas", colored_img)

cv.waitKey(0)
cv.destroyAllWindows()
