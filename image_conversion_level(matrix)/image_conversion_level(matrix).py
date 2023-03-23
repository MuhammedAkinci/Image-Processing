import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\(r)esim_donusum_duzeyi(matrix)\helikopter.jfif", 0)
row, col = img.shape

m = np.float32([[1, 0, 10], [0, 1, 70]])# the values we enter here are the degrees of operations such as scrolling in the picture

dst = cv2.warpAffine(img, m, (row, col)) # thanks to this, we can do operations such as scrolling the pictures

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()