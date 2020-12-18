//
// Created by 15075 on 2020/12/4.
//

#include <iostream>
using namespace std;
typedef int ElemType;
int main() {
    ElemType n;
    ElemType k = 1;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n - i; ++j) {
            if (k < 10) cout << "0" << k;
            else cout << k;
            ++k;
        }
        cout << endl;
    }
}