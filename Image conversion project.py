# -*- coding: utf-8 -*-
# Image Conversion project

import cv2

# Get the path of the image from the user, ensuring it's in UTF-8
path = input('Enter the path of image: ').encode('utf-8').decode('utf-8') 

print("You entered this path =", path)

# Load the image in grayscale mode
img = cv2.imread(path, 0) 

# Resize the image
img = cv2.resize(img, (1000, 300))
img = cv2.flip(img, 0)   #0,1,-1

# Display the grayscale image
cv2.imshow("Gray scale image", img)
print("Image in Gray scale", img)

# Wait for a key press
k = cv2.waitKey(0) 
if k == ord("s"):
    cv2.imwrite("D:\shineouput.png",img) 
   
    
else:
    cv2.destroyAllWindows()