import numpy as np

list_1 = [1,2,3,4,5]

# Create NumPy 1 dimensional (a axis) array list object of type byte (-128 to 127)
# A N-dimensional array is a usually fixed size multidimensional
# array that contains items of the same type.

np_arr_1 = np.array(list_1, dtype=np.int8)

m_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create NumPy multidimensional (2 axis) array without defining type

np_m_arr_1 = np.array(m_list_1)


# Reshape array to 1 by 9
np_m_arr_1.reshape((1, 9))
np_m_arr_1
# Reshape array to 2 by 5 (Items are either lost or 0s added)
resize = np_m_arr_1.resize((2,5))
print(resize)
# Transpose axes
transpose = np_m_arr_1.transpose()
print(transpose)
# Swap axes 
swapaxes = np_m_arr_1.swapaxes(0,1)
# Flatten in order
np_m_arr_1.flatten()
# Flatten in column order
np_m_arr_1.flatten('F')
# Sort rows
np_m_arr_1.sort(axis=1)

# Sort columns
np_m_arr_1.sort(axis=0)

print(np_m_arr_1)