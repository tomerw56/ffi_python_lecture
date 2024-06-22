// main.cpp
#include <Python.h>
#include <iostream>

int main() {
    // Initialize the Python Interpreter
    Py_Initialize();

    // Define the name of the Python file (without the .py extension)
    PyObject* pName = PyUnicode_DecodeFSDefault("mymodule");

    // Import the Python file as a module
    PyObject* pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != nullptr) {
        // Get the function object from the module
        PyObject* pFunc = PyObject_GetAttrString(pModule, "add");

        if (pFunc && PyCallable_Check(pFunc)) {
            // Prepare the arguments to the function
            PyObject* pArgs = PyTuple_Pack(2, PyLong_FromLong(2), PyLong_FromLong(3));

            // Call the function
            PyObject* pValue = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);

            if (pValue != nullptr) {
                // Print the result
                std::cout << "Result of call: " << PyLong_AsLong(pValue) << std::endl;
                Py_DECREF(pValue);
            } else {
                Py_DECREF(pFunc);
                Py_DECREF(pModule);
                PyErr_Print();
                std::cerr << "Call failed" << std::endl;
                return 1;
            }
        } else {
            if (PyErr_Occurred()) PyErr_Print();
            std::cerr << "Cannot find function 'add'" << std::endl;
        }

        // Clean up
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
    } else {
        PyErr_Print();
        std::cerr << "Failed to load 'mymodule'" << std::endl;
        return 1;
    }

    // Finish the Python Interpreter
    Py_Finalize();
    return 0;
}
