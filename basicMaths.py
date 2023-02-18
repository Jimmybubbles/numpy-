import numpy as np
from numpy import random

arr_3 = np.array([1, 2, 3, 4])
arr_4 = np.array([2, 4, 6, 8])
# Add values
arr_3 + arr_4
# Subtract
arr_3 - arr_4
# Multiply
arr_3 * arr_4
# Divide
arr_3 / arr_4
# Random 4 digit 1D array between 0 to 100
arr_5 = random.randint(100, size=(4))
arr_5
# Random 2 by 3 digit 2D array between 0 to 100
arr_6 = random.randint(100, size=(2, 3))
arr_6
# 4 random floats
random.rand(4)
# Get random value from an array
random.choice(arr_3)

# Sum of values in array
arr_3.sum()
# Sum columns
print(arr_6)
arr_6.sum(axis=0)
# Cumulative sum of rows
arr_6.cumsum(axis=1)

# Min of each row
arr_6.min(axis=1)
# Max of each column
arr_6.max(axis=0)

print("arr_3", arr_3)
print("arr_4", arr_4)
# Add individual numbers to array
np.add(arr_3, 5)
# Add arrays
np.add(arr_3, arr_4)
# Subtract
np.subtract(arr_3, arr_4)
# Multiply
np.multiply(arr_3, arr_4)
# Divide
np.divide(arr_3, arr_4)

arr_5 = np.array([[1, 2], [3, 4]])
arr_6 = np.array([[2, 4], [6, 9]])
print("arr_5\n", arr_5)
print("arr_6\n", arr_6)
# Divides elements in 1st array by 2nd array and returns remainder
np.remainder(arr_6, arr_5)

# Return values in 1st array to powers defined in 2nd array
np.power(arr_6, arr_5)
# Square root
np.sqrt(arr_3)
# Cube root
np.cbrt(arr_3)
# Absolute value of every element
np.absolute([-1, -2])
# Exponential of all elements in array
np.exp(arr_3)
# log functions
np.log(arr_3)
np.log2(arr_3)
np.log10(arr_3)
# Greatest common divisor
np.gcd.reduce([9, 12, 15])
# Lowest common multiple
np.lcm.reduce([9, 12, 15])

# Round down
np.floor([1.2, 2.5])
# Round up
np.ceil([1.2, 2.5])

# Can receive 6 values and square them
sq_arr = np.arange(6)**2
sq_arr[arr_3]

arr_7 = random.randint(100, size=(5, 3))
print("arr_7\n", arr_7)
# Get index for max value per column
mc_index = arr_7.argmax(axis=0)
mc_index
# Get numbers corresponding to indexes
max_nums = arr_7[mc_index]
arr_7[mc_index, range(arr_7.shape[1])]