//
// Created by 15075 on 2020/12/5.
//

#include <iostream>

using namespace std;

int main() {
    double x, sum =  0, v = 2;
    int count = 0;
    cin >> x;
    while (sum <=x) {
        sum += v;
        v *= 0.98;
        ++count;
    }
    cout << count;
    return 0;
}