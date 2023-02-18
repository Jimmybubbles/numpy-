import numpy as np

list_1 = [1,2,3,4,5]

# Create NumPy 1 dimensional (a axis) array list object of type byte (-128 to 127)
# A N-dimensional array is a usually fixed size multidimensional
# array that contains items of the same type.

np_arr_1 = np.array(list_1, dtype=np.int8)

m_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create NumPy multidimensional (2 axis) array without defining type

np_m_arr_1 = np.array(m_list_1)
# Generate random arrays
ss_arr_1 = np.random.randint(10, size=(2, 2))
print("ss_arr_1\n", ss_arr_1)
ss_arr_2 = np.random.randint(10, size=(2, 2))
print("ss_arr_2\n", ss_arr_2)

# Stack arr_2 under arr_1
np.vstack((ss_arr_1, ss_arr_2))
# Stack horizontally
np.hstack((ss_arr_1, ss_arr_2))

# Delete 2nd row on each array
ss_arr_3 = np.delete(ss_arr_1, 1, 0)
ss_arr_4 = np.delete(ss_arr_2, 1, 0)
print("ss_arr_3\n", ss_arr_3)
print("ss_arr_4\n", ss_arr_4)
# Combine arrays
np.column_stack((ss_arr_3, ss_arr_4))
# Stack in a 2D array
np.row_stack((ss_arr_3, ss_arr_4))

# Generate 2x10 array
ss_arr_5 = np.random.randint(10, size=(2, 10))
print("ss_arr_5\n", ss_arr_5)
# Split into 5 arrays taking from both arrays in multidimensional array
np.hsplit(ss_arr_5, 5)
# Split after 2nd & 4th column
np.hsplit(ss_arr_5, (2, 4))