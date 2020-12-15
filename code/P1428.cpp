//
// Created by 15075 on 2020/12/6.
//

#include <cstdio>

int main() {
    int n, count = 0;
    scanf("%d", &n);
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i]) count++;
        }
        printf("%d ", count);
        count = 0;
    }
}