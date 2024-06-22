// gcc -shared -o libmultiply.so -fPIC multiply.c
// multiply.c
#include <stdio.h>

void multiply_by_two(double* array, int length) {
    for (int i = 0; i < length; i++) {
        array[i] *= 2;
    }
}