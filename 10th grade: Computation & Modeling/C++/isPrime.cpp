#include <iostream>
#include <cassert>

// Write a function that determines whether a nonnegative integer x is prime.
// Loop through numbers between 2 and x-1 and see if you can find any factors.
// Note that neither 0 nor 1 are prime.

bool isPrime(int x)
{
    if (x > 1) {
        for(int i = 2; i < x + 2; i++) {
            if (x > i) {
                if ((x % i) == 0) {
                    return false;
                }
            }
        }
        return true;
    }
    return false;
}

int main()
{
    assert(!isPrime(0));
    assert(!isPrime(1));
    assert(isPrime(2));
    assert(isPrime(3));
    assert(!isPrime(4));
    assert(isPrime(5));
    assert(isPrime(7));
    assert(!isPrime(9));
    assert(isPrime(11));
    assert(isPrime(13));
    assert(!isPrime(15));
    assert(!isPrime(16));
    assert(isPrime(17));
    assert(isPrime(19));
    assert(isPrime(97));
    assert(!isPrime(99));
    assert(!isPrime(99));
    assert(isPrime(13417));

    std::cout << "Success!\n";

    return 0;
}