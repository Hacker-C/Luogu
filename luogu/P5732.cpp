// !Created by 15075 on 2020/12/15.

#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int ans[n][n];
    for (int i = 0; i < n; i++) {
        ans[i][0] = 1;
        ans[i][i] = 1;
    }
    for (int i = 2; i < n; i++) {
        for (int j = 1; j < i; j++) {
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j];
        }
    }
    for (int i=0;i<n;i++) {
        for (int j = 0; j <= i; j++) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}