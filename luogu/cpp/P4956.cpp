//
// Created by 15075 on 2020/12/6.
//

#include <iostream>

using namespace std;

int main() {
    double n, k;
    cin >> n;
    for (int x = 100; x >= 1; x--) {
        k = (n / 364 - x) / 3;
        if (int(k)==k && k > 0) {
            cout << x << endl << k;
            break;
        }
    }
}