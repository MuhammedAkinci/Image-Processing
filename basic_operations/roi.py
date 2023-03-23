# roi --> region of interest --> area of interest
# Here we will separate the clone man's head from his body in clone.jpg :)

import cv2

img = cv2.imread("klon.jpg")
#print(img.shape[:2])

roi = img[30:150, 100:250] # We check 30:200 horizontal values, 200,300 vertical values

cv2.imshow("Klon", img)
cv2.imshow("Roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()