//
// Created by 15075 on 2020/12/4.
//

//#include <iostream>
//
//using namespace std;
//typedef double ElemType;
//
//int main() {
//    ElemType k, sum = 0, i = 1;
//    cin >> k;
//    while (sum <= k) {
//        sum += 1 / i;
//        i++;
//    }
//    cout << i - 1;
//}

#include <iostream>

using namespace std;

int main() {
    int n1, n2, a, sum = 0;
    cin >> n;
    for (int i = 0; i < n1; i++) {
        cin >> n2;
        for (int j = 0; j < n2; j++) {
            cin >> a;
            sum += a;
        }
        cout << sum << endl << endl;
        sum = 0;
    }
}

