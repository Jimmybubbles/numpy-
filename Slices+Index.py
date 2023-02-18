import numpy as np

list_1 = [1,2,3,4,5]

# Create NumPy 1 dimensional (a axis) array list object of type byte (-128 to 127)
# A N-dimensional array is a usually fixed size multidimensional
# array that contains items of the same type.

np_arr_1 = np.array(list_1, dtype=np.int8)

m_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create NumPy multidimensional (2 axis) array without defining type

np_m_arr_1 = np.array(m_list_1)

# Change value at index
# np_m_arr_1[0,0] = 2
# np_m_arr_1.itemset((0,1), 1)
np_m_arr_1
# Get size of array
np_m_arr_1.shape
# Get value by index
np_m_arr_1[0,1]
np_m_arr_1.item(0,1)

# Get specific indices
np.take(np_m_arr_1, [0, 3, 6])
# Replace provided index values with new values
np.put(np_m_arr_1, [0, 3, 6], [10, 10, 10])
print(np_m_arr_1)

# Start at 1st through 5th with 2 step
np_arr_1[:5:2]
# Get 2nd value from each row
np_m_arr_1[:,1]
# Flip Array
np_arr_1[::-1]

# Get evens
evens = np_m_arr_1[np_m_arr_1%2==0]
evens

# Get values > 5
np_m_arr_1[np_m_arr_1 > 5]
# 5 < value < 9
np_m_arr_1[(np_m_arr_1 > 5) & (np_m_arr_1 < 9)]
# 5 < value or value = 10
np_m_arr_1[(np_m_arr_1 > 5) | (np_m_arr_1 == 10)]

# Find uniques
np.unique(np_m_arr_1)

print(evens)