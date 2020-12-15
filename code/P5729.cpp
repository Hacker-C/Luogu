#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
    int w, x, h, q, x1, x2, y1, y2, z1, z2, ans = 0;
    scanf("%d%d%d", &w, &x, &h);
    scanf("%d", &q);
    int arr[22][22][22];
    memset(arr, -1, sizeof(arr));
    while (q--) {
        cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                for (int k = z1; k <= z2; k++) {
                    arr[i][j][k] = 0;
                }
            }
        }
    }
    for (int i = 1; i <= w; i++) {
        for (int j = 1; j <= x; j++) {
            for (int k = 1; k <= h; k++) {
                if (arr[i][j][k]) ans++;
            }
        }
    }
    printf("%d", ans);
}