# in the video we convert car.mp4 to places where cars pass,
#we improve the first frame and other frames while doing absdiff()
import cv2
import numpy as np

cap = cv2.VideoCapture("C:\PycharmProjects\Opencv\(a)rka_plan_cikarma\car.mp4")

a, first_Frame = cap.read() #We took the first frame with cap.read, we can throw it into an infinite loop so that it shoots infinite times
first_Frame = cv2.resize(first_Frame, (640, 480))
first_gray = cv2.cvtColor(first_Frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5,5), 0) # we use the blur method to soften the output image

while 1:
    a, frame = cap.read()   #We took the first frame with cap.read, we can throw it into an infinite loop so that it shoots infinite times
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  # we use the blur method to soften the output image

    diff = cv2.absdiff(first_gray, gray) #we use it to compare the first frame with the other frames -->
    # First, we enter the variable we will compare first, then with which variable we will compare the first variable.
    
    b, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY) # the purpose of doing this is when the screen comes out without this diff window -->
    # output had color shift due to gray colors, but our goal is to output only black or white -->
    # so we applied threshold and changed the image to black and white only thanks to thresh_binary

    cv2.imshow("frame original", frame)
    cv2.imshow("first", first_Frame)
    cv2.imshow("diff", diff)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()