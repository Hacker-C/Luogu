// !Created by 15075 on 2020/12/11.

#include <iostream>

using namespace std;
int arr[3010];

int main() {
    int n, m, min = 0, sum = 0;
    cin >> n >> m;
    if (n == 0 || m == 0) {
        cout << 0;
        return 0;
    }
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < m; i++) {
        min += arr[i];
    }
    for (int i = 1; i <= n - m; i++) {
        for (int j = i; j < i + m; j++) sum += arr[j];
        if (sum < min) {
            min = sum;
        }
        sum = 0;
    }
    cout << min;
    return 0;
}