# here we will overlay two images and switch between images as we change our sled value

import cv2
import numpy as np

def nothing(x):
    pass

img1 = cv2.imread("C:\PycharmProjects\Opencv\Alistirmalar\(r)esim_donusum_uygulamasi1.jpg")
img1 = cv2.resize(img1, (640,480))

img2 = cv2.imread("C:\PycharmProjects\Opencv\Alistirmalar\(r)esim_donusum_uygulamasi2.jpg")
img2 = cv2.resize(img2, (640,480))

output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# the purpose of this is to add the weights of the images on top of each other, making our work easier in the transition
# first we enter the first image we will add, then the weight of the image, then we do the same for the second image, and finally we enter the default gamma value
windowName = "Transition Program"
cv2.namedWindow(windowName)

cv2.createTrackbar("Alpha-Beta",windowName,0,1000,nothing)
# alpha actually output is for img1 in parentheses In beta for the other, this trackbar will go back and forth between 0 and 1000

while 1:
    cv2.imshow(windowName,output)
    alpha = cv2.getTrackbarPos("Alpha-Beta", windowName)/1000
    # the purpose of this is to make the sled go between 0 and 1000 so we divide by 1000
    beta = 1 - alpha # beta is in between so we did it like this between 1 and alpha so
    output = cv2.addWeighted(img1, alpha, img2, beta, 0) # we did this because the output value will change in each frame
    print(alpha, beta)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()