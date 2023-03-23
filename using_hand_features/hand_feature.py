import cv2
import numpy as np
import math

def findMaxContour(contours): # the purpose of this is to find the max area and max index
    max_i = 0
    max_area = 0

    for i in range(len(contours)): # here is to find the max one by comparing the fields with each other
        area_hand = cv2.contourArea(contours[i]) # so i will navigate and retrieve any value in the contours-->
        # then it will find the area of the contours it travels and equate it to area_face
        if max_area < area_hand:
            max_area = area_hand
            max_i = i

        try:
            c = contours[max_i] # this c will hold the contours values in max_i, that is, it will hold the max area

        except: # but if it fails -->
            contours = [0]
            c = contours[0] # so if it can't hold, we reset c

        return c

cap = cv2.VideoCapture(0)

while 1:
    a, frame = cap.read()
    frame = cv2.flip(frame, 1)

    roi = frame[50:200, 250:400] #frame[y1:y2] ve [x1:x2] -->
    # we need to take our face somewhere for detection on the screen, we will do this over the frame, we will hide it in roi
    # at first we wrote how far it should go on the y-axis, then we wrote it on the x-axis

    cv2.rectangle(frame, (200,50), (400, 250), (0,0,255), 0) # what we draw on, start and end points, color, thickness, font
    # The thickness of 2 at the end of the parenthesis 1 line above may cause an error, so we made 0 due to the shapes that will appear.
    # ie thickness 0 prevents errors that may occur by preventing it from being included in the max operation.

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 45, 79], dtype=np.uint8) # hsv range we set for the face, we entered these lower values
    upper_color = np.array([17, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1) # the purpose of this and 1 line up is to reduce the tingling of the mask
    mask = cv2.medianBlur(mask, 15) # we also cleaned the image that appeared in the mask thanks to this

    # we enter contours

    contours, b = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        try:  # Sometimes we can get an error while coding, so we used try, except
            c = findMaxContour(contours)
        # since our main purpose here is inside the rectangle, the max contours will be there and we will hide them in c

            extLeft = tuple(c[c[:, :, 0].argmin()][0])
            # inside [c[:, :, 0].argmax()] the following part will find us the smallest x value with the help of argmin()
            # (c[c[:, :, 0].argmin()][0]) this way x and o will find y of x
            extRight = tuple(c[c[:, :, 0].argmax()][0])
            # that is, the part with 0 in the innermost parenthesis looks at x's, even if it is 1, it looks at y's. and we said argmax because where x is max is right side
            extTop = tuple(c[c[:, :, 1].argmin()][0])
            # here we wrote a instead of 0 in the innermost parenthesis, because the ball is up and down, we are looking for y, think of it as the x,y axis


            cv2.circle(roi, extLeft, 5, (0,255,0), 2)
            cv2.circle(roi, extRight, 5, (0, 255, 0), 2)
            cv2.circle(roi, extTop, 5, (0, 255, 0), 2)


            cv2.line(roi, extLeft, extTop,(255,0,0), 2) # drew a line from the far left to the top here
            cv2.line(roi, extTop, extRight, (255, 0, 0), 2)
            cv2.line(roi, extRight, extLeft, (255, 0, 0), 2)
            # We find the length and angles of the lines we created in the 3 lines above

            a1 = math.sqrt((extRight[0] -  extTop[0]) ** 2 + (extRight[1] - extTop[1]) ** 2)
            # so we find the length of the far right and the top, here the length of the rightmost to the top
            c1 = math.sqrt((extTop[0] - extLeft[0]) ** 2 + (extTop[1] - extLeft[1]) ** 2)
            # so we find the lowest to the far right length, here the length of the lowest to the far right
            b1 = math.sqrt((extRight[0] - extLeft[0]) ** 2 + (extRight[1] - extLeft[1]) ** 2)
            # so we find the length of the lowest to the highest here is the length of the lowest to the highest

            try: # sometimes we use try except to prevent variables 0 value and 0 division error in our operations

                angle_a1b1 = int(math.acos((a**2+b**2-c**2)/(2*b*c))*57) # this is the cos rule we know
                # We find the angle between the sides a1 and b1 so it becomes an up line
                # on the bottom, we print the angle we found above where we want on the screen

                cv2.putText(roi, str(angle_a1b1), (extRight[0]-50, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
                # write the result of the angle obtained as a result of the operation we have done here, exactly to the left of the junction of a1b1
                # where to write first, then we convert the text to string, then we enter the coordinates of the place where it will be written, -->
                # then we entered the font type, then the font thickness of the angle, then the color, and finally we made the text look better with LINE_AA

                if angle_a1b1 > 70: # we told him to draw a rectangle if the angle is greater than 70 it's totally arbitrary
                    cv2.rectangle(frame, (0, 0), (100, 100), (255, 0, 0), -1)

                else:
                    pass

            except:
                cv2.putText(roi, "!", (extRight[0] - 50, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        except:
            pass
    else:
        pass

    cv2.imshow("frame", frame)
    cv2.imshow("roi", roi) # shows the partition inside the rectangle on the screen in a different roi window, but only as much as the rectangle covers
    #cv2.imshow("mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
