# Pandas is used to manipulate tabular data and more
import pandas as pd
import numpy as np
# Import using NumPy
from numpy import genfromtxt

# Read table of data from CSV file and convert to Numpy array
ic_sales = pd.read_csv('icecreamsales.csv').to_numpy()
ic_sales

# Read data using NumPy
ic_sales_2 = genfromtxt('icecreamsales.csv', delimiter=',')
# Remove NANs
ic_sales_2 = [row[~np.isnan(row)] for row in ic_sales_2]
ic_sales_2

print(ic_sales)