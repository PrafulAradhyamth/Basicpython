# Your data in the text file
# Value1  Value2  Value3
# 0.4839  0.4536  0.3561
# 0.1292  0.6875  MISSING
# 0.1781  0.3049  0.8928
# MISSING 0.5801  0.2038
# 0.5993  0.4357  0.7410
import numpy as np
my_array2 = np.genfromtxt('data2.txt',skip_header=1,filling_values=-999)
print my_array2