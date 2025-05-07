#include <iostream>
#include <cassert>

int fib(int n) {
    if(n < 2) {
        return n;
    } else {
        return fib(n - 2) + fib(n - 1);
    }
}

int metaFibonacciSum(int n) {

    if(n < 2) {
        return n;
    } else {

        int sumOfPartiamSums = 0;
        for(int i = 0; i <= n; i++) {
            int partialSum = 0;
            for(int j = 0; j <= fib(i); j++) {
                partialSum += fib(j);
            }
            sumOfPartiamSums += partialSum;
        }

        return sumOfPartiamSums;

    }

}

int main()
{
    std::cout << "Testing...\n";
    
    assert(metaFibonacciSum(6)==74);

    std::cout << "Success!\n";

    return 0;
}
