//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int n, k = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (k < 10) cout << "0" << k++;
            else cout << k++;
        }
        cout << endl;
    }
    cout << endl;
    k = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << "  ";
        }
        for (int j = 1; j <= i; j++) {
            if (k < 10) cout << "0" << k++;
            else cout << k++;
        }
        cout << endl;
    }
}