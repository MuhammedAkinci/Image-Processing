# our goal in this lesson is how to create an image of computer
import cv2
import numpy as np

img = np.zeros((10,10,3), np.uint8) #we painted the screen we removed in the following 4 lines
img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,150)
img[0,3] = (255,255,15)

img = cv2.resize(img, (1000, 1000), interpolation= cv2.INTER_AREA) # The purpose of interpolation is to prevent some conflicts that may arise.

cv2.imshow("canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()