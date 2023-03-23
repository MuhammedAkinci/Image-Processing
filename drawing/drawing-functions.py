# WE WILL DRAW SOME SHAPES HERE!!!


import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255  #The screen that came out with #255 became completely white

# this is the line
cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5)  #thickness method displays the thickness of the line
cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness=7) # Even if we write 5 or 7 directly without writing thickness, but let's see :)

# this is rectangular
cv2.rectangle(canvas, (20,20), (50,50), (0,255,0), 2) # If we want the shape we created to be filled, we write -1 instead of 2.


# this is the apartment
cv2.circle(canvas, (250,250), 100, (0,0,255), 5)

# this is triangle
p1 = (100,200)
p2 = (50,50)
p3 = (300,100)

#alternatif çizimler
points = np.array([[110, 200], [330, 200], [290, 220], [100,100]], np.int32) #np.int32 was put for values
cv2.polylines(canvas, [points], True, (0,0,100), 5) # If we want the shape we made to be closed, we make it True


cv2.line(canvas, p1, p2, (0,0,0), thickness=4)
cv2.line(canvas, p2, p3, (0,0,0), thickness=4)
cv2.line(canvas, p1, p3, (0,0,0), thickness=4)

# this is the ellipse
cv2.ellipse(canvas, (300,300), (80,20), 10, 90, 360, (255,255,0), -1)
# one line above the first values after the canvas are the center point, the next brackets are width and height -->
# the other number is the angle to be formed with the horizontal axis, the other bracket starting and ending angles are the last, the color and thickness


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()