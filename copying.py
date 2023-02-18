import numpy as np

list_1 = [1,2,3,4,5]

# Create NumPy 1 dimensional (a axis) array list object of type byte (-128 to 127)
# A N-dimensional array is a usually fixed size multidimensional
# array that contains items of the same type.

np_arr_1 = np.array(list_1, dtype=np.int8)

m_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create NumPy multidimensional (2 axis) array without defining type

cp_arr_1 = np.random.randint(10, size=(2, 2))
# Both variables point at the same array
cp_arr_2 = cp_arr_1
# Change value
cp_arr_1[0,0] = 2
print("cp_arr_1\n", cp_arr_1)
print("cp_arr_2\n", cp_arr_2)
# Create a view of data where changes don't effect original
cp_arr_3 = cp_arr_1.view()
print("cp_arr_3\n", cp_arr_3)
cp_arr_3 = cp_arr_3.flatten('F')
print("cp_arr_3\n", cp_arr_3)
print("cp_arr_1\n", cp_arr_1)
# Copy and create new array
cp_arr_4 = cp_arr_1.copy()