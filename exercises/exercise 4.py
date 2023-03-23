import numpy as np
import matplotlib.pyplot as plt

path = 'C:\PycharmProjects\Opencv\(A)listirmalar\(A)listirmalar3.jpeg'
img = plt.imread(path)


"""
[r,g,b] burada anlatılmak istenen pikseller
[50,50,0] bunları liste halide yazdık çünkü hepsi bir değere karşılık geliyor yani 50 ye 50 pikselinde red pikseline ulaştık 
[70,70,1] bu da aynı şekilde 70 e 70 de green değerleri almak istedik
[:,:,2] # bunda da tüm değerlerdeki mavi değerlri aldık mavi olma sebebi 2 çünkü 0,1,2 de r,g,b de 2 b ye karşılık gelir o da blue
r -> 0-255
g -> 0-255
b -> 0-255 
"""


r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]


output = np.dstack((r,g,b)) # here it will stack all images one below the other and find the original image

plt.imshow(output)
plt.show()

output = [img,r,g,b]
titles = ["Image","Red","Green","Blue"] # 4 windows will appear, these are their names respectively


for i in range(4):
    plt.subplot(2,2,i+1)
    # this function means sub-graphs, we enter how many rows and columns will be in it first. With i+1, we tell where the graphics will be placed one by one.
    plt.axis("off") # turned off axes
    plt.title(titles[i]) #The purpose of this is to navigate through the titles and write the window steps each time, respectively, and create the plt.title window name.
    if i ==0:
        plt.imshow(output[i]) # the purpose of this is if i = 0 then Image will be displayed
    else:# if not, i will navigate by itself and the windows will appear in order.
        plt.imshow(output[i],cmap='gray')  # turn gray around here if that doesn't happen the pictures come out in very different colors
    plt.show()