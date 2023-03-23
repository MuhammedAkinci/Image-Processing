import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = np.zeros((500, 500), np.uint8)
img = cv2.imread("C:\PycharmProjects\Opencv\histogram\opemcv.png")

cv2.rectangle(img, (0,60), (200, 150), (255, 255, 255), -1) # we drew a rectangle here

cv2.imshow("img", img)
plt.hist(img.ravel(), 256, [0,256]) # Required to make a ravel histogram, the other is the range of how many values are at the end
# ravel allows us to combine pixel values into a single line plt.hist allows us to make a histogram
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
