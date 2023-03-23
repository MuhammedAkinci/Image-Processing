import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 # The screen that came out with 255 turned completely white

font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas, "OpenCV", (30,100), font1, 4, (0,0,0), cv2.LINE_AA)

'''cv2.putText(canvas, "OpenCV", (30,100), font2, 4, (0,0,0), cv2.LINE_AA)
#cv2.putText(canvas, "OpenCV", (30,100), font3, 4, (0,0,0), cv2.LINE_AA)'''
# The first value after canvas is what we write inside the shape, the other brackets, between which coordinates -->
# font1 is the size of the text -> 4, so the next parenthesis is the color of the text, and the last is the type of the font
# WE CAN USE ANY TYPE OF FONT WE WANT, BUT THE FONT AVAILABLE IN EACH EACH IS DIFFERENT, THE CONTENT IS THE SAME !!!


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()