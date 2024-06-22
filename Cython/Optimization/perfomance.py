import random
from time import time
import solution_regular as regular
import solution_cython as cython
import solution_cython_numpy as cython_numpy
import numpy as np
def time_function(title, function, **kwargs):
    start = time()
    for i in range(1_000):
        function(**kwargs)
    elapsed = (time() - start) / 1_000
    print(f"Time per call, {title}: {elapsed * 1000:.2} ms")


depths = random.sample(range(10, 300000), 1000)
time_function("regular",regular.count_increases,depths=depths)
time_function("cython",cython.count_increases,depths=depths)
numpy_depths=np.array(depths).astype("int32")
time_function("solution_cython_numpy",cython_numpy.count_increases_cy_array,depths=numpy_depths)