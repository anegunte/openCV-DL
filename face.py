import cv2
import numpy as np
capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    cv2.imshow("Video",frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
capture.release()
cv2.destroyAllWindows()