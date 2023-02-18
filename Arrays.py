import numpy as np

# Provides beautiful plots of numerous type that are either
# static, animated and/or interactive

import matplotlib.pylab as plt
from numpy import random

# A python list 
list_1 = [1,2,3,4,5]

# Create NumPy 1 dimensional (a axis) array list object of type byte (-128 to 127)
# A N-dimensional array is a usyally fixed size multidimensional
# array that contains items of the same type.

np_arr_1 = np.array(list_1, dtype=np.int8)

# Create multidimenional list

m_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create NumPy multidimensional (2 axis) array without defining type

np_m_arr_1 = np.array(m_list_1)

# You can also create arrays by defining the start value,
# stop value (up to but not include stop) and step amount
np.arange(1, 10)

# With floats define start, end and number of values
np.linspace(0, 5, 7)

# You can create a 3 item array of zeroes
np.zeros(4)

# You can create multidimensional arrays of zeroes by passing
# a tuple with the 1st value being rows and the 2nd columns
np.zeros((2, 3))

# Create array of 1s
np.ones((2, 3))

# Get number of items in the array
np_m_arr_1.size

# Create array with defined values
np_arr_2 = np.array([1, 2, 3, 4, 5, 6])

# Data Types
# Boolean : np.bool_
# Char : np.byte
# Short : np.short
# Integer : np.short
# Long : np.int_
# Float : np.single & np.float32
# Double : np.double & np.float64
# np.int8 : -128 to 127
# np.int16 : -32768 to 32767
# np.int32 : -2147483648 to 2147483647
# np.int64 : -9223372036854775808 to 9223372036854775807

# Create random 5 value 1D array from 10 to 50
random = np.random.randint(10, 50, 5)
# Create random matrix 2x3 with values between 10 and 50
np.random.randint(10, 50, size=(2, 3))

# Get help with a function
np.random.randint

print(random)

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