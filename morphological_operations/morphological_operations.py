import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Tresholding\helikopter.jfif", 0)

kernel = np.ones((5,5), np.uint8) # the higher the value here, the more distorted the picture
erosion = cv2.erode(img, kernel, iterations = 1) # here we can say that the picture is kind of examining
dilation = cv2.dilate(img, kernel, iterations = 1) # here we can say that the picture becomes thicker, the example is not important, the logic is important
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN ,kernel) # noises on the picture are removed
gardient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) # DRAW THE EXTERNAL PART OF THE PICTURE, LEAVING THE OTHERS THE SAME
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)  # dims and erases


cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("gardient", gardient)
cv2.imshow("tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()