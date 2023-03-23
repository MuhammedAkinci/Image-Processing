import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\insan_bedeni_algilama\(r)esimden_insan_bedeni_algilama.jpg")
body_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\insan_bedeni_algilama\(r)esimden_insan_bedeni_algilama.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bodies = body_cascade.detectMultiScale(gray, 1.1, 1)

for (x, w, y, h) in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 3)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()