import numpy as np
import time
from numba import jit

def regular_sum_array(arr):
    total = 0.0
    for i in arr:
        total += i
    return total

# Create a large NumPy array
array = np.random.rand(10**7)

# Measure the time taken by the plain Python function
start_time = time.time()
total = regular_sum_array(array)
end_time = time.time()

print(f"Sum: {total}")
print(f"Time taken (plain Python): {end_time - start_time} seconds")

@jit(nopython=True)
def numba_sum_array(arr):
    total = 0.0
    for i in arr:
        total += i
    return total

# Measure the time taken by the Numba-optimized function
start_time = time.time()
total = numba_sum_array(array)
end_time = time.time()

print(f"Sum: {total}")
print(f"Time taken (Numba): {end_time - start_time} seconds")
