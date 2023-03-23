import cv2
import numpy as np

img = cv2.imread("klon.jpg")
dimension = img.shape
print(dimension)

color = img[150,200] # the purpose of doing this is to get the color value of any pixel
# We make a top line at 1000, 1000, but if the size of our image is less than 1000, it will not work -->
# we used the shape method to understand the size of the image
print("BGR:", color)


blue = img[200, 100, 0] # We are curious about the value with index 0 between 420 and 500
print("Blue:", blue)

green = img[200, 100, 1]
print("Green:", green)

red = img[200, 100, 2]
print("Red:", red)

img[200, 100, 0] = 250
print("New Blue:", img[200, 100, 0])

blue1 = img.item(150, 200, 0) # The value in parentheses is assigned to blue1 with the item method
print("New blue:", blue1) # we have done assignment here

img.itemset((150, 200, 0), 172) # first we write in which coordinates we want to change, then we write which color we want to change
print("New Blue1:", img[150, 200, 0]) # here is the reason why we don't write blue 1 instead of img, we changed pixels here because we didn't assign

cv2.imshow("Klon Soldier", img)
cv2.waitKey(0)
cv2.destroyAllWindows()