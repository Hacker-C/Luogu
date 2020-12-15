//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <algorithm>

using namespace std;
typedef unsigned long ul;
typedef unsigned int ui;
ul a[10010];
ul ans[10010];

int main() {
    ui n, count = 0, j = 0;
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    if (n == 1) {
        cout << 1;
    } else {
        for (int i = 1; i < n; i++) {
            if (a[i] == a[i - 1] + 1) {
                count++;
                ans[j] = count;
            } else {
                count = 0;
                j++;
            }
        }
    }
    sort(ans, ans+j);
    cout << ans[j-1]+1;
}
