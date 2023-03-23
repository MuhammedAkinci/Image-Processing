import cv2
import numpy as np

img = cv2.imread("C:\PycharmProjects\Opencv\Alistirmalar\(b)ulanik_goruntu_starwars.jpg")

blurry_img = cv2.medianBlur(img, 9)# we blurred the picture so the image is a bit blurry
laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()
# with this function, we check whether a picture is blurred or not, the function at the end returns us a value -->
# and according to that value, it is checked whether the picture is blurred or not.

if laplacian < 500 #We have set  500 for this study, it can also be a different value
    print(laplacian)
    print("this image is blurry image")


cv2.imshow("img", img)
cv2.imshow("blurry_img", blurry_img)

cv2.waitKey(0)
cv2.destroyAllWindows()