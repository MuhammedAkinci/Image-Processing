import cv2
import numpy as np
import pytesseract # we will use to read text
import imutils

img = cv2.imread("C:\PycharmProjects\Opencv\(r)esimden_plaka_okuma\(r)esimden_plaka_okuma.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filtered = cv2.bilateralFilter(gray, 5, 250, 250)
# here we are filtering. The filtering process changes according to what we write in parentheses. -->
# first we enter the image that we converted to gray, gray, then we enter the diameter values, these values are our smoothing values -->
We entered # parameter, sigma color and sigma space, respectively, after gray. change the result as you play with these values, the picture changes
# our purpose of filtering is to refine the sharp parts

edged = cv2.Canny(filtered,30,200)
# We detect the corners using the canny() function, first we entered the image we filtered, then the min and max values -->
# As you play with the min and max values, the corner finding rates in the picture change

edged1 = cv2.Canny(gray, 30, 200)
# here we did the same operation on the gray image, the number of corners was better because we did not filter before

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print("kontur: ", contours)
# now we will find the coordinates of the borders

cnts = imutils.grab_contours(contours)
# The purpose of grab_contours is to capture the appropriate contours, so we get the appropriate values in the contours
# and then we sort them, our purpose of doing this is to find the rectangular plate easier
#print("imutils.grab_contours: ", cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

# We sort the values in cnts and the key purpose is to sort by field. sorted can sort in different ways -->
# we are doing this to prevent it. Thanks to reverse=true, we can sort it in reverse order -->
# :10 means do it for values from 0 to 10
#print("lined contour: ", cnts)

screen = None # our purpose of using this depends on whether we find a closed value. if we find it there will be none

for c in cnts: # here we are processing to detect the license plate. we do it by marking the contours
    epsilon = 0.018 * cv2.arcLength(c, True) # our epsilon accuracy coefficient. 0.018 is an experimental number, it has no different meaning -->
    # arcLength allows us to find the arc length of the contours. -->
    # We pulled the values from cnts with #c and checked for spaces with True

    approx = cv2.approxPolyDP(c, epsilon, True)  # thanks to this we get a little closer to the correct contours values
    # so sometimes errors can occur in pictures with input and output, we use them to minimize these errors
    if len(approx) == 4: #If there are 4, we say there is a rectangle here.
        screen = approx # we said screen none above, but if there is a rectangle, we equate it to screen
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [screen], 0, (255,255,255), -1)
# here we detect the plate by drawing contours on our picture and draw the plate's perimeter and separate it from the picture
# We said mask at first, then we said screen because we would draw the conoturs inside the mask because it holds the coordinates -->
# and then we enter our drawing mode, then the colors, then the thickness

new_img = cv2.bitwise_and(img, img, mask=mask)# here we will print the plate inside that white area
# first we enter the image, then our second image source and finally a decision structure

(x, y) = np.where(mask == 255) # here we said hide all the white areas in the mask here in this line
(topx, topy) = (np.min(x), np.min(y)) # here we define the lower and upper corners so that we can crop and find the back picture
# Thanks to np.min, we find those values, starting from the top left and going down to the right, this is the vertex finding process.
(bottomx, bottomy) = (np.max(x), np.max(y))
# so this cropped the top lines so we can see only the license plate

cropped = gray[topx:bottomx + 1, topy:bottomy + 1] # We are cropping the images by taking the values aligned from the top and bottom
Our goal of making #+1 is to get the last value, that is, to reach all the values of the picture.

text = pytesseract.image_to_string(cropped, lang="eng")
 # we read with this and read the plate, or rather show the writings in the area we have determined
print("detected text", text)
#cv2.imshow("licence plate", img)
#cv2.imshow("gray", gray)
#cv2.imshow("filtered",filtered)
#cv2.imshow("edged", edged)
#cv2.imshow("edged1", edged1)
#cv2.imshow("mask", mask)
cv2.imshow("new_img", new_img)
cv2.imshow("cropped", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()