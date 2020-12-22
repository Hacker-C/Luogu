#include <iostream>
#include <cstring>

using namespace std;
int arr[2000010];

int main() {
    int n, t;
    double a, max = 0;
    memset(arr, -1, sizeof(arr));
    cin >> n;
    while (n--) {
        cin >> a >> t;
        if (int(a * t) > max) {
            max = (int) a * t;
        }
        for (int i = 1; i <= t; i++) {
            arr[int(a * i)] = -arr[int(a * i)];
        }
    }
    for (int i = 0; i <= max; i++) {
        if (arr[i] == 1) cout << i;
    }
    return 0;
}