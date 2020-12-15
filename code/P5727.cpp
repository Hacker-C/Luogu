//
// Created by 15075 on 2020/12/7.
//

#include <iostream>

using namespace std;
int a[10010];


int main() {
    int n, i = 0;
    cin >> n;
    while (1) {
        a[i] = n;
        i++;
        if (n == 1) {
            break;
        } else if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
    }
    for (int j = i-1; j >= 0; j--) {
        cout << a[j] << " ";
    }
}