#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstdbool>
#include <string.h>
#include <math.h>
 
using namespace std;
 
 
 
int main()
{
    int a[1000005] = {0};
    int b[100005] = {0};
    int n,t;
    cin >> n >> t;
    for (int i=1;i<=n;i++)
    {
        cin >> a[i];
        b[i] = b[i-1] + a[i];
    }
    while (t--)
    {
        int l,r;
        int sum = 0;
        cin >> l >> r;
        sum = b[r] - b[l-1];
        printf("%d\n",sum);
    }
    return 0;
}