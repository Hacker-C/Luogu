//
// Created by 15075 on 2020/12/6.
//

#include <iostream>
#include <cstdio>

using namespace std;
#define S 300

int main() {
    int a[12], leftMoney = 0, saveMoney = 0;
    for (int i = 0; i < 12; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < 12; i++) {
        leftMoney += S;
        leftMoney -= a[i];
        if (leftMoney < 0) {
            cout << -(i + 1);
            return 0;
        } else {
            saveMoney += (leftMoney - leftMoney % 100);
            leftMoney %= 100;
        }
    }
    cout << saveMoney * 1.2 + leftMoney;
    return 0;
}