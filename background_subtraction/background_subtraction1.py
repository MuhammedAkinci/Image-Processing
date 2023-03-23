import cv2
import numpy as np

cap = cv2.VideoCapture("C:\PycharmProjects\Opencv\(a)rka_plan_cikarma\car.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=150, detectShadows=True # this will do the background removal we did before -->
# enters 3 variables in it. First of all, we work on frames, the other is the threshold value, it is about detecting shadows.
# so detectShadow detects shadows




while 1:

    a, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    mask = subtractor.apply(frame) # we apply this function to the #mask variable and store the resulting values in the mask.
    # this subtractor.apply() applies the above createBackground part here and throws it into the mask

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()