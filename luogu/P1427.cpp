//
// Created by 15075 on 2020/12/6.
//

#include <iostream>
using namespace std;
typedef unsigned long ul;
int main() {
    ul a[110], b;
    int i = 0;
    while (cin>>b) {
        a[i++] = b;
        if (b==0) break;
    }
    for (int j = i - 2; j >=0; j--) {
        cout << a[j] << " ";
    }
}