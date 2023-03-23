import cv2
import numpy as np

img1 = cv2.imread("C:\PycharmProjects\Opencv\Hough_Line\coins.jpg")
img2 = cv2.imread("C:\PycharmProjects\Opencv\Hough_Line\yuvarlaklar.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 =cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# YOU WILL USE MEDIAN AND BLUUR TO REDUCE ANTING AND SOME THINGS IN THE VIDEO

img1_blur = cv2.medianBlur(gray1, 5) #first we enter the value we want to blur, then we enter the size(size)
img2_blur = cv2.medianBlur(gray2, 5) #first we enter the value we want to blur, then we enter the size(size)

circles = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1, img1.shape[0]/4, param1=200, param2=10, minRadius=15, maxRadius=80)
#We are looking for the circles in the photo like this, first we enter what we blur, then we enter the detection method, the method is always the same, then we enter the resolution -->
#then we enter the minimum distance between the circles. The aim of the method we use at the end is if we enter few numbers, we find many circles, if we enter many numbers, we find less circles. We find the circles based on the picture.
#The first we entered is the param1 gradient value and the other is the threshold value, these are specific to this method and the values against them are also important.
 # We write assuming that our circles are between 5 and 30 radius values in the last radius we entered.

circles2 = cv2.HoughCircles(img2_blur, cv2.HOUGH_GRADIENT, 1, img2.shape[0]/4, param1=200, param2=10, minRadius=15, maxRadius=80)

if circles is not None: # so the circles we're talking about here are not hollow
    circles = np.uint16(np.around(circles)) #normally we used to write uint8, now we can write 16 if we want, we can write 32 if we want, the purpose of this is just to change the range
    # rounds the values in around circles, converts them to uint16 and then puts them back into circles

    for i in circles[0,:]:# let i travel in circles from 0 to the end
# We determine the center of the circle that we will draw with 0 and 1 of the assigned values, and the radius with the 2nd
        cv2.circle(img1, (i[0], i[1]), i[2], (0,255,0), 2)

   # for s in circles2[0,:]:
    #    cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2)

# TO USE CIRCLES 2, VALUES CHANGE ACCORDINGLY ABOVE ^^^

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()