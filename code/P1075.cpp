//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <cmath>

using namespace std;
typedef unsigned long ul;

bool isPrime(ul x) {
    if (x == 2 || x == 3) {
        return true;
    } else {
        bool flag = true;
        for (int i = 2; i < sqrt(x) + 1; i++) {
            if (x % i == 0) {
                flag = false;
            }
        }
        return flag;
    }
}

int main() {
    ul n;
    cin >> n;
    for (ul j = 2; j < (int) (n / 2) + 1; j++) {
        if (n % j == 0 && isPrime(j) && isPrime(n / j)) {
            cout << n / j;
            return 0;
        }
    }
}