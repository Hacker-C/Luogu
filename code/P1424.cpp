//
// Created by 15075 on 2020/12/1.
//

#include <iostream>
using namespace std;
int main() {
    int x, n;
    cin >> x >> n;
    int t, sum = 0;
    for (int i = 1; i <= n; i++) {
        t = (x + i - 1) % 7 == 0 ? 7 : (x + i - 1) % 7;
        if (t != 6 && t != 7) sum += 250;
    }
    cout << sum;
}