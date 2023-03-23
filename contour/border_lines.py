import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\PycharmProjects\Opencv\Kontur\deneme.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# first we entered gray, then we will process the min and max values
# thresh binary already consists of binary 0s and 1s, this generally means that the output will be either black or white

contours,ret = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# the capitalized methods we write at the end make our work easier when making contours and at the same time, this is how it is used
# here we only use contours and contours from the rejection variables, but of course it would be ok if the rejection stopped for it to work -->
# these variables are put in different things. For the code to work, contours must be written first, then rejection (contours, rejection)

cv2.drawContours(img, contours, -1, (0,0,255), 3)
#we enter which picture we will draw at first, the other coordinates we will use -->
# How do we draw the shape, of course, according to what we wrote in contours, when we do the other -1, it draws everywhere, for example, if we write 0 there, it only draws the places outside the shape -->
# following numbers colors, final thickness

cv2.imshow("contour", img)
cv2.waitKey(0)
cv2.destroyAllWindoes()