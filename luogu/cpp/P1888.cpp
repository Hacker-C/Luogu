//
// Created by 15075 on 2020/12/1.
//

#include <iostream>
#include <algorithm>

typedef unsigned long long ul;

ul gcd(ul, ul);

ul max(ul, ul);

ul min(ul, ul);

using namespace std;

int main() {
    ul arr[3];
    cin >> arr[0] >> arr[1] >> arr[2];
    sort(arr, arr + 3);
    cout << (arr[0] / gcd(arr[0], arr[2])) << "/" << (arr[2] / gcd(arr[0], arr[2]));
}

ul gcd(ul x, ul y) {
    int a = min(x, y);
    int b = max(x, y);
    int t1,t2;
    while (b != a) {
        b = b - a;
        t1 = min(a,b);
        t2 = max(a,b);
        a = t1;
        b = t2;
    }
    return a;
}

ul max(ul x, ul y) {
    if (x > y) return x;
    else return y;
}

ul min(ul x, ul y) {
    if (x < y) return x;
    else return y;
}