# bgr-rgb-grayscale

import cv2
import matplotlib.pyplot as plt

path = "C:\PycharmProjects\Opencv\(A)listirmalar\(A)listirmalar1.jpg"
img = cv2.imread(path,1) # Reads in BGR format cv2 always reads 1, normal reads 0, grayscale

#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # causing this mess

plt.imshow(img) # will be in rgb format
plt.imshow(img,cmap='gray',interpolation = 'BICUBIC')
# RGB means cmap color map means gray, it is written as interpolation format and fixes the disorder
plt.show()