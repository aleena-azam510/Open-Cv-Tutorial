# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

img = cv.imread("resources/picture.jpg")

# stacking same image

# 1- Horizontal stack
hor_img = np.hstack((img,img))

# 2- Vertical stack
vert_img = np.vstack((img,img))

cv.imshow("horizontal stack", hor_img)
cv.imshow("vertical stack", vert_img)
cv.waitKey(0)
cv.destroyAllWindows()

# you can only stack images of same shape (height,width,colour)
# we cannot resize the stack image
# 
