import cv2
import numpy as np

vid = cv2.VideoCapture("C:\PycharmProjects\Opencv\insan_bedeni_algilama\(v)ideolarda_insan_bedeni_algilama.mp4")
body_cascade = cv2.CascadeClassifier("C:\PycharmProjects\Opencv\insan_bedeni_algilama\(r)esimden_insan_bedeni_algilama.xml")

while 1:
    ret, frame = vid.read() # tek tek okuduk anları# we read the moments one by one
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # turn gray


    bodies = body_cascade.detectMultiScale(gray, 1.1, 4) # we put the information in the body cascade into the bodies

    for (x, w, y, h) in bodies: # here we circled the people you found in the video
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0,0,255), 3)

    cv2.imshow("video", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()