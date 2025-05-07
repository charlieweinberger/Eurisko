#include <iostream>
#include <cassert>

int dotProduct (int array1[], int array2[], int len) {
    int answer = 0;
    for (int i = 0; i < len; i++) {
        answer += array1[i] * array2[i];
    }
    return answer;
}

int main()
{

    int array1[] = {1, 2, 3, 4};
    int array2[] = {5, 6, 7, 8};
    int length = sizeof(array1) / sizeof(array1[0]);
    int ans = dotProduct(array1, array2, length);

    std::cout << "Testing...\n";
    assert(ans == 70);
    std::cout << "Success!\n";

    return 0;
}