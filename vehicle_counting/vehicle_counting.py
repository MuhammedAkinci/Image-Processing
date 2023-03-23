# here we will count how many vehicles pass in a video we have
# we will count every car that crosses a line that we put somewhere in the video

import cv2
import numpy as np

vid = cv2.VideoCapture("C:\PycharmProjects\Opencv\(a)rac_sayma\(a)rac_sayma.avi")
backsub = cv2.createBackgroundSubtractorMOG2()

c = 0 # this will be our counter we will increment the c counter for every passing car

while True:
    ret, frame = vid.read()
    if ret:
        # means if the rejection is true this is the syntax so if the frames are shot correctly then the rejection will be true -->
        # we queried it here, so if the rejection is true (if the frames are taken correctly):
        fgmask = backsub.apply(frame)
        # here f max means remove the background, we perform this operation with backsub, it means apply application

        cv2.line(frame, (50, 0), (50, 300), (0, 255, 0), 2) # we drew 2 lines in this and the following line
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0), 2) # for each vehicle passing through this line, the counter will increase by 1 and the total number of vehicles will be found

        contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        try: hierarchy = hierarchy[0]
        except: hierarchy = []
            # try except purpose is to prevent some errors that we will encounter in the future, anyway, this is our purpose of using hierarchy

        for contour, hier in zip(contours,hierarchy):
            # this for loop will retrieve information about contours and hierarchy
            # The reason we keep it in the zip is because the contours and hierarchy values will be different when the vehicles are passing.

            (x, y, w, h) = cv2.boundingRect(contour) # with this function we are pulling values and throwing them to the other side
        # here we also calculate the width and height values of w and h as well as x and y

            if w > 40 and h > 40: # this means if the width and height are greater than 40 then the car is passing there so draw a rectangle
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

                if x > 50 and x < 70:
                    # here, if the coordinates pass through our line coordinates, that is, if they coincide, there is a car -->
                    # so the counter to find the number of cars is +1

                    c += 1

        cv2.putText(frame,"car: "+str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4,cv2.LINE_AA)
        # here we write car where there are cars in the frame, and in the other, 90,100 coordinates where the text will be blurred -->
        # Then we enter the font, something like the type of writing, the others are the thickness, color and font size.
        # The number after FONT_HERSHEY_SIMPLEX is the size of the car text, the other (0,0,255) the next number is the thickness of the car text

        cv2.imshow("img", fgmask)
        cv2.imshow("car counter", frame)
        cv2.imshow("fgmask", fgmask)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break



vid.release()
cv2.destroyAllWindows()