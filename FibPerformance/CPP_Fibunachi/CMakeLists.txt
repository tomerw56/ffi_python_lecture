# project specific information
cmake_minimum_required(VERSION 3.14)
project(fibunchi_cpp)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY bin)
add_library(fibunchi_cpp SHARED fib.cpp fib.hpp)

# Find pybind11
find_package(pybind11 REQUIRED)

# Create the shared library
add_library(fibonacci SHARED fib.hpp fib.cpp bindings.cpp)

# Link pybind11
target_link_libraries(fibonacci PRIVATE pybind11::module)


