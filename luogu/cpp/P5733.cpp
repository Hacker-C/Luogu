#include <iostream>
#include <cstring>

using namespace std;
char ch[110];

int main() {
    cin >> ch;
    int length = strlen(ch);
    for (int i = 0; i < length; i++) {
        if (ch[i] >= 'a' && ch[i] <= 'z') {
            ch[i] = ch[i] - 32;
        }
    }
    cout << ch;
}