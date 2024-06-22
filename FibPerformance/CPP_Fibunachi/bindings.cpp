#include <pybind11/pybind11.h>
#include "fib.hpp"

namespace py = pybind11;

PYBIND11_MODULE(fibonacci, m) {
    m.doc() = "Fibonacci module implemented in C++";
    m.def("fib", &fibonacci, "A function that calculates Fibonacci numbers");
}