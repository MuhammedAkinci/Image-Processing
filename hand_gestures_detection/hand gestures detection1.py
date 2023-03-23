import cv2
import numpy as np
import math

vid = cv2.VideoCapture(0)

while (1):

    try:
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)

        kernel = np.ones((3,3), np.uint8)

        roi = frame[100:300, 100:300] # here we enter the coordinates for x and y
        # these coordinates are the coordinates of the rectangle that will appear on the screen
        cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 0)

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        lower_skin = np.array([0, 20, 70], np.uint8)
# in this line, we entered the lower color values of our hand to determine
        upper_skin = np.array([20, 255, 255], np.uint8) # here we set the upper values, we entered the values to detect our hand


        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        mask = cv2.dilate(mask, kernel, iteration=4) #The purpose of using kernel here is to make the black parts white.

        mask = cv2.GaussianBlur(mask, (5,5), 100) # the purpose of this is to delete the images that occur in the output (5.5) height and width values


        _, contours, a = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # _ ve a önemli değil hata almamak için sadec
        cnt = max(contours, key=lambda x:cv2.contourArea(x))
        # this function selects the largest of the values it receives as input and sends it as output
        # key=lambda x:cv2.contourArea(x) this is special usage will find areas in contours and select the largest

        epsilon = 0.005 * cv2.arcLength(cnt, True) # this and the code below provide a better approach to contours
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        hull = cv2.convexHull(cnt)#a convex cover (line) around our hand, etc. We wrote to create

        area_hull = cv2.contourArea(hull) # this variable will hold the hull area and this will make it easier for us to find the area of the hand
        area_cnt = cv2.contourArea(cnt)# here we applied it to find hand values because the required hand coordinates are in cnt
        area_ratio = ((area_hull - area_cnt) / area_cnt) * 100

        # here we will find what percent of the area we do not have in the cover that will form
        # subtract the area of our hand from the whole area and divide it by the area of our hand and multiply the result by 100 to find the value

        hull = cv2.convexHull(approx, returnPoints=False)
        # here we got the indices of contours thanks to convexHull
        # Our purpose of writing False is to find the indices, so if we said True, it would find the contours.
        defects = cv2.convexityDefect(approx, hull)# this will also find defects due to convexity

        L = 0 #To determine the number of defects, we first gave zero and left it like that.


        for i in range(defects.shape[0]):# here i will loop as much as the value in defect
            s, e, f, d = defects[i, 0] #here are 1 each! will increase and transfer the values to s,e,f,d as it increases


            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])

            b = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            c = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            d = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            # Since the triangle shape that will be formed in the b, c, d lines above has 3 corners, we wrote it like this and found their coordinates

            s = (b + c + d) / 2
            # To find the area of a triangle whose side lengths we know in #geometry, we first add all the sides of the triangle -->
            # After we divide the resulting value by 2 and then use the result to find the area
            area = math.sqrt(s * (s - b) * (s - c) * (s - d)) # böyle yaparak kenar uzunluklarını bildiğimiz üçgen alanına ulaşıyoruz
            v = (2 * area) / b # here we will find the distance between the points and the convex


            angle = math.acos((c ** 2 + d ** 2 - b ** 2) / (2 * c * d)) * 57
            # we find the angle between acos and two sides using cosine
            # this is a rule we better write it like this

            if angle <= 90 and d > 30:
                L += 1 # if the decision structure is realized, our flaw is increased by 1
                cv2.circle(roi, far, 3, [255, 0, 0], -1)
                # here we draw circles where the headlights in the roi area are the farthest and corner points ie headlight
                # we will draw the headlight coordinates in roi. Let the radius of the circle be 3, then we entered the color value and -->
                # we filled the circles we drew last with -1

            cv2.line(roi, start, end, [255, 0, 0], 2) # we draw to determine the start and end points

        L += 1

        font = cv2.FONT_HERSHEY_SIMPLEX # our purpose here is only the shape of the text on the screen

        if L == 1:
            if area_cnt < 2000: # this is the case when the hand is not in that rectangle
                cv2.putText(frame, "put your hand in the box", (0, 50), font, 0.5, (0,0,255), 3, cv2.LINE_AA)

            else:
                if area_ratio < 12:# we said here if the percentage of the area we do not have is less than 12
                    cv2.putText(frame, "0", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                elif area_ratio < 17.5:
                    cv2.putText(frame, "GOOD LUCK:)", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                else:
                    cv2.putText(frame, "1", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif L == 2: # if there are 2 defects

            cv2.putText(frame, "2", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif L == 3:
            if area_ratio < 27:
                cv2.putText(frame, "3", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
            else:
                cv2.putText(frame, "OK!", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif L == 4:
            cv2.putText(frame, "4", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif L == 5:
            cv2.putText(frame, "5", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif L == 6:
            cv2.putText(frame, "reposition", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA) #6 Saying I don't understand something when you find fault

        else:
             cv2.putText(frame, "reposition", (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow("mask", mask)
        cv2.imshow("frame", frame)

    except:
        pass

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
vid.release()