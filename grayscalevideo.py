import cv2
import numpy as np
capture =  cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Video",gray)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
capture.release()
cv2.destroyAllWindows()