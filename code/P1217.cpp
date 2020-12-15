//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;
typedef unsigned long ul;

bool isInRange(ul x, ul m, ul n) {
    if (x >= m && x <= n) return true;
    else return false;
}

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
    ul a, b;
    scanf("%lu%lu", &a, &b);

    //1
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        if (isPrime(d1) && isInRange(d1, a, b)) cout << d1 << endl;
    }
    //2
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        ul t = 10 * d1 + d1;
        if (isPrime(t) && isInRange(t, a, b)) {
            cout << t << endl;
        }
    }
    //3
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        for (ul d2 = 0; d2 <= 9; d2++) {
            ul t = 100 * d1 + 10 * d2 + d1;
            if (isPrime(t) && isInRange(t, a, b)) {
                cout << t << endl;
            }
        }
    }
    //4
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        for (ul d2 = 0; d2 <= 9; d2++) {
            ul t = d1 * 1000 + d2 * 100 + d2 * 10 + d1;
            if (isPrime(t) && isInRange(t, a, b)) {
                cout << t << endl;
            }
        }
    }
    //5
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        for (ul d2 = 0; d2 <= 9; d2++) {
            for (ul d3 = 0; d3 <= 9; d3++) {
                ul t = 10000 * d1 + 1000 * d2 + 100 * d3 + 10 * d2 + d1;
                if (isPrime(t) && isInRange(t, a, b)) {
                    cout << t << endl;
                }
            }
        }
    }
    //6
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        for (ul d2 = 0; d2 <= 9; d2++) {
            for (ul d3 = 0; d3 <= 9; d3++) {
                ul t = 100000 * d1 + 10000 * d2 + 1000 * d3 + 100 * d3 + 10 * d2 + d1;
                if (isPrime(t) && isInRange(t, a, b)) {
                    cout << t << endl;
                }
            }
        }
    }
    //7
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        for (ul d2 = 0; d2 <= 9; d2++) {
            for (ul d3 = 0; d3 <= 9; d3++) {
                for (ul d4 = 0; d4 <= 9; d4++) {
                    ul t = 1000000 * d1 + 100000 * d2 + 10000 * d3 + 1000 * d4 + 100 * d3 + 10 * d2 + d1;
                    if (isPrime(t) && isInRange(t, a, b)) {
                        cout << t << endl;
                    }
                }
            }
        }
    }
    //8
    for (ul d1 = 1; d1 <= 9; d1 += 2) {
        for (ul d2 = 0; d2 <= 9; d2++) {
            for (ul d3 = 0; d3 <= 9; d3++) {
                for (ul d4 = 0; d4 <= 9; d4++) {
                    ul t = 10000000 * d1 + 1000000 * d2 + 100000 * d3 + 10000 * d4 + 1000 * d4 + 100 * d3 + 10 * d2 +
                           d1;
                    if (isPrime(t) && isInRange(t, a, b)) {
                        cout << t << endl;
                    }
                }
            }
        }
    }
    return 0;
}