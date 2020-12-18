//
// Created by 15075 on 2020/12/4.
//

#include <iostream>

using namespace std;
typedef unsigned long ul;

int main() {
    ul K, S = 0, count = 0;
    cin >> K;
    for (int i = 1; i <= K; ++i) {
        for (int j = 1; j <= i; ++j) {
            if (count >= K) break;
            S += i;
            count++;
        }
    }
    cout << S;
}