# here we made the background color of the map we have black and we painted the shapes on the map blue.
# After , we determined the bends by drawing lines on the outer bend parts and revealed the outer bend shape.
import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Kontur\map.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3,3))
ret,thresh = cv2.threshold(blur, 40, 225, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = [] # We made an empty hull array to keep the convex hull points, and we'll throw it in as we find it,

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], False)) # returns the index where the value is found because it is false here; if true, it returns the value itself.
    # here is a concept called return points in front of false. return points optional

bg = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

for i in range(len(contours)):
    cv2.drawContours(bg, contours, i, (255, 0, 0), 3, 8, hierarchy)
    # first we entered what to draw the drawing on, then we entered the contours points to draw on bg -->
    # then we entered the index of each conoturs, then we entered the color, then we entered the thickness of the drawing, the linetype, and finally we entered the hierarchy
    cv2.drawContours(bg, hull, i, (0, 255, 0), 1, 8)

cv2.imshow("image",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()