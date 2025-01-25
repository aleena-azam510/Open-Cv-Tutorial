# -*- coding: utf-8 -*-
import cv2 as cv
 
img = cv.imread("resources/scenery.jpg")
img = cv.resize(img,(800,600))   
img_gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("pehli image",img)
cv.imshow("Second image",img_gray)

cv.waitKey(0)
cv.destroyAllWindows()

