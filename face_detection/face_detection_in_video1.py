# here we will detect faces in a video
import cv2
import numpy as np

vid = cv2.VideoCapture("C:\PycharmProjects\Opencv\yuz_algilama\(v)ideoda_yuz_algilama.mp4")
face_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\yuz_algilama\(y)uz_algilama1.xml")

while 1:
    ret, frame = vid.read() # let's read each frame one by one
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # turning every frame gray for easy detection of haar-like features

    faces = face_cascade.detectMultiScale(gray, 1.1, 2)
    # now let's find the coordinates of the faces on each square using our cascade file

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y),(x + w, y + h), (0,255,0), 2)

    cv2.imshow("image", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()