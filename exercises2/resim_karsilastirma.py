# here we can find out if they are equal by comparing the two images with each other, we compare the pixels

import cv2
import numpy as np

path1 = "C:\PycharmProjects\Opencv\Alistirmalar\karsilasitrma_aircaft.jpg"
path2 = "C:\PycharmProjects\Opencv\Alistirmalar\karsilasitrma_aircaft1.jpg"

img1 = cv2.imread(path1)
img1 = cv2.resize(img1, (640,480))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2, (640,480))

img3 = cv2.medianBlur(img1, 7)
#our purpose of doing this is to corrupt an active image and assign it to a different variable and get different results from the output

if img1.shape == img2.shape:
    print(f"first picture {img1} and the second picture {img2} has same size")

else:
    print(f"first picture {img1} and the second picture {img2} hasn't same size")

# diff == difference
diff = cv2.subtract(img1, img3) # this function compares 2 pictures and paints the different parts a different color
b, g, r = cv2.split(diff) # Thanks to split, we split the diff and reach the bgr values, then we sync


if cv2.countNonZero(b) == 0 and  cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
# this function scans the values of the variable it enters one by one and determines how many non-0's
    print("this 3 pictures are completely equal")

else:
    print("This 3 pictures are not equal")

cv2.imshow("aircraft1", img1)
cv2.imshow("aircraft2", img2)
cv2.imshow("Difference", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()