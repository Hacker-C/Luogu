#include <cstring>
#include <cstdio>

int buy[1010][7];
int ans2[7] = {0};

int main() {
    int n, reward[7], count, flag;
    scanf("%d", &n);
    int ans[n];
    memset(ans, 0, sizeof(ans));
    for (int i = 0; i < 7; i++) scanf("%d", &reward[i]);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 7; ++j) {
            scanf("%d", &buy[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        count = 0;
        for (int j = 0; j < 7; ++j) {
            flag = 0;
            for (int k = 0; k < 7; k++) {
                if (buy[i][j] == reward[k]) flag = 1;
            }
            if (flag) count++;
        }
        ans[i] = count;//存储每一张票中了号码的个数
    }
    for (int i = 0; i < n; i++) {
        switch (ans[i]) {
            case 7:
                ans2[0]++;
                break;
            case 6:
                ans2[1]++;
                break;
            case 5:
                ans2[2]++;
                break;
            case 4:
                ans2[3]++;
                break;
            case 3:
                ans2[4]++;
                break;
            case 2:
                ans2[5]++;
                break;
            case 1:
                ans2[6]++;
                break;
        }
    }
    for (int i = 0; i < 7; i++) printf("%d ", ans2[i]);
}