//
// Created by 15075 on 2020/12/2.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int a[3];
    char b[3];
    for (int i = 0; i < 3; i++) cin >> a[i];
    for (int i = 0; i < 3; i++) cin >> b[i];
    sort(a, a + 3);
    for (int i = 0; i < 3; i++) {
        switch (b[i]) {
            case 'A':
                b[i] = 0;
                break;
            case 'B':
                b[i] = 1;
                break;
            case 'C':
                b[i] = 2;
                break;
        }
    }
    for (int i = 0; i < 3; i++) {
        cout << a[b[i]] << " ";
    }
}
