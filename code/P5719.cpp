//
// Created by 15075 on 2020/12/3.
//
#include <iostream>
#include <cstdio>
using namespace std;
typedef unsigned int ElemType;

int main() {
    ElemType n, k, s1, s2, c1, c2;
    s1 = s2 = c1 = c2 = 0;
    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        if (i % k == 0) {
            s1 += i;
            c1++;
        } else {
            s2 += i;
            c2++;
        }
    }
    printf("%.1f %.1f", (float) s1 / c1, (float) s2 / c2);
}