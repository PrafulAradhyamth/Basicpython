# Import `numpy` as `np`
import numpy as np
import matplotlib.pyplot as plt

# Initialize your array
my_3d_array = np.array([[[1,2,3,4], [5,6,7,8]], [[1,2,3,4], [9,10,11,12]]], dtype=np.int64)

# Pass the array to `np.histogram()`
# Specify the number of bins
print(np.histogram(my_3d_array, bins=range(0,13)))

# Construct the histogram with a flattened 3d array and a range of bins
plt.hist(my_3d_array.ravel(), bins=range(0,13))

# Add a title to the plot
plt.title('Frequency of My 3D Array Elements')

# Show the plot
plt.show()
