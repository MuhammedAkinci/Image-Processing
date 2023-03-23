import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Kontur\contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thrash = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, a = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
area = cv2.contourArea(cnt) # With contourArea we find the area of the picture
print(area) # here we found area using contourArea
M = cv2.moments(cnt)
print(M) # here we find space using moments

perimeter = cv2.arcLength(cnt, True)
# here we find the perimeter The reason for entering True is if the shape is closed, it continues to calculate, that is, it checks whether the shape is closed or not.
print(perimeter)

cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh", thrash)

cv2.waitKey(0)
cv2.destroyAllWindows()