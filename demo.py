# -*- coding: utf-8 -*-
import cv2                   #imports the OpenCV library, which is essential for image processing tasks.

# Colorful image
img1 = cv2.imread("D:\\jellyfish1.jpg",1)      #read an image named "jellyfish.jpg" from the specified path.
print(img1)
img1 = cv2.resize(img1,(1000,300))              # resizes the image to a width of 1280 pixels and a height of 700 pixels.
cv2.imshow("Colored image", img1)                    #displays the image in a window named "original"ws.


 # Gray scale image
img2=cv2.imread("D:\\jellyfish1.jpg",0)
img2 = cv2.resize(img2,(1000,300)) 
cv2.imshow("Gray scale image", img2) 
print("Image in Gray scale",img2)


#Unchanged
img3=cv2.imread("D:\\jellyfish1.jpg",-1)
img3 = cv2.resize(img3,(1000,300)) 
cv2.imshow("unchanged image", img3) 
print("Image in Gray scale",img3)


cv2.waitKey()                                   #waits for a key press from the user.
cv2.destroyAllWindows()                         #closes all the OpenCV windo