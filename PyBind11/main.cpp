#include <pybind11/embed.h> // everything needed for embedding
namespace py = pybind11;

int main() {
    py::scoped_interpreter guard{}; // start the interpreter and keep it alive

    py::print("Hello, World!"); // use the Python API


    py::module_ calc = py::module_::import("calc");
    py::object result = calc.attr("add")(1, 2);
    int n = result.cast<int>();
    assert(n == 3);
}