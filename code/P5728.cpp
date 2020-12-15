#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    int n, count = 0;
    cin >> n;
    int arr[n][3];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            char flag = 1;
            int sum1 = 0, sum2 = 0;
            for (int k = 0; k < 3; k++) {
                if (abs(arr[i][k] - arr[j][k]) > 5) flag = 0;
                sum1 += arr[i][k];
                sum2 += arr[j][k];
            }
            if (flag && abs(sum1 - sum2) <= 10) count++;
        }
    }
    cout << count;
}