import numpy as np
import pandas as pd

ic_sales = pd.read_csv('icecreamsales.csv').to_numpy()
# Array 1 - 5
sarr_1 = np.arange(1, 6)
np.mean(sarr_1)
np.median(sarr_1)
np.average(sarr_1)
np.std([4, 6, 3, 5, 2]) # Standard Deviation
np.var([4, 6, 3, 5, 2]) # Variance
# Also nanmedian, nanmean, nanstd, nanvar

print("ic_sales\n", ic_sales)
# Get the 50th percentile of the data
np.percentile(ic_sales, 50, axis=0)
# Get 1st column
ic_sales[:,0]

# Correlation coefficient : Measure of correlation between data
# Closer to 1 the more the data is correlated
np.corrcoef(ic_sales[:,0], ic_sales[:,1])

# Calculating Regression line
# Σ(x-x̅)*(y-ȳ) / Σ(x-x̅)2
temp_mean = np.mean(ic_sales[:,0])
sales_mean = np.mean(ic_sales[:,1])
numerator = np.sum(((ic_sales[:,0] - temp_mean)*(ic_sales[:,1] - sales_mean)))
denominator = np.sum(np.square(ic_sales[:,0] - temp_mean))
slope = numerator/denominator
# Calculate y intercept
y_i = sales_mean - slope * temp_mean
y_i
reg_arr = ic_sales[:,0] * slope + y_i
reg_arr