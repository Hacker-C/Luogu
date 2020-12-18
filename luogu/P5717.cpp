//
// Created by 15075 on 2020/12/2.
//

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;
typedef unsigned long ul;

int main() {
    int a[3];
    cin >> a[0] >> a[1] >> a[2];
    sort(a, a + 3);
    if (a[0] + a[1] > a[2] && a[1] + a[2] > a[0] && a[0] + a[2] > a[1]) {
        if (pow(a[0], 2) + pow(a[1], 2) == pow(a[2], 2)) cout << "Right triangle\n";
        if (pow(a[0], 2) + pow(a[1], 2) > pow(a[2], 2)) cout << "Acute triangle\n";
        if (pow(a[0], 2) + pow(a[1], 2) < pow(a[2], 2)) cout << "Obtuse triangle\n";
        if (a[0] == a[1] || a[1] == a[2]) cout << "Isosceles triangle\n";
        if (a[0] == a[1] && a[1] == a[2]) cout << "Equilateral triangle";
    } else {
        cout << "Not triangle";
    }
}