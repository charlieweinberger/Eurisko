#include <iostream>
#include <cassert>

int main()
{
    int array[5]{ 30, 50, 20, 10, 40 };

    for(int i = 0; i < 5; i++) {

        int minElem = 1000000;
        int minElemIndex = 1000000;
        for(int j = 0; j < 5; j++) {
            int jthELem = array[j];
            if (i <= j && jthELem < minElem) {
                minElem = jthELem;
                minElemIndex = j;
            }
        }

        int currentElem = array[i];

        array[i] = minElem;
        array[minElemIndex] = currentElem;

    }

    std::cout << "\nTesting...\n";

    assert(array[0]==10);
    assert(array[1]==20);
    assert(array[2]==30);
    assert(array[3]==40);
    assert(array[4]==50);

    std::cout << "Succeeded\n";

    return 0;
}