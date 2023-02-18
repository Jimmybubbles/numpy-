import numpy as np

# Generate array of 200 values between -pi & pi
t_arr = np.linspace(-np.pi, np.pi, 200)

# Plot with x axis & y axis data 
# plt.plot(t_arr, np.sin(t_arr)) # SIN
# plt.plot(t_arr, np.cos(t_arr)) # COS
# plt.plot(t_arr, np.tan(t_arr)) # TAN
# Display plot
# plt.show()

# Provides inverse of If y = cos(x), x = arccos(y)
np.arcsin(1)
np.arccos(1)
np.arctan(0)

# Also arctan2, sinh, cosh, tanh, arcsinh, arccosh, arctanh

# Radians to degrees
np.rad2deg(np.pi)
# Degrees to radians
np.deg2rad(180)

# Hypotenuse c = √w² + h²
np.hypot(10,10)