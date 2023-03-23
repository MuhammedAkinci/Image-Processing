import cv2
import numpy as np

def nothing():
    pass

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("image") # The reason we named the window is to place the trackbar interface in the colored part, that is, one line up.

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
# The first entered name, the other one is the name of the window, the other two are the start and end values, and the nothing function comes at the end there is no purpose trackbar works like this

switch = "0: OFF, 1: ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
# This is the purpose of doing r,g,b above, to keep the values while the colors are being formed, meaning that it can be r - 60, g - 30, b - 10
    s = cv2.getTrackbarPos(switch, "image") # What we store in the switch is the name of the sled, our purpose of making  ->
    # to make the switch work while playing with the values on the screen
    # so when the key is at 0, even if the sleds play, the color does not come, but if the key is switch 1, the colors come as the sleds play
    if s == 0:
        img[:] = [0,0,0]

    if s == 1:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
#cv2.waitKey(0)
