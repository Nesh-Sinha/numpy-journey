import numpy as np
import time
start = time.time()
''' Creating Array From List'''

arr_1d = np.array([1,2,3,4,5])
print("1D array :" , arr_1d)

arr_2d = ([1,2,3],[4,5,6])
print("2D array :" , arr_2d)

''' NUMPY VS List'''

py_list = [1,2,3]
print("python list multiplication " , py_list * 2 ,"\n time taken :" ,time.time()-start)

py_array = np.array([1,2,3,4]) # element wise multiplication
print("Numpy Array  multiplication " , py_array * 2,"\n time taken :" ,time.time()-start)

# python list multiplication  [1, 2, 3, 1, 2, 3]
# time taken : 0.0014786720275878906

# Numpy Array  multiplication  [2 4 6 8]
# time taken : 0.002488374710083008




''' Creating array from scratch'''

zeros = np.zeros((3,4))
print("zeroes array : \n", zeros)
# zeroes array : 
#  [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

ones = np.ones((3,4))
print("ones array : \n", ones)
# ones array :
#  [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

full = np.full((2,2),7) #gives a complete matrix of a constant value
print("full array : \n", full)
# full array :
#  [[7 7]
#  [7 7]]

random = np.random.random([2,3]) # gives random matrix in dimnsion
print(random)

sequence =np.arange(0,10,1) #gives array in sequence
print(sequence)


''' VECTOR , MATRIX & TENSOR'''

vector = np.array([1,2,3,4,5,6])
print("vector :" , vector) 
# vector : [1 2 3 4 5 6]

matrix = np.array([[1,2,3,4],
                  [5,6,7,8]])
print("matrix : ", matrix)
# matrix :  [[1 2 3 4]
#            [5 6 7 8]]


tensor = np.array([[[1,2], [2,3]],
                   [[5,6], [7,8]]])
print("tensor :" ,tensor)

# tensor : [[[1 2]
#            [2 3]]

#           [[5 6]
#            [7 8]]]







''' Array Properties'''

arr= np.array([[1,2,3],
               [4,5,6]])

print("Shape :",arr.shape)
print("Size :",arr.size)
print("Dimension :",arr.ndim)
print("DType :",arr.dtype)

# Shape : (2, 3)
# Size : 6
# Dimension : 2
# DType : int64


''' Array Reshaping'''

array = np.arange(12)
print("Original array :", array)
#Original array : [ 0  1  2  3  4  5  6  7  8  9 10 11]

reshaped = array.reshape((3,4))
print("reshaped array :\n", reshaped)
# reshaped array :
#  [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

flattened = reshaped.flatten()
print("reshaped array :", flattened)
# reshaped array : [ 0  1  2  3  4  5  6  7  8  9 10 11]
print("reshaped array :\n", reshaped)
# retuns a copy , Changes to the flattened array won't affect the original array.

raveled = reshaped.ravel() 
print("ravel array :", raveled)
# array : [ 0  1  2  3  4  5  6  7  8  9 10 11]
print("reshaped array :\n", reshaped)
# ravel returns view insted of copy , hanges to the raveled array may affect the original array



# Transpose
transpose = reshaped.T
print("original :", reshaped)
print("transposed :", transpose)

# original : 
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# transposed : 
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]