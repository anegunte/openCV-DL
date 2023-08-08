import cv2
image = cv2.imread("opencv/Unknown.jpeg")
#cv2.imshow("original",image)
#cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',gray)
cv2.waitKey(0)
