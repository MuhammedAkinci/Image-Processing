import numpy as np

# one-dimensional arrays
'''
x = np.array([1,2,3], np.int16) # range of np.int16
print(x)
print(type(x))
'''

# MULTI-DIMENSIONAL ARRANGEMENTS

# 2 dimensional arrays
'''
x = np.array([[1, 2, 3], [4, 5, 6]], np.int16)
print(x)
print(type(x))
print(x[:,0]);print(x[:,1]);print(x[:,2])
'''

# 3D Arrays

'''
x = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]],np.int16)
print(x)
print("////")
print(x[0,0,0])
print("////")
print(x[0,1,0])
print("////")
print(x[1,1,1])
'''

# NUMPY NDARRAY
# ndarray --> n-dimensional array

'''
x = np.array([[-2,-1,0,5],[9,4,5,-7],[9,7,6,5]],np.int16) # unsigned int

print(x)
print(x.shape)
print(x.ndim)
print(x.dtype)
print(x.size)
print(x.T)
'''
# NUMPY ONES AND ZEROS --> ONES and ZEROS

x = np.empty([3,3],np.uint8) #np.empty means creating an empty array when we run it, it has numbers in it but it's random
print("x: ",x)
print("-------")

y = np.full((3,3,3),dtype=np.int16,fill_value=10)
# here we have created an array with 3 rows, 3 columns and 3 depth and it's a shame what number we want to enter with fill_valueprint("y: ",y)
print("-------")

z = np.ones((2,5,5),dtype=np.int8) # here we have created an array of 2 rows, 2 columns, 5 depths, which we call np.ones, which is filled with the number 1.
print("z: ",z) # A set of 1s represents the white screen in image processing

j = np.zeros((2,3,3),dtype=np.int8) # here we have created an array of 2 rows, 3 columns and 3 depths, which we call np.zeros, which is filled with the number 0
print("j: ",j) # represents a rendering black screen with a set of zeros