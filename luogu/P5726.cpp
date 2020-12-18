//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    double min, max, sum = 0;
    int n;
    cin >> n;
    double scores[n];
    if (n == 0) {
        cout << "0.00";
        return 0;
    }
    for (int i = 0; i < n; i++) {
        scanf("%lf", &scores[i]);
        sum += scores[i];
    }
    max = min = scores[0];
    for (int i = 1; i < n; i++) {
        min = scores[i] < min ? scores[i] : min;
        max = scores[i] > max ? scores[i] : max;
    }
    printf("%.2lf", (sum - max - min) / (n - 2));
}