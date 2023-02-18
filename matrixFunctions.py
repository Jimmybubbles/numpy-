import numpy as np
from numpy import linalg as LA


print("arr_5\n", arr_5)
print("arr_6\n", arr_6)
arr_8 = np.array([[5, 6], [7, 8]])

# Matrix multiplication with Dot Product
# (1 * 2) + (2 * 6) = 14 [0,0]
# (1 * 4) + (2 * 9) = 22 [0,1]
# (3 * 2) + (4 * 6) = 30 [1,0]
# (3 * 4) + (4 * 9) = 12 + 36 = 48 [1,1]
np.dot(arr_5, arr_6)
# Compute dot product of 2 or more arrays
LA.multi_dot([arr_5, arr_6, arr_8])

# Inner product 
# (1 * 2) + (2 * 4) = 10 [0,0]
# (1 * 6) + (2 * 9) = 24 [0,1]
# (3 * 2) + (4 * 4) = 22 [1,0]
# (3 * 6) + (4 * 9) = 54 [1,1]
np.inner(arr_5, arr_6)
np.dot(arr_5, arr_6)

# Tensor Dot Product
# (1 * 1) + (2 * 2) + (3 * 3) + (4 * 4) = 30
# (5 * 1) + (6 * 2) + (7 * 3) + (8 * 4) = 
arr_9 = np.array([[[1, 2],
        [3, 4]],
       [[5, 6],
        [7, 8]]])
arr_10 = np.array([[1, 2],
       [3, 4]], dtype=object)
np.tensordot(arr_9, arr_10)

# Einstein Summation : Provides many ways to perform
# operations on multiple arrays
arr_11 = np.array([0, 1])
arr_12 = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
# Left Side of -> : 1 axis for arr_11 and 2 axis for arr_12
# Right of -> : Array we want (1D Array)
# ij : Means multiply arr_11 single item by each column of arr_12 and sum
# [0, 4 + 5 + 6 + 7]
np.einsum('i,ij->i', arr_11, arr_12)
# Sum values in arr_11
np.einsum('i->', arr_11)
# Dot Product
print("arr_3\n", arr_3)
print("arr_4\n", arr_4)
np.einsum('i,i->', arr_3, arr_4)
# Matrix multiplication
np.einsum('ij,jk', arr_5, arr_6)
# Get diagonal
np.einsum('ii', arr_5)
# Transpose
np.einsum('ji', arr_5)

# Raise matrix to the power of n
# Given [[a, b], [c, d]]
# [[a² + bc, ab +db], [ac + dc, d² + bc]
LA.matrix_power(arr_5, 2)

# Kronecker product of 2 arrays
# Given [[a, b], [c, d]], [[e, f], [g, h]]
# [[a*e, a*f, b*e, b*f], [a*g, a*h, b*g, b*h], ...]
np.kron(arr_5, arr_6)

# Compute eigenvalues
LA.eig(arr_5) # Returns eigenvectors
LA.eigvals(arr_5)

# Get Vector Norm sqrt(sum(x**2))
LA.norm(arr_5)

# Get Multiplicative Inverse of a matrix
LA.inv(arr_5)

# Get Condition number of matrix
LA.cond(arr_5)

# Determinates are used to compute volume, area, to solve systems
# of equations and more. It is a way you can multiply values in a
# matrix to get 1 number.
# For a matrix to have an inverse its determinate must not equal 0
# det([[a, b], [c, d]]) = a*d - b*c
arr_12 = np.array([[1, 2], [3, 4]])
# 1*4 - 2*3 = -2
LA.det(arr_12)

# Determinate of 3x3 Matrix
# det([[a, b, c], [d, e, f], [g, h, i]]) = a*e*i - b*d*i + c*d*h
# - a*f*h + b*f*g - c*e*g

# When we multiply a matrix times its inverse we get the identity
# matrix [[1,0],[0,1]] for a 2x2 matrix
# Calculate the inverse 1/(a*d - b*c) * [[d, -b], [-c, a]]
# 1/(4 - 6) = -.5 -> [[-.5*4, -.5*-2], [-.5*-3, -.5*a]]
arr_12_i = LA.inv(arr_12)
arr_12_i

np.dot(arr_12, arr_12_i)

# Solving Systems of Linear Equations
# If you have 3x + 5 = 9x -> 5 = 6x -> x = 5/6
# If you have x + 4y = 10 & 6x + 18y = 42
# Isolate x -> x = 10 - 4y
# 6(10 - 4y) + 18y = 42 -> 60 - 24y + 18y = 42 - > -6y = -18 -> y = 3
# x + 4*3 = 10 -> x = -2
arr_13 = np.array([[1, 4], [6, 18]])
arr_14 = np.array([10, 42])
# Solve will solve this for you as well
LA.solve(arr_13, arr_14)

# Return a identity matrix with defined number of rows and columns
np.eye(2, 2, dtype=int)