# here we will write some operations using mouse in the video
# we will draw a circle on the image in the video by using the key we assigned in the code

import cv2
import numpy as np

cap = cv2.VideoCapture("C:\PycharmProjects\Opencv\mause_kullanimi\line.mp4")

circles = []
def mause(event, x, y, flags, params):
# We keep the operation we do in the event, x and y are the center coordinates, that is the point we press with the mouse.
# we didn't use falgs and params, we wrote from formality

    if event == cv2.EVENT_LBUTTONDOWN:# so if the event is equal to the left button, do the following
        circles.append((x,y)) # the purpose of doing this is that if we press many places on the screen, there will be many circles, we have created on the horizontal def to keep them

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mause)
# to detect the operation we do with this mouse. the first value is the window name but the name we set above is not gini what we did before-->
# then we enter a function to understand which button of the mouse we will do the operations with.

# now we start the frames

while 1:
    a, frame = cap.read()
    cv2.resize(frame, (500, 350))
    for center in circles: # we will draw a circle around the center so it will travel in the center circles
        cv2.circle(frame, center,20, (255,0,0), -1)# The center of the circles we will draw on the frame will be the center, then the radius and then the radius, then the color

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27: # means 27 esc

        break
    elif key == ord("h"): # but if we press the h key, we create a function that clears the window
        circles = [] # The center was always filled with for above, but if we say h here, we emptied it as it appears in the code.

cap.release()
cv2.destroyAllWindows()