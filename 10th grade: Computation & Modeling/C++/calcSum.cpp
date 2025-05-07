#include <iostream>
#include <cassert>

int calcSum(int m, int n) {

    int ascending[m][n];

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            ascending[i][j] = n*i + j + 1;
        }
    }

    int descending[n][m];

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            descending[i][j] = (m*n) - (m*i + j);
        }
    }

    int ascendingTimesDescending[m][m];

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < m; j++) {
        
            int rowTotal = 0;

            for(int k = 0; k < n; k++) {
                rowTotal += ascending[i][k] * descending[k][j];
            }

            ascendingTimesDescending[i][j] = rowTotal;

        }
    }

    int sum = 0;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < m; j++) {
            sum += ascendingTimesDescending[i][j];
        }
    }

    return sum;

}

int main() {
    
    std::cout << "Testing...\n";
    
    assert(calcSum(2,3) == 131);

    std::cout << "Success!\n";

    return 0;
}
