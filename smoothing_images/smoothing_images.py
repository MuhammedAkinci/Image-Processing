# Our goal here is to post a post on a photo or make a photo more referral
# we've done things like reducing the blur in a photo or increasing the blur in a photo
# everything here is correct
import cv2
import numpy as np

img_filter = cv2.imread("D:\\OpenCV\\test_images\\filter.png")
img_median = cv2.imread("D:\\OpenCV\\test_images\\median.png")
img_bilateral = cv2.imread("D:\\OpenCV\\test_images\\bilateral.png")

blur =cv2.blur(img_filter,(7,5)) # we play on the picture as the numbers in parentheses change
cv2.imshow("original", img_filter) # here we show the img filter, we have already played with the image on the top line
cv2.imshow("blur", blur)

blur_gaussian = cv2.GaussianBlur(img_filter,(5,5), cv2.BORDER_DEFAULT) # we made the default related to the border lines we wrote at the end
cv2.imshow("blur2", blur_gaussian)


blur_median = cv2.medianBlur(img_median, 5) # no matter how much we play with the number here, the other picture that will come out is not original, that is, it changes
cv2.imshow("original", img_median)
cv2.imshow("blur_median", blur_median)


blur_bilateral = cv2.bilateralFilter(img_bilateral, 9, 75, 75) # trailing numbers change the picture
cv2.imshow("Original", img_bilateral)
cv2.imshow("blur_bilateral", blur_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()