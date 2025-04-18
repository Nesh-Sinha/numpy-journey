import numpy as np


''' Indexing & Slicing'''

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print("basic slicing :", arr[2:7])
# basic slicing : [3 4 5 6 7]

print("with step :", arr[2:9:3]) # slice(from,till,step)
# with step : [3 6 9]

print("Negative indexing:", arr[-3])
# Negative indexing: 8


''' Indexing 2D Array'''

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print("specific element :" , arr_2d[1,2]) #array[row,column]
# specific element : 6

print("entire row :",arr_2d[2]) 
# entire row : [7 8 9]

print("entire column :",arr_2d[:,1]) # by using ' : ' in the place of row we mean that we want the whole row
# entire column : [2 5 8]



'''  Sorting '''

unsorted = np.array([4,6,4,4,3,8,7,7,6,5,6,7,8,9])

print("sorted array :", np.sort(unsorted))
# sorted array : [3 4 4 4 5 6 6 6 7 7 7 8 8 9]


'''Sorting 2D Array'''

arr_2d_unsorted = np.array([[3,1],[1,2],[2,3]])

print(" Sorted 2D Array by Row : \n", np.sort(arr_2d_unsorted,axis=0))
# Sorted 2D Array by Row : done by axis = 0
#  [[1 1]
#   [2 2]      top - bottom
#   [3 3]]

print(" Sorted 2D Array by column : \n", np.sort(arr_2d_unsorted,axis=1))
# Sorted 2D Array by Column : done by axis = 1
# [[1 3]    
#  [1 2]      left - right
#  [2 3]]

''' Filtering'''

numbers =np.array([1,2,3,4,5,6,7,8,9,10])
even_number = numbers[numbers % 2 == 0]
print("even number :",even_number)
# even number : [ 2  4  6  8 10]
# numpy allow us to use expression inside array

''' Filter With Mask'''

mask = numbers > 5
print("numbers greater than 5 :", numbers[mask])
# numbers greater than 5 : [ 6  7  8  9 10]
# the variable can store the expression in numpy



''' Fancy Indexing vs np.where() '''
num = np.array([1,2,3,4,5,6,7])
indices = [0,2,4]
print(num[indices])
# [1 3 5] 

where_result =np.where(numbers > 5) 
print("np where", numbers[where_result])
# np where [ 6  7  8  9 10]
# np.where() works like mask but with a condition or expression 

condition_array = np.where(num > 5, num*2,num)
print(condition_array)
# [ 1  2  3  4  5 12 14]
#(main condition , value of x , value of y)
#(condition, if true , else)

''' Adding and Removing data'''

num1 = np.array([1,2,3])
num2 = np.array([4,5,6])
combine = num1 + num2
print(combine)
# [5 7 9]

combined = np.concatenate([num1 , num2])
print(combined)
#[1 2 3 4 5 6]



''' Array Compatibility'''

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])

print("Compatibility Shapes :" , a.shape == b.shape == c.shape)
# Compatibility Shapes : True



''' Adding Row & Column'''

original = np.array([[1,2],[3,4]])
new_row = np.array([[5,6]])

with_new_row = np.vstack((original,new_row)) 
# vstack() means virtical stack
#((old, new )) tuple of data

print("Original : ",original)
#Original :  [[1 2]
#             [3 4]]

print("Added : ",with_new_row)
# Added :  [[1 2]
#           [3 4]
#           [5 6]]

new_column = np.array([[7],[8],[9]])
with_new_column = np.hstack((with_new_row,new_column))
print(with_new_column)
# [[1 2 7]
#  [3 4 8]
#  [5 6 9]]


''' Delete'''

arr = np.array([2,3,4,5,6,7,7,8])
delete = np.delete(arr ,2)
print("array after delete :", delete)
# array after delete : [2 3 5 6 7 7 8]