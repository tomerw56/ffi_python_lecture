import ctypes
import time
import timeit
import numba

# Load the shared object file
lib = ctypes.CDLL('./libfibunchi_cpp.so')

# Define the argument and return types of the fib function
# Assuming the fib function takes an integer and returns an integer
lib.fibonacci.argtypes = [ctypes.c_int]
lib.fibonacci.restype = ctypes.c_longlong
number_of_loops = 100
value = 150


def _do_test(function, caption: str) -> float:
    start = time.process_time()
    for index in range(number_of_loops):
        function(value)
    total = time.process_time() - start

    print(f"{caption} version took {total}")




def cpp_fib(number: int) -> int:
    # Call the fib function

    return lib.fibonacci(number)




def python_fib(number: int) -> int:
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
    return current


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    _do_test(function=python_fib, caption="python")
    _do_test(function=cpp_fib, caption="ctype")
