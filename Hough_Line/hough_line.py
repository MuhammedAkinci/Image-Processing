# here we create algorithms such as line determination and identify specific lines
# for example, lanes on the roads, we prepare the basis for them

import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Hough_Line\h_line.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)
# canny aim is to detect corners we take corners thanks to canny
# so thanks to canny we detected the lines in our photo and identified them

#cv2.HoughLines() # this and the HoughLinesP function below do pretty much the same job, but this makes the pc tired by using the cpu more, so we will use the HoughLinesP function
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap = 200)
# here we use it to determine the lines by entering the values
# Thanks to the maxLineGap function we entered at the end, the spaces in the photo are filled with lines thanks to this function.

for line in lines:
    # The main purpose of using for is that it is difficult to determine the lines at once with houghlinesp, so we used for, it helped in determining the line, it sent the values ​​to x and y by navigating the line lines, and we already set up the process according to x and y
    x1, y1, x2, y2 = line[0] #these x and y's actually represent the starting and ending points of the lines
    cv2.line(img, (x1, y1), (x2, y2), (0,255,0), 2) # first image, then start values, then end values, then color, last thickness


cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()