#include <iostream>
#include <algorithm>

using namespace std;
int ans[210 * 210];

int main() {
    int n, a, sum = 0, count = 0;
    cin >> n;
    fill(ans, ans + n * n, 1);
    while (cin >> a) {
        count++;
        if ((count) % 2) {
            for (int i = sum; i < sum + a; i++) {
                ans[i] = 0;
            }
        }
        sum += a;
        if (sum >= n*n) break;
    }
    for (int i = 0; i < n * n; i++) {
        cout << ans[i];
        if ((i + 1) % n == 0) cout << endl;
    }
}