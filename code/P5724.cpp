//
// Created by 15075 on 2020/12/5.
//

#include <iostream>

using namespace std;

int main() {
    int n, min, max;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) cin >> a[i];
    min = max = a[0];
    for (int i = 1; i < n; i++) {
        max = a[i] > max ? a[i] : max;
        min = a[i] < min ? a[i] : min;
    }
    cout << max - min;
}