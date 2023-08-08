import cv2
import numpy as np

image = cv2.imread("/Users/vaishnavianegunte/Desktop/python/opencv/Unknown.jpeg")
#cv2.imshow("Original Image",image)
#cv2.waitKey(0)
blur = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Blurred Image",blur)
cv2.waitKey(0)