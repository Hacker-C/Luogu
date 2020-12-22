#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
typedef unsigned long ul;

int main() {
    ul m, n;
    cin >> m >> n;
    char ss[11];
    int ans[10];
    memset(ans, 0, sizeof(ans));
    for (ul i = m; i <= n; i++) {
        sprintf(ss,"%lu", i);
        for (int j = 0; j < strlen(ss); j++) {
            ans[ss[j] - '0']++;
        }
    }
    for (int i = 0; i < 10; i++) {
        cout << ans[i] << " ";
    }
}