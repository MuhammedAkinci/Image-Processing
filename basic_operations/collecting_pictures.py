import cv2
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 255), -1)

add = cv2.add(circle, rectangle)
print(add)  # we added the circle and rectangle values together with the add method
print(add[256, 256]) # when we do this, we add circle 256 and rectangle 256, the output will be [256 0 256] -->
# the reason the output is like this is 255,0,0 (circle) and 0,0,255 (rectangle) when creating circle and rectangle. -->
# circle 255 and rectangle 0 add up to 255, circle 0 and retangle 0 add up to 0, circle 0 and rectangle 255 add up to 255

cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Add", add)

cv2.waitKey(0)
cv2.destroyAllWindows()