import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8)
# + 255 //// # np.zeros purpose is to create a black canvas in a certain area, that is to create a kind of drawing screen
#3 is meant for color while np.uint8 is for drawing
# In order for the color of the resulting drawing screen to be white, we need to add + 255 to the end of the above line of code, if we enter 100, it will turn gray

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
