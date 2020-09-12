
# Import arrays from numeric python library
import numpy as np
# Create a numpy array
my_array = np.array([[1,2],[3,4]])
# Make the array `my_array` with specific data type
my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
# Display array
print(my_array)
#The shape indicates the shape of the array, and
print(my_array.shape)
#The data type or dtype pointer describes the kind of elements that are contained within the array,
print(my_array.dtype)

# Print the length of `my_array`
print(len(my_array))

# Change the data type of `my_array`
my_array.astype(float)

# Select items at row 0 and 1, column 1
print(my_array[0:2,1])

# Select items at index 0 and 1
#print(my_array[0:2])

# Specify a condition
#bigger_than_3 = (my_3d_array >= 3)

#The data pointer (If you want to poke inside C internals) indicates the memory address of the first byte in the array,
#print(my_array.data)
#The strides (If you want to poke inside C internals)  are the number of bytes that should be skipped in memory to go to the next element. If your strides are (10,1), you need to proceed one byte to get to the next column and 10 bytes to locate the next row.
#print(my_array.strides)

