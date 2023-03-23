# Here we will do operations such as converting a picture with bgr to rgb
import cv2

img = cv2.imread("klon.jpg")

img_RGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # first we entered the source image, the other is the value that does the conversion
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Converted from bgr to hsv here
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converted from bgr to gray here

cv2.imshow("Klon Asker", img)
cv2.imshow("Klon RGB", img_RGB)
cv2.imshow("Klon HSV", img_HSV)
cv2.imshow("Klon GRAY", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()