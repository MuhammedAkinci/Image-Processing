# here we will write a code that will only follow the eraser in the video called hsv.mp4. The focus of the code we will write will be the eraser.
import cv2
import numpy as np

def nothing(x): # we do this just to avoid errors

    pass

cap = cv2.VideoCapture("C:\PycharmProjects\Opencv\HSV_ile_nesne_saptama\hsv.mp4")

cv2.namedWindow("Trackbar")

cv2.createTrackbar("LH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("LS", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("LV", "Trackbar", 0, 255, nothing)
# first we enter the sled name, then the window name, then the sled we entered will switch between values
cv2.createTrackbar("UH", "Trackbar", 0, 179, nothing)
cv2.createTrackbar("US", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UV", "Trackbar", 0, 255, nothing)

while 1:
    a, frame = cap.read()
    frame = cv2.resize(frame, (500, 350))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Trackbar") # we will do this in others to store the values of the above LH sled
    ls = cv2.getTrackbarPos("LS", "Trackbar")
    lv = cv2.getTrackbarPos("LV", "Trackbar")

    uh = cv2.getTrackbarPos("UH", "Trackbar")
    us = cv2.getTrackbarPos("US", "Trackbar")
    uv = cv2.getTrackbarPos("UV", "Trackbar")

    lower_blue = np.array([lh, ls, lv]) # We will keep the hsv values in them to apply a mask. we entered the lower values
    upper_blue = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, lower_blue, upper_blue) # will make it apply when values change when we play with the sled here
    bitwise = cv2.bitwise_and(frame, frame, mask=mask) # in the process we did, the output will be black and white, but we want to see the blue color in the video, we did it to see it

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("bitwise", bitwise)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()