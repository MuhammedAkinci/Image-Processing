# here we will work on the image of a white dog playing ball in our video named dog
import cv2
import numpy as np

cap = cv2.VideoCapture("C:\PycharmProjects\Opencv\Kontur\dog.mp4")

while 1: # purpose is to create an infinite loop here
    ret, frame = cap.read() # thanks to this, the operations on the videos become easier, so we can reach the values we want quickly

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # we converted the output image to hsv
    sensitivity = 15

    lower_white = np.array([0,0,255 - sensitivity]) # here we entered the range of values of the bottom color that will actually follow the dog
    upper_white = np.array([255, sensitivity, 255]) # here we entered the upper values of the color for dog tracking in the same way

    mask = cv2.inRange(hsv, lower_white, upper_white) #We said apply the values we assigned in hsv to lower and upper range to use video here.
    res = cv2.bitwise_and(frame, frame, mask = mask) #the purpose of this is to use a mask function to work properly.
    # The reason why it writes two frames inside is a special use, we can say that doing this creates a binary loop.We can find all kinds of information about -->
    #this usage by searching the internet as  # cv2.bitwise_and()

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()