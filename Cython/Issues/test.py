from time import time

from issues import cython_sum,cython_do_nothing

def do_nothing():
    pass

def timeit(title, function, args=None):
    start = time()

    for i in range(1_000):
        if not args:
            out = function()
        else:
            out = function(args)
    elapsed = (time() - start) / 1_000
    print(f"Time per call, {title}: {elapsed * 1000:.2} ms")


l = list(range(1000000))

timeit("do_nothing",do_nothing)
timeit("cython_do_nothing",cython_do_nothing)
timeit("build in sum",sum, args=l)
timeit("cython_sum",cython_sum, args=l)
