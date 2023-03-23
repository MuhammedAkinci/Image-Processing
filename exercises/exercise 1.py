import numpy as np
import matplotlib.pyplot as plt

path = 'C:\PycharmProjects\Opencv\(A)listirmalar\(A)listirmalar1.jpg'
img = plt.imread(path)
print(img)
print("min value: ",img.min()) # smallest pixel value
print("max value: ", img.max()) # largest pixel value
print("mean: ", img.mean()) # mean calculates the average of the colors
print("median: ",np.median(img)) # found the median
print("average: ",np.average(img)) # calculate the average here too
print("mean1: ",np.mean(img)) # it's the same mean but different spelling but they work the same way
