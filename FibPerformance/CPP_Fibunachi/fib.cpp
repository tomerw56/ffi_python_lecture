#include "fib.hpp"
long long fibonacci(int number) {
   if (number <= 1) return number;
        long long  a = 0, current = 1, c;
        for (int i = 2; i <= number; ++i) {
            c = a + current;
            a = current;
            current = c;
        }
    return(current);
}