import cv2
import numpy as np

vid = cv2.VideoCapture("C:\PycharmProjects\Opencv\goz_izleme\eye_motion.mp4")

while 1:
    ret, frame = vid.read() # Our purpose for using ret was to return true if the frames were drawn correctly.


    if ret is False:
        break

    roi = frame[80:210, 230:450] #something like the pixels or values of the eye in this video

    rows, cols, e = roi.shape # We calculated the rows and columns here. We don't have anything to do with the e variable, it's just a write rule


    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    a, thresh = cv2.threshold(gray, 3, 250, cv2.THRESH_BINARY_INV)
    # our purpose in this last video is to make black places white and white places black so that we can examine the eye movements better
    contours, b = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    # This function sorts the values in it, but it will sort according to the operations we want while sorting.
    # will calculate the fields according to what we wrote, that is, according to what we wrote, and sort them accordingly
    # what we write at the end, we say start writing in reverse while sorting, that is, if it will write from big to small, it will write from big to small.

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
# This function helps us to get the coordinate values of the shape that will be formed.

        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # we draw on roi upper left coordinate x and y lower right isr the other parenthesis the other blue color and the last thickness


        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        # We draw the line in green color. Thickness 2, x + w/2 to center the purpose, the part with the other rows, that is, the finish line will come to the very end of the lines.

        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        # If we come to these horizontal lines, we will draw the values to the end of the columns

        break

    frame[80:210, 230:450] = roi
    # So here we said that the values held in the roi y, that is, the values in the operations we have done above, according to the coordinates in the frame, we said, and there will be exactly an overlap.
    # already seems like there is no difference, but we can say that overlapping values and minimizing possible errors.
    cv2.imshow("frame", frame)
    cv2.imshow("roi", roi)

    if cv2.waitKey(80) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()