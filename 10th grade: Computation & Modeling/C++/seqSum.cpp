#include <iostream>
#include <cassert>

int seqSum(int n) {
    
    int terms[n + 1];
    terms[0] = 0;
    terms[1] = 1;

    for (int i = 2; i <= n; i++) {
        terms[i] = terms[i - 1] + 2 * terms[i - 2];
    }
    
    int sum = 0;
    for(int i = 0; i <= n; i++) {
        sum += terms[i];
    }
    return sum;

}

int extendedSeqSum(int n) {
    
    int terms[n + 1];
    terms[0] = 0;
    terms[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        terms[i] = terms[i - 1] + 2 * terms[i - 2];
    }
    
    return seqSum(terms[n]);

}

int main()
{
    std::cout << "Testing...\n";
    
    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!\n";

    return 0;
}