//
// Created by 15075 on 2020/12/1.
//

#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    //0-670-82162-4
    char a[10];
    int result = 0;
    scanf("%c-%c%c%c-%c%c%c%c%c-%c", &a[0], &a[1], &a[2], &a[3], &a[4], &a[5], &a[6], &a[7], &a[8], &a[9]);
    for (int i = 0; i < 9; i++) {
        result += (a[i] - '0') * (i + 1);
    }
    result %= 11;
    if (result == 10) {
        if (a[9] == 'X') cout << "Right";
        else {
            cout << a[0] << "-" << a[1] << a[2] << a[3] << "-"
                 << a[4] << a[5] << a[6] << a[7] << a[8] << "-"
                 << "X";
        }
    } else {
        if (result == a[9] - '0') cout << "Right";
        else {
            cout << a[0] << "-" << a[1] << a[2] << a[3] << "-"
                 << a[4] << a[5] << a[6] << a[7] << a[8] << "-"
                 << result;
        }
    }
    return 0;
}