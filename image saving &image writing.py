# -*- coding: utf-8 -*-
# image saving and image writing
import cv2 as cv
from cv2 import imwrite

img = cv.imread("resources/picture.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh,binary) = cv.threshold(gray, 127,255,cv.THRESH_BINARY)

imwrite('resources/img_gray.jpg',gray)

imwrite('resources/img_binary.jpg',binary)

#cv.waitKey()
#cv.destroyAllWindows()


