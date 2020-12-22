#include <iostream>
#include <cstring>

using namespace std;
int arr[110];
int ans[110];

int main() {
    memset(ans, 0, sizeof(ans));
    int n, count = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (arr[i] == arr[j] + arr[k] && j != i && k != i && k != j) {
                    ans[i]++;
                    break;
                }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (ans[i]) count++;
    }
    cout << count;
}