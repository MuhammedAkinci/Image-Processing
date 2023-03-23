import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\yuz_algilama\(y)uz_algilama1.xml")
eye_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\goz_algilama\(r)esimde_goz_algilama.xml")

vid = cv2.VideoCapture("C:\PycharmProjects\Opencv\goz_algilama\(v)ideoda_goz_algilama.mp4")

while 1:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (480, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 70, 80), 3)

    roi_frame = frame[y:y+h, x:x+w]
    # here actually trap the parts from y to y+x y and x to x+w and put them in the roi_frame so the roi_frame will represent the face
    roi_gray = frame[y:y+h, x:x+w] # we do the same for the picture we turned gray


    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow("video", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()