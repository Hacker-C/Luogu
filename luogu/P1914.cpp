//
// Created by 15075 on 2020/12/9.
//

#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;
char ch[51];

int main() {
    int n;
    cin >> n >> ch;
    int length = strlen(ch);
    n %= 26;
    for (int i = 0; i < length; i++) {
        if (ch[i]+n > 'z') {
            ch[i] = 'a' + ch[i] + n - 'z' - 1;
        } else {
            ch[i] += n;
        }
    }
    cout << ch;
}