#include <iostream>
#include <cstring>

using namespace std;
#define MAX_SIZE 10010
int arr[MAX_SIZE];

int main() {
    memset(arr, -1, sizeof(arr));
    int l, m, a, b, k = 0;
    cin >> l >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        for (int j = a; j <= b; j++) {
            arr[j] = 0;
        }
    }
    for (int i = 0; i <= l; i++) {
        if (arr[i] == -1) {
            k++;
        }
    }
    cout << k;
}