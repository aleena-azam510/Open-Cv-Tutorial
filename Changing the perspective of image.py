# -*- coding: utf-8 -*-

# Changing the perspective of imagee

import cv2 as cv
import numpy as np

img = cv.imread("resources/warp.jpg")
#print(img.shape)    # (225, 225, 3)
width = 225
height = 225
width,height = 225 , 225
# defining points
point1 = np.float32([[100 , 31],[205 ,  66],[18 , 147],[143 , 183]])
point2 = np.float32([[0,0],[225,0],[0,height],[width,height]])


matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img,matrix, (width,height))

cv.imshow("original", img)
cv.imshow("transfomed", out_img)