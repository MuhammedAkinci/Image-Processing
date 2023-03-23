# here we have determined the convex and convex points of a star shape
#After, we determined the outer bend parts by drawing straight lines.
#After, we determined the inner bend parts by marking them with small circles, and in this way, we found the inner and outer bends.

import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Kontur\star.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0) # There was cv2.THRESH_BINARY here, but we assigned a number to it because the error was given for value not found in defects.shape.

contours, a = cv2.findContours(thresh, 2, 1)# There was cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE here, but we assigned a number to it because the error was not found for value in defects.shape.
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints =  False)
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
# by doing this, we wanted i to return as the 0th element of the defects size
    s,e,f,d = defects[i, 0] # s -> start point, e -> end point, f -> farthest point, d -> distance
    # we will draw using s and e, it represents things that are bent inside
    startPoint = tuple(cnt[s][0])
    endPoint = tuple(cnt[e][0])
    farPoint = tuple(cnt[f][0])

    cv2.line(img, startPoint, endPoint, [0, 255, 0], 2)
    cv2.circle(img, farPoint, 5, [0, 255, 0], -1)# first we entered where to draw, then we entered the places that were bent inwards, then we entered the radius

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()