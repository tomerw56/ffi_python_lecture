import cython
def cython_sum(values):
    cdef long result = 0
    cdef long v
    for v in values:
        result += v
    return result
def cython_do_nothing():
    pass