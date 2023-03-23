# matplotlib is actually a data visualization library
import matplotlib.pyplot as plt# plt here can change we can write whatever we want
import numpy as np # np here can change, we can write whatever we want


'''
x = np.arange(5) # Define an x in the range 5
y = x

print(x)
plt.plot(x,y,"o--") # o, o-, o-- here if there were only x and y it would have drawn a straight line but he continued dot by point because we did it
plt.plot(x,-y)
plt.plot(-x,y,"o")
plt.title("y=x, y=-x") # this creates the area of our graph
plt.show()
'''

# The shapes we have drawn in the chart may vary according to the data we have given, it is up to us.
# in general we use plot to graph data and show to show

'''
N = 10
x = np.linspace(0, 10, N) # linspace purpose is to generate data for us in the range we entered


y = x

plt.plot(x,y,"o--")
plt.axis("off") # this axis purpose makes only our line appear when the table is output
plt.show()


x = [1,2,3,4] # here we create the list ourselves and draw a graph according to the list we created
plt.plot(x,[y**2 for y in x])# we go into x let y loop through x and square each number
plt.show()
'''



'''
x = np.arange(3)# wrote the numbers from 0 to 3


plt.plot(x,[y**2 for y in x]) # Let y walk through x and square each number

plt.plot(x,[y**3 for y in x])# Let y go through x and cube each number

plt.plot(x,2*x) # every x value is doubled

plt.plot(x, 5.2*x) # let each value of x be a multiple of 5.2


plt.legend(['x**2','x**3','x*2','x*5.2'],loc='lower right')
# we wrote what it should show and the last one is where we want to show the things we want to show
# this function will tell you what drawings we made
# upper right/center/left, lower right/center/left

plt.grid(True) # thanks to this we create a grid i.e. the small square forming lines on the graphic background
plt.xlabel('x = np.arange(3)') # thanks to this we named the xs
plt.ylabel('y = f(x)'# here we name the y's
plt.axis([0,2,0,10]) # here we enter the max and min values of the x axis we want to see with axis first, then we enter the max and min values of y
plt.title("Simple Plot") # here we type the name of the chart
plt.savefig("C:\PycharmProjects\Opencv\(n)umpy_and_matplotlib\matplotlib.png") # the purpose of this is to record what we do
plt.show()
'''
'''

path = "C:\PycharmProjects\Opencv\(n)umpy_and_matplotlib\matplotlib1.jpg"
img = plt.imread(path)# we did the image display process with plt this time

plt.imshow(img)
plt.show()

print(img);print("type: ",type(img));print("shape: ",img.shape);print("ndim: ",img.ndim);print("size: ",img.size);print("dtype:", img.dtype)
# first we wrote img, then we wrote its type, then we split it (shape), then we learned ndim, then we learned its height, last data type uint8 mi or something

print("red channel: ",img[50,50,0]) # 50 ye 50 deki kırmızı değerleri aldık,  rgb--> r =0, g=1, b=2
print("green channel: ",img[50,50,1]) # we did the same operations as above
print("blue channel: ",img[50,50,2])
print("rgb channel value: ",img[50,50,:]) # trailing 2 dots to get all values
'''
