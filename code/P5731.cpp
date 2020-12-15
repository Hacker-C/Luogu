#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

int main() {
    int n, x = 0, y = 0, t = 0;
    cin >> n;
    int m = n;
    int ans[n][n];
    int count = ceil(n / 2);
    while (count--) {
        for (int j = x; j < n - 1; j++) {
            ans[x][j] = ++t;
        }
        for (int i = y; i < n - 1; i++) {
            ans[i][n - 1] = ++t;
        }
        for (int j = n - 1; j > x; j--) {
            ans[n - 1][j] = ++t;
        }
        for (int i = n - 1; i > y; i--) {
            ans[i][y] = ++t;
        }
        x++;
        y++;
        n -= 1;
    }
    if (m % 2) {
        int k = ceil(m/2);
        ans[k][k] = m * m;
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            printf("%3d", ans[i][j]);
        }
        cout << endl;
    }
    return 0;
}
