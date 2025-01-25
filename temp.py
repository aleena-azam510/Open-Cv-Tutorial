# -*- coding: utf-8 -*-
import cv2                   #imports the OpenCV library, which is essential for image processing tasks.
img1 = cv2.imread("D:\\Machine_Learning_OneShots\\jellyfish1.jpg",1)      #read an image named "jellyfish.jpg" from the specified path.
img1 = cv2.resize(img1,(1280,700))              # resizes the image to a width of 1280 pixels and a height of 700 pixels.
cv2.imshow("Colored image", img1)                    #displays the image in a window named "original"
cv2.waitKey()                                   #waits for a key press from the user.
cv2.destroyAllWindows()                         #closes all the OpenCV windows.

