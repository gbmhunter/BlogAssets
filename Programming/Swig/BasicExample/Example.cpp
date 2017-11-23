
#include "Example.hpp"

int ExClass::Factorial(int n) {
    if (n < 0) {
        return 0;
    }
    if (n == 0) {
        return 1;
    }
    else {        
        return n * ExClass::Factorial(n-1);
    }
}