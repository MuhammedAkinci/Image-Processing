import cv2
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("C:\PycharmProjects\Opencv\(A)listirmalar\(A)listirmalar3.jpeg")
plt.subplot(4,2,1) # here we entered how much a graph we created and finally it is in the 1st place
plt.title("Original Image")
plt.imshow(img)
plt.subplot(4,2,2)
plt.title("img + img")
plt.imshow(img + img) # here we have collected two images on top of each other
plt.subplot(4,2,3)
plt.title("img - img")
plt.imshow(img - img) # black screen occurred because there is subtraction and subtraction of all values here
plt.subplot(4,2,4)
plt.title("np.flip(img,0)")
plt.imshow(np.flip(img,0)) # 0,1,2 we enter them if we want, they change their reflection 0 takes their reflection according to x
plt.subplot(4,2,5)
plt.title("np.flip(img,1)")
plt.imshow(np.flip(img,1)) # 1 gets it relative to the y-axis
plt.subplot(4,2,6)
plt.title("np.flip(img,2)")
plt.imshow(np.flip(img,2))  #2, the color values change, there is no reflection
plt.subplot(4,2,7)
plt.title("np.fliplr(img)") # means put left to right, right side and left side
plt.imshow(np.fliplr(img)) #received its reflection relative to the y-axis
plt.subplot(4,2,8)
plt.title("np.flipud(img)") # uptodown makes the picture upside down like flipud
plt.imshow(np.flipud(img)) # got its reflection relative to the x-axis
plt.show()