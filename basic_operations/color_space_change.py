import cv2
import numpy as np

cap = cv2.VideoCapture("1.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == False: #this is because; not get error. The error does not prevent the code from working, but it does not allow us to get full efficiency -->
        # Still, the little details matter.
        break


    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()