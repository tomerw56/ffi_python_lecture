// demo.cpp
#include <iostream>

void cppFunction() {
    std::cout << "This is a C++ function." << std::endl;
}

extern "C" void cFunction() {
    std::cout << "This is a C function." << std::endl;
}

int main() {
    cppFunction();
    cFunction();
    return 0;
}
