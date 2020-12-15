//
// Created by 15075 on 2020/12/5.
//

#include <iostream>
#include <cstring>

using namespace std;
#define LENGTH 12
char str[LENGTH];

int main() {
    int k = 0;
    cin >> str;
    if (str[0] == '-') {
        cout << str[0];
        k++;
    } else if (strlen(str) == 1 && str[0] == '0') {
        cout << "0";
    }
    int flag = 1;
    for (int i = strlen(str) - 1; i >= k; i--) {
        if (str[i] != '0') flag = 0;
        if (!flag) cout << str[i];
    }

}