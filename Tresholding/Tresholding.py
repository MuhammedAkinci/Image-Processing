import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\PycharmProjects\Opencv\Tresholding\helikopter.jfif", 0) #0 turns gray

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21,2) # the numbers we wrote last->>
# allows a change to occur, but the remainder of the division by 2 should be 1 --> there is no need to question, this is the rule bro asdasdas
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21,2)

cv2.imshow("img", img)
cv2.imshow("img-th1", th1)
cv2.imshow("img-th2", th2)
cv2.imshow("img-th3", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()