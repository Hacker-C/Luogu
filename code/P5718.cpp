//
// Created by 15075 on 2020/12/3.
//

#include <iostream>
using namespace std;
typedef unsigned int ElemType;
int main() {
    ElemType n, m, min;
    cin >> n;
    for (ElemType i = 0; i < n; i++) {
        if (i == 0) cin >> min;
        else cin >> m;
        if (m < min) min = m;
    }
    cout << min;
}