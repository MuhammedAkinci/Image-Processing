#in this example we aim to find the corners of the drawing in a photo and we find

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\PycharmProjects\Opencv\corner_detection\opencv.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
#the first one we entered is gray, the other is how many corners there will be, the other is the quality value, and the other is the min distance between the corners.
# The goodFeaturesToTrack function allows us to find the corners. gray cannot be used like this directly in the above parenthesis, first it must be converted to float 32
corners = np.int0(corners) # the reason we do this is because we can't do it with float while drawing, we converted it to int because it was done with int

for corner in corners:
    x,y = corner.ravel()
    # While creating a circle with x and y, we used ravel to reach the values more easily, but we also needed to use corner values because they were not alone.
    cv2.circle(img, (x,y), 3, (0,0,255), -1)

cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()