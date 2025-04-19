import numpy as np
import matplotlib.pyplot as plt

''' Advanced Operations with Basic examples'''

# Data Structure : [restaurant_id, 2021, 2022, 2023, 2024]

sales_data = np.array([
    [1, 3200, 3500, 3700, 3900],  # Domino's
    [2, 3000, 3100, 3300, 3400],  # Pizza Hut
    [3, 4100, 4300, 4500, 4700],  # McDonald's
    [4, 2900, 3000, 3200, 3300],  # KFC
    [5, 2200, 2400, 2600, 2800],  # Burger King
])

print("==== Zomato Sales Analysis ====")
print("\n sales data shape " , sales_data.shape)
# sales data shape  (5, 5)

# printing sample data for 1st 3 restrarant---------
print("sample data for 1st 3 restrarant :\n",  sales_data[:3]) #(0:3)
# sample data for 1st 3 restrarant :
#  [[   1 3200 3500 3700 3900]
#   [   2 3000 3100 3300 3400]
#   [   3 4100 4300 4500 4700]]

print("\n entire data without ids :\n", sales_data[:,1:]) #[row,column] 
#row -> : is requesting entir data 
#Column -> 1 id defining the starting range and : is gathering starting from range 1

#  entire data without ids :
#  [[3200 3500 3700 3900]
#  [3000 3100 3300 3400]
#  [4100 4300 4500 4700]
#  [2900 3000 3200 3300]
#  [2200 2400 2600 2800]]


''' ---Total sale per year---'''

yearly_total = np.sum(sales_data[:,1:],axis=0)
print(yearly_total) # top to bottom
# [15400 16300 17300 18100]

print(np.sum(sales_data[1:,:],axis=1)) #left to right
# [12802 17603 12404 10005]

print("entire sales : ",np.sum(yearly_total[:]))
#entire sales :  67100

print(sum(yearly_total))  #without numpy
# 67100




'''---Minimum and Max Sales Per Restraurant---'''

min_sale = np.min(sales_data[:,1:],axis=1)
print(min_sale)
# [3200 3000 4100 2900 2200]

print("max sales among all : ",np.max(sales_data[:,1:]))
# max sales among all :  4700

''' --------Average sales per restraurant--------- '''

avg_sales = np.mean(sales_data[:, 1:], axis = 1)
print("average sales : ",avg_sales)
# average sales :  [3575. 3200. 4400. 3100. 2500.]



''' ----- Cumelative sales ---------- '''

cumsum = np.cumsum(sales_data[: , 1:], axis = 1)
print("cumulative sum : " , cumsum)
# cumulative sum :  [[ 3200  6700 10400 14300] -> a a+b a+b+c a+b+c+d
#                    [ 3000  6100  9400 12800]
#                    [ 4100  8400 12900 17600]
#                    [ 2900  5900  9100 12400]
#                    [ 2200  4600  7200 10000]]

plt.figure(figsize=(8,6))
plt.plot(np.mean(cumsum,axis=0))
plt.title("Average cumulative sales accross all restraurant ")
plt.xlabel("years")
plt.ylabel("sales")
plt.grid(True)
plt.show()



''' ------ Vectors --------'''

vector1 = np.array([1,2,3,4,5,6])
vector2 = np.array([7,8,9,10,11,12])

print("Vector addition : ",vector1 + vector2 )
# Vector addition :  [ 8 10 12 14 16 18]

print("Vector multiplication : ",vector1 * vector2 )
# Vector multiplication :  [ 7 16 27 40 55 72]

print("Dot Product : ",np.dot(vector1 ,vector2 ))
# Dot Product :  217

angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1)*np.linalg.norm(vector2)))
print("angle : ",angle )
# angle :  0.27609007144367437


''' ---- Vectorized operation ---- '''

restraurant_type = np.array(['biscuit','cookies','cake','bread','brownie'])
vectorized_upper = np.vectorize(str.upper)
print("vectorized upper : ",vectorized_upper(restraurant_type))
# vectorized upper :  ['BISCUIT' 'COOKIES' 'CAKE' 'BREAD' 'BROWNIE']



'''---- BroadCast----'''

monthly_average = sales_data[:,1:] / 12
print(monthly_average)
# 12 will be divided with each and every value , that's broadcasting

# [[266.66666667 291.66666667 308.33333333 325.        ] 
#  [250.         258.33333333 275.         283.33333333] 
#  [341.66666667 358.33333333 375.         391.66666667] 
#  [241.66666667 250.         266.66666667 275.        ] 
#  [183.33333333 200.         216.66666667 233.33333333]]