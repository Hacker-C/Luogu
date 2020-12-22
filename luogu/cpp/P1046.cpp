//
// Created by 15075 on 2020/12/2.
//

#include <iostream>

using namespace std;
typedef unsigned long ul;

int main() {
    ul a[10], b, n = 0;
    for (int i = 0; i < 10; i++) {
        cin >> a[i];
    }
    cin >> b;
    for (int i = 0; i < 10; i++) {
        if (a[i] <= b+30) n++;
    }
    cout << n;
}