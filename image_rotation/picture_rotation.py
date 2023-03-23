import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\(r)esim_donusum_duzeyi(matrix)\helikopter.jfif", 0) #0 turns gray
row, col = img.shape

M = cv2.getRotationMatrix2D((col/2, row/2), 90, 1,) # first we enter the column, then the row, then in which direction we want to rotate, and finally the scale
dst = cv2.warpAffine(img, M, (col,row))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
