# -*- coding: utf-8 -*-
# basic functions and manipulation in open cv

import cv2 as cv
import numpy as np
img = cv.imread("resources/picture.jpg")

# resizing
resized_img = cv.resize(img, (450, 250))
# gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur image
blur_img = cv.GaussianBlur(img, (7, 5), 0)
# edge detection
edge_img = cv.Canny(img, 48, 48)
# thickness of lines
mat_kernal = np.ones((7, 7), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernal), iterations=1)
#thinner image
ero_img = cv.erode(dilated_img, mat_kernal,iterations=1)
#cropping the image
print("The size of our image is ",img.shape)
cropped_img = resized_img[0:200,200:300]


cv.imshow("original", img)
cv.imshow("cropped_image", cropped_img)
#cv.imshow("resized", resized_img)
#cv.imshow("gray", gray_img)
#black and white image
#cv.imshow("blurred", blur_img)
#cv.imshow("edge detection", edge_img)
#cv.imshow("dilated image", dilated_img)
#cv.imshow("thinner image",ero_img)


cv.waitKey(0)
cv.destroyAllWindows()
