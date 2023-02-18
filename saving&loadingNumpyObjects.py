import numpy as np

arr_15 = np.array([[1, 2], [3, 4]])
# Save as randarray.npy
np.save('randarray', arr_15)
# Load saved array 
arr_16 = np.load('randarray.npy')
arr_16

# Save as a CSV 
np.savetxt('randcsv.csv', arr_15)
# Load CSV
arr_17 = np.loadtxt('randcsv.csv')
arr_17