import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Arac_algilama\(r)esimde_arac_algilama.jpg")
car_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\Arac_algilama\(r)esimde_arac_algilama.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.2, 1)

for (x, w, y, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, x + h), (0,0,255), 3)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()