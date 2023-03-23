import cv2
import numpy as np

image_path = "C:\PycharmProjects\Opencv\Alistirmalar\sablon_eslestirme_starwars (1).jpg"
template_path = "C:\PycharmProjects\Opencv\Alistirmalar\sablon_eslestirme_starwars2.jpg"

img = cv2.imread(image_path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread(template_path, 0) # Another gray conversion method can be done with the cv2.IMREAD_GRAYSCALE method
#Let's do this not by turning it into normal gray, but in a different way. If we enter 1 after the first variable, if we enter 0, it will show the picture in gray tone.
print(template.shape)# if we run the original image, the output will be (117, 121.3) because it is colored


w, h = template.shape[::-1]
# because we wrote -1 here, we wrote w,h because it takes -1 in reverse, so h,w. If there weren't -1, we would write h,w

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# this function allows us to match our template to a suitable place on the image -->
# we enter what we will place first, then what we will place on top of the last spelling rule

location = np.where(result >= 0.9)# We used np.where to find where result is greater than 0.7
# The closer we get 0.9 to 1, the smaller the coordinates will be because we are getting closer and closer to the center.
#print(location) # ie by zip below, we got rid of the number confusion when we actually print on this line and -->
# we found the coordinates more accurately and quickly

for point in zip(*location[::-1]):
# if we do this, we won't be able to find anything meaningful because it will travel one by one, we will get meaningful coordinates thanks to zip -->
# We put * in parentheses after zip, attention it also comes from zip
# If we write without -1, we have width and height values -->
# but with -1 we name those values in reverse so they are height and width
    print(point)
    cv2.rectangle(img, point, (point[0] + w, point[1] + h), (0, 255, 0), 3)

cv2.imshow("img", img)
cv2.imshow("result", result)
cv2.imshow("template", template)

cv2.waitKey(0)
cv2.destroyAllWindows()