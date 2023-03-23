
# here we have compared the thresh, blur, gray and normal versions of a map we have

import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Kontur\map.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3,3))
ret,thresh = cv2.threshold(blur, 40, 225, cv2.THRESH_BINARY)

cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()