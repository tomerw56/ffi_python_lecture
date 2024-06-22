import numba
import time
#timeit.timeit("fib_numba.python_fib_numba(150)",setup="import fib_numba")


@numba.jit(nopython=True)
def python_fib_numba(number: int, number_of_loops: int = 100) -> int:
     for index in range(number_of_loops):
        if number == 0:
            return 0
        if number == 1:
            return 1
        prevprev = 0
        prev = 1
        current = 1
        for _ in range(number - 1):
            current = prevprev + prev
            prevprev = prev
            prev = current
