import numpy as np
import time 
import sys


a = np.array([1, 2, 3]) #single dimensional array
print(a)

b = np.array([(1, 2, 3), (4, 5, 6)])#multi-dimentional array
print(b)

S = 100000

L1 = range(S)
L2 = range(S)
A1 = np.array(S)
A2 = np.array(S)

start = time.time()
result = [(x,y) for x,y in zip(L1, L2)]

print((time.time()-start)*1000)

start = time.time()
result = A1 + A2
print((time.time()-start)*1000)


#ndim=> to find the dimension of the array
c = np.array([(1, 2, 3), (4, 5, 6)])
print("dimension of the array is ", c.ndim)

#itemsize to calculate the byte size of each element
c = np.array([(1, 2, 3)])
print("size of each element of the array is ", c.itemsize)

#dtype to find the data type of the element that are stored in the array
c = np.array([(1, 2, 3)])
print("type of the array is ", c.dtype)
print("size of the array is ", c.size)
print("shape of the array is ", c.shape)

#reshape() is used to change the number of the row and columns
c = np.array([(1, 2, 3), (4, 5, 6)])
print("reshaped array is ", c.reshape(3, 2))

#this is how to slice the array
c = np.array([(1, 2, 3), (4, 5, 6)])
print(c[0, 2])

c = np.array([(1, 2, 3), (4, 5, 6)])
print(c[0:, 2])

c = np.array([(1, 2, 3), (4, 5, 6)])
print(c[0:2, 1:])


#linespace return an evenly spaced numbers over a specified interval
c = np.array([(1, 2, 3)])
print(np.linspace(1, 2, 10))# np.linspace(start, stop, size)

#min/max 
c = np.array([(1, 2, 3)])
print("maximum is ", c.max())
print("minimum is ", c.min())
print("sum is ", c.sum())

#sum
c = np.array([(1, 2, 3), (4, 5, 6)])
print("sum of the row is ", c.sum(axis=0)) # row is axis = 0 and columns is axis = 1
print("sum of the column is ", c.sum(axis=1))
