import cv2

img = cv2.imread("indir.jfif")# allows us to read the mathematical values of the pictures imread
#print(img) # we read the image at this stage
###############

cv2.namedWindow("image", cv2.WINDOW_NORMAL)# This allows us to play with the picture when it comes out
cv2.imshow("image", img)
cv2.imwrite("indir1.jfif", img) # only this part allows us to save the picture
cv2.waitKey(0) # When we type 0, it stays on the screen until we turn it off. The waitkey allows us to see the image on the screen.
cv2.destroyAllWindows() # the purpose of this is when we close the picture one line above, something may remain open in the back, this will cause us trouble, we close all the windows to avoid problems
# this was operations like showing the pictures we did above

