//
// Created by 15075 on 2020/12/3.
//

#include <iostream>
#include <cmath>

using namespace std;
typedef long double ElemType;
int main() {
    ElemType a;
    int i = 0;
    cin >> a;
    if (a == 1) {
        cout << 1;
    } else {
        while (a > 1) {
            a = ceil(a /  2);
            i++;
        }
        cout << i;
    }
}