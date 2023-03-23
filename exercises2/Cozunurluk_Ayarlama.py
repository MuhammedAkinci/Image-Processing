#Here we made some manipulations and applied the video with the get() and set() functions.
# We got values with get() and reassigned those values with set() to our video, which already has a value

import cv2
import numpy as np

windowName = "Live Video"
cap = cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)
print("Width:" + str(cap.get(3))) # If we write 3 in the cap.get function, it will give us the width
print("Height:" + str(cap.get(4))) #4 gives height
cap.set(3,1280) # We rearrange the value we received with cap.get with the set and the value 3 becomes 1280
cap.set(4, 720) # we also changed the height with 720


print("New Width:" + str(cap.get(3)))
print("New Height:" + str(cap.get(4)))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # tumble the image and invert it with respect to the y-axis



    cv2.imshow(windowName, frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()