// !Created by 15075 on 2020/12/13.

#include <iostream>
#include <cstring>

using namespace std;
int a[100];

int main() {
    memset(a, 0, sizeof(a));
    int s1, s2, s3,ans;
    int maxCount = 0;
    cin >> s1 >> s2 >> s3;
    for (int i = 1; i <= s1; i++) {
        for (int j = 1; j <= s2; j++) {
            for (int k = 1; k <= s3; k++) {
                a[i + j + k]++;
            }
        }
    }
    for (int i = 3; i <= s1 + s2 + s3; i++) {
        if (a[i]>maxCount) {
            maxCount = a[i];
            ans = i;
        }
    }
    cout << ans;
    return 0;
}