import cv2
import numpy as np
from collections import deque # bu fonksiyon sayesinde bir listeleme işlemi yapacağız resim çizmede işimize yarıyacak

cap = cv2.VideoCapture(0)

kernel = ((5,5), np.uint8)

lower_blue = np.array([100, 60, 60])
upper_blue = np.array([140, 255, 255])

blue_points = [deque(maxlen=512)]
#here we will list (keep) the blue drawings in this variable while drawing on the screen
# we said it should be 512 long, the purpose of this is because the drawings are made up of points, we will hide the points in it.
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

colors = [(255,0,0), (0,255,0), (0,0,255), (0,255,255)] # will hold these color values, each representing the above colors respectively

colors_index = 0

# WE HAVE DONE BETWEEN NP.ZEROS AND NAMEWINDOW("PAINT") WITHIN WHILE BECAUSE WE DO THE SAME ACTION WITHIN FRAMES
# BECAUSE WE ALSO DRAW IN FRAMES

paint_window = np.zeros((471, 636,3)) + 255
# We created a white screen of 471, 636 and said there are 3 color values
# The purpose of the 255 we put at the end is to turn white by adding 255 to all values on the 473,636 screen.

paint_window = cv2.rectangle(paint_window, (40, 1), (140, 65), (0, 0, 0), 2) # white button. it's empty
# we save the drawings we made here in paint_window, we normally do not write them, but in order not to get an error
# actually we created a button here, this button is the button that will clear the screen when we press it

paint_window = cv2.rectangle(paint_window, (160, 1), (255, 65), colors[0], -1) # blue button, filled with -1
paint_window = cv2.rectangle(paint_window, (275, 1), (370, 65), colors[1], -1) # green button, filled with -1
paint_window = cv2.rectangle(paint_window, (390, 1), (485, 65), colors[2], -1) # red button, filled with -1
paint_window = cv2.rectangle(paint_window, (505, 1), (600, 65), colors[3], -1) #yellow button, filled with -1
In # colors[0] we have already kept the colors and their values above, as the color array +1 comes the colors blue, grren, red and yellow, respectively
font = cv2.FONT_HERSHEY_SIMPLEX # the purpose of this is the shape of the text when typing in putText



cv2.putText(paint_window, "Clear All", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
# we entered where to write, what to write, coordinates, typeface, font scale?, entered color, size and spelling beautification
cv2.putText(paint_window, "Blue", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paint_window, "Green", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paint_window, "Red", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paint_window, "Yellow", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

cv2.namedWindow("Paint") # this picture table we will draw inside this


while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    frame = cv2.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (160, 1), (255, 65), colors[0], -1)
    frame = cv2.rectangle(frame, (275, 1), (370, 65), colors[1],-1)
    frame = cv2.rectangle(frame, (390, 1), (485, 65), colors[2],-1)
    frame = cv2.rectangle(frame, (505, 1), (600, 65), colors[3], -1)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame, "Clear All", (49, 33), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Blue", (185, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Green", (298, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Red", (420, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Yellow", (520, 33), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    if ret is False:
        break
        # this is for exit loop when video ends or frames are misread
        # because if we do this he won't get tired at the computer because he doesn't work in vain

    mask = cv2.inRange(hsv, lower_blue, upper_blue,)

    kernel = ((5, 5), np.uint8)

    mask = cv2.erode(mask, (5,5), iterations=2) # this and the following 2 lines to beautify the output

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5,5)) # for example the tingles are gone

    mask = cv2.dilate(mask, (5,5), iterations=1) # thicken here too


    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    center = None
    # this center point is when the center of the circle we draw in the drawing enters the coordinates of the buttons, then we get the color


    if len(contours) > 0: # If there is a value in contours, we said enter it here

        max_contours = sorted(contours, key=cv2.contourArea, reverse=True)[0] # sort the areas in contours from largest to smallest

        ((x,y), radius) = cv2.minEnclosingCircle(max_contours)
        # here we create the circle we mentioned in the center, this center will return the x,y and radius values
        cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 0), 3)
        # we will draw on the frames, their centers will be x, y, radius will be radius, color and thickness
        # Our aim is to put int, the result can be float, so the code will not work, we converted it to int to avoid this error

        M = cv2.moments(max_contours) # find the center point of the circle

        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # thanks to this we divide the value from m10 by m00 and find the x value of the center and then we find the y value

        if center[1] <= 65: # If center[1], that is, if the y value is greater than 65, we said why 65 because the y value is the same in the frames above.

            if center[0] >= 40 and center[0] <= 140:
                # If x is between 40 and 140, the corresponding clear all part
                # so we will take all the color value and set it to 0

                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]

                blue_index = 0
                gree_index = 0
                red_index = 0
                yellow_index = 0

                # we made all colors 0 above so the screen is cleared

                paint_window[67:,:,:] = 255
                # here we made all x,y values after 67 in paint_window reason to start from 67 -->
                # 67 coincides with the buttons, we will not do anything to them, so we started from 67 and later.

            elif center[0] >= 160 and center[0] <= 255:
                colors_index = 0
                # colors_index will be 0 if above condition is met because colors[0] already has blue value
                # also, between 160 and 255 already corresponds to the blue color, we can check it from above

            elif center[0] >= 275 and center[0] <= 370:
                colors_index = 1

            elif center[0] >= 390 and center[0] <= 485:
                colors_index = 2

            elif center[0] >= 505 and center[0] <= 600:
                colors_index = 3

        else: # Here we said that if it is greater than 65, if it is not less than 65, so here we go into drawing works.

            if colors_index == 0:
                blue_points[blue_index].appendleft(center)
                # that is, we will append the values that center travels to the left of the list with appendleft, and then we draw these points


            elif colors_index == 1:
                green_points[green_index].appendleft(center)

            elif colors_index == 2:
                red_points[red_index].appendleft(center)

            elif colors_index == 3:
                yellow_points[yellow_index].appendleft(center)

    else: # here we increased the indexes 1 by 1


        blue_points.append(deque(maxlen=512))
        blue_index += 1

        green_points.append((deque(maxlen=512)))
        gree_index += 1

        red_points.append(deque(maxlen=512))
        red_index += 1

        yellow_points.append(deque(maxlen=512))
        yellow_index += 1

    points = [blue_points, green_points, red_points, yellow_points] # this will hold our pointes


    # the purpose of these forms is to set the points array because it is multidimensional.
    for i in range(len(points)): # i points will travel as long as
        for j in range(len(points[i])): # j will traverse i values
            for k in range(len(points[i][j])): # k will traverse the j and i values

                if points[i][j][k-1] is None or points[i][j][k] is None:
                    # the purpose of this is if the start and end values of points are not null
                    continue

                    cv2.line(frame, points[i][j][k-1], points[i][j][k], colors[i], 2)
                    # the color list was empty we entered i in it will write the points in the content order of the points array
                    cv2.line(paint_window, points[i][j][k-1], points[i][j][k], colors[i], 2)




    cv2.imshow("frame", frame)
    cv2.imshow("paint_window", paint_window)
    cv2.imshow("mask", mask)



    if cv2.waitKey(3) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()