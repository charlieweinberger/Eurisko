#include <iostream>
#include <cassert>

int nthFib (int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return nthFib(n - 1) + nthFib(n - 2);
    }
}

int calcIndex (int n) {
    
    for (int i = 0; i < 99999; i++) {
        if (nthFib(i) > n) {
            return i;
        }
    }

}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!\n";

    return 0;
}