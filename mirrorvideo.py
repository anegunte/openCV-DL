import cv2
import numpy as np
capture =  cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    # mirror =  1 , upside down = 0 , mirror upside down = -1
    frame = cv2.flip(frame,-1)
    cv2.imshow("Mirror Video",frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
capture.release()
cv2.destroyAllWindows()