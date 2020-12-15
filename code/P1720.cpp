//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;
int main() {
    double sum;
    int n;
    cin >> n;
    sum = pow((1+sqrt(5))/2, n) - pow((1-sqrt(5))/2, n);
    sum /= sqrt(5);
    printf("%.2f", sum);
}