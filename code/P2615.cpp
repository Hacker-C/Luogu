// ! Created by 15075 on 2020/12/11.
#include <iostream>
#include <cstring>

using namespace std;
int arr[40][40];

int main() {
    int N, x, y;
    cin >> N;
    memset(arr, 0, sizeof(arr));
    arr[0][(N - 1) / 2] = 1;
    //x,y记录填充元素K-1的位置
    x = 0;
    y = (N - 1) / 2;
    for (int k = 2; k <= N * N; k++) {
        if (x == 0 && y != N - 1) {
            x = N - 1;
            y = y + 1;
        } else if (x != 0 && y == N - 1) {
            x = x - 1;
            y = 0;
        } else if (x == 0 && y == N - 1) {
            x = x + 1;
            y = y;
        } else if (arr[x - 1][y + 1] == 0) {
            x = x - 1;
            y = y + 1;
        } else {
            x = x + 1;
            y = y;
        }
        arr[x][y] = k;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
