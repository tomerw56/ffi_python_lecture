import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./libmultiply.so')  # Use 'libmultiply.dll' on Windows

# Define the argument and return types for the C function
lib.multiply_by_two.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
lib.multiply_by_two.restype = None

# Create a NumPy array
array = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)

# Call the C function
lib.multiply_by_two(array.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), len(array))

# Print the modified array
print(array)
