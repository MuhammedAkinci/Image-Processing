# here we find the geometric center of gravity of a shape we have

import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Kontur\contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
M = cv2.moments(thresh)
# this method keeps some image related values
# Actually, we are using M above so that we can use the values below when we print(M) in x and y.

x = int(M["m10"] / M["m00"]) #here is the x part of the center of gravity where y and x are varia in geometry this is x
y = int(M["m01"] / M["m00"]) #here we find y

# There are values when we print(M) in the two lines above, we use them to find the center of gravity
# The purpose of writing int in front of the parenthesis is that it is possible that the result will be in float type in the division operation, so we converted it to int.

cv2.circle(img, (x,y), 5, (255,255,0), -1) # here we drew a small circle to see the center of gravity

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()