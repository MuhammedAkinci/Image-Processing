# when we start here, the corners of the object or entity that will appear on the screen are determined
# So, for example, when the camera is turned on, if I am in front of the camera, my body lines will be visible with a white line as much as I look.

import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
# we flip the image that will come out with flip, we get different images by playing with 1

    edges = cv2.Canny(frame, 100, 200) # here we deflect the corners. first the frame is entered, then we enter the min and max threshold values
    # here we can change the image that will appear by playing with 100 and 200, we determine the corners of what appears on the screen thanks to canny
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()