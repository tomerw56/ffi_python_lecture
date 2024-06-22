from time import time
import numpy as np
import sys
import simd_example




def timeit(title,function, arr1, arr2):
    start = time()
    for i in range(1_000):
        out = function(arr1, arr2)
    elapsed = (time() - start) / 1_000
    print(f"Time per call, {title}: {elapsed * 1000:.2} ms")


# Arrays laid out linearly in memory:
ARR1 = np.random.random((1_000_000,)).astype(np.float32)
ARR2 = np.random.random((1_000_000,)).astype(np.float32)
timeit("average_arrays_1",simd_example.average_arrays_1,ARR1,ARR2)
timeit("average_arrays_2",simd_example.average_arrays_2,ARR1,ARR2)
timeit("average_arrays_3",simd_example.average_arrays_3,ARR1,ARR2)