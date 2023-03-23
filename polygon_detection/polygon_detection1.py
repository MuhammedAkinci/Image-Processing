# Based on the corner numbers of some shapes we have here, we will give them names according to the number of corners.
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX # the purpose of these fonts is the difference in writing styles
font1 = cv2.FONT_HERSHEY_COMPLEX # If we write opencv fonts on the internet to access such photos, we will get what we want.

img = cv2.imread("C:\PycharmProjects\Opencv\cokgen_algilama\polygons.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY) # binary part converts the image to 0 and 1 ie black and white
contours, b= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    cv2.drawContours(img, [approx], 0, (0), 5)

    x = approx.ravel()[0] # this ravel method puts all columns in line, 0th index of this approx.ravel we wrote represents x
    y = approx.ravel()[1] # 1 index also represents y

    if len(approx) == 3: # the purpose of doing this is to be able to find the polygons, if the length is equal to 3, it is already a polygon
        cv2.putText(img, "Triangle", (x, y), font, 1, (0)) # enter what to write first and then what to write -->
        # Where we will write in the img is x and y, we write it in the font, then we enter the values 1 and 0
        # the number we write as the second to last number, the size of the numbers that appear on the screen
        # The purpose of using putText is to put text on the name, that is, it allows us to write something on the shapes we find

    if len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))  # the number we write as the second to last number, the size of the numbers that appear on the screen

    if len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))  # the number we write as the second to last number, the size of the numbers that appear on the screen

    if len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), font, 1, (0))  # the number we write as the second to last number, the size of the numbers that appear on the screen

    elif len(approx) > 6:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0)) # the number we write as the second to last number, the size of the numbers that appear on the screen

cv2.imshow("İmg", img)
cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()