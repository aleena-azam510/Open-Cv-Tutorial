# -*- coding: utf-8 -*-
# Image into black and white

import cv2 as cv

img = cv.imread("resources/picture.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh,binary) = cv.threshold(gray, 127,255,cv.THRESH_BINARY)
cv.imshow("original", img)
cv.imshow("gray", gray)
cv.imshow("Black and white", binary)
cv.waitKey()
cv.destroyAllWindows()