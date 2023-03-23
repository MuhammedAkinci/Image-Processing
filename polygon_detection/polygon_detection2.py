# here we will identify the shapes you have taken on the webcam and name them according to the shape
import cv2
import numpy as np

def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("Settings")

cv2.createTrackbar("Lower-Hue", "Settings", 0, 180, nothing) # first we enter the name of the sled, then the window name, then the range, and nothing
cv2.createTrackbar("Lower-Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Lower-Value", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Hue", "Settings", 0, 180, nothing) # THANKS TO THIS AND SIMILAR LINES, I CAN MOVE THE SLIDES
cv2.createTrackbar("Upper-Saturation", "Settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Value", "Settings", 0, 255, nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

while 1:
    ret, frame = cap.read()

    # we turn and animate the image as we want, so when we flip it, for example, when we raise the right hand, it will actually appear on the screen and our hand will be raised on the PC, we have used it before
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    LH = cv2.getTrackbarPos("Lower-Hue", "Settings") # our purpose of doing this is to get the position of the slides so getTrackbarPos --> get the position of the trackbar so find
    # first we enter the position of the sled, then the window where the sled is located, that is, the window that will appear is whatever we name it.
    LS = cv2.getTrackbarPos("Lower-Saturation", "Settings") # our purpose of doing this is to get the position of the sleds
    LV = cv2.getTrackbarPos("Lower-Value", "Settings") # our purpose of doing this is to get the position of the sleds

    UH = cv2.getTrackbarPos("Upper-Hue", "Settings")
    US = cv2.getTrackbarPos("Upper-Saturation", "Settings") # I GET THE LOCATIONS OF THE SLIDES IN THIS AND SIMILAR PLACES
    UV = cv2.getTrackbarPos("Upper-Value", "Settings")

    lower_color = np.array([LH, LS, LV])
    upper_color = np.array([UH, US, UV]) # AND I STORE THE VALUES FINDING OUT OF THE ABOVE OPERATIONS THANKS TO THESE TWO LOWER_COLOR AND UPPER_COLOR

    mask = cv2.inRange(hsv, lower_color, upper_color) # We apply the values we find and then store using the mask variable

    kernel = np.ones((5, 5), np.uint8) # is used to remove the white dots on the black image after the camera is turned on, that is, after masking
    mask = cv2.erode(mask, kernel) # We are trying to erode the output image with mask

    contours, a = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # by doing this it finds contours in the mask

    for cnt in contours: # For loop purpose, we need the center points of the shape we have determined, we will do some operations using them
        area = cv2.contourArea(cnt) # will extract values from cnt contours and calculate their areas
        epsilon = 0.02 * cv2.arcLength(cnt, True) # true shows that the shape is closed We multiply the arc length formed in cnt by 0.02 and equal epsilon
        approx = cv2.approxPolyDP(cnt, epsilon, True) # by doing this, we make improvements to the contours we find with cnt

        x = approx.ravel()[0] # approx if it's a multidimensional array it all turns into a single line thanks to ravel
        y = approx.ravel()[1]

        # now we start contours below
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))

            if len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))

            if len(approx) > 6:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))

        # conoturs finished !!!

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(3) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()