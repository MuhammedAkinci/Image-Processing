import cv2
import numpy as np

img1 = cv2.imread("C:\PycharmProjects\Opencv\(b)itwise\s1.png")
img2 = cv2.imread("C:\PycharmProjects\Opencv\(b)itwise\s2.png")

bit_and = cv2.bitwise_and(img2, img1) # here we compared two images

bit_or = cv2.bitwise_or(img2, img1)
# when we do this, a solid black line appears in a window when we say imshow -->
# it's because the images are not the same size, so a black line is formed because the lines overlap -->
# If this is the imshow of the process I'm talking about, the part with cv2.imshow("bit_or", bit_or) is below

bit_xor = cv2.bitwise_xor(img2, img1)
#when we do this it will be like in "or" only difference is a triangle on the striped part

bit_not = cv2.bitwise_not(img2) # not get the reverse of the picture itself
bit_not2 = cv2.bitwise_not(img1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_not2", bit_not2 )


cv2.waitKey(0)
cv2.destroyAllWindows()