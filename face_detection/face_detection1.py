# here we will detect faces in a picture

import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\yuz_algilama\(f)ace.png")
face_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\yuz_algilama\(f)rontalface.xml")
# The purpose of the CascadeClassifier function above is to cascade that xml file according to cascade, and
# helps us to use

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 2)
# first we enter which picture it is, then we enter how much we will reduce the picture, and then we enter how many windows it will find faces -->
# the purpose of doing this is to make more sure to find -->
# Pictures will be found in the coordinates we give here and saved as a tuple on faces
# here we used the face_cascade file to find the coordinates of the face in the picture.

for (x, y, w,h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
# the aim of the above (x + w, y + h) is to go down with x + w to the right with y + h, that is, down to the right -->
# our purpose of doing this is because we didn't specify the range of the rectangle before

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()