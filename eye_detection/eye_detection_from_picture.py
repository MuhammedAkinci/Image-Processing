import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\goz_algilama\(r)esimde_goz_algilama.png")
eye_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\goz_algilama\(r)esimde_goz_algilama.xml")
face_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\yuz_algilama\(y)uz_algilama1.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y + h), (0,0,255), 3)

img2 = img[y:y+h, x:x+w]
# here actually trap the parts from y to y+x y and x to x+w and put them in img2 so img2 will express the face
gray2 = gray[y:y+h, x:x+w] # we do the same for the picture we turned gray

eyes = eye_cascade.detectMultiScale(gray2)

for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img2, (ex, ey), (ex + ew, ey+ eh), (255, 0, 0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
