// ! Created by 15075 on 2020/12/15.

#include <iostream>
#include <cstring>

using namespace std;

int main() {
    int n, m, k, x, y, count = 0;
    cin >> n >> m >> k;
    int ans[n + 1][n + 1];
    memset(ans, -1, sizeof(ans));
    while (m--) {
        cin >> x >> y;
        for (int i = x - 2; i <= x + 2; i++) {
            if (!(i < 0 || i > n)) ans[i][y] = 0;
        }
        for (int j = y - 2; j <= y + 2; j++) {
            if (!(j < 0 || j > n)) ans[x][j] = 0;
        }
        if (!(x - 1 < 0 || y - 1 < 0 || y + 1 > n || x + 1 > n))
            ans[x - 1][y - 1] = ans[x - 1][y + 1] = ans[x + 1][y - 1] = ans[x + 1][y + 1] = 0;
    }
    while (k--) {
        cin >> x >> y;
        for (int i = x - 2; i <= x + 2; i++) {
            for (int j = y - 2; j <= y + 2; j++) {
                if (!(x - 2 < 0 || y - 2 < 0 || x + 2 > n || y + 2 > n))
                    ans[i][j] = 0;
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (ans[i][j]) count++;
        }
    }
    cout << count;
}