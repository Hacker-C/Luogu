//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <cmath>

using namespace std;
typedef unsigned long ul;

ul isPrime(ul x) {
    if (x == 2 || x == 3) {
        return true;
    } else {
        bool flag = true;
        for (int i = 2; i < sqrt(x) + 1; i++) {
            if (x % i == 0) {
                flag = false;
                break;
            }
        }
        if (flag) return true;
        else return false;
    }
}

int main() {
    ul K, i = 2, S = 0, count = 0;
    cin >> K;
    while (1) {
        if (S <= K) {
            if (isPrime(i)) {
                S += i;
                if (S <= K) {
                    cout << i << endl;
                    count++;
                }
            }
            i++;
        } else {
            break;
        }
    }
    cout << count;
}