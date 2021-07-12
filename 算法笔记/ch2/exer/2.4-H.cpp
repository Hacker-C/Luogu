#include<cstdio>
int fib(int n);
int main() {
	int n;
	scanf("%d",&n);
	printf("%d\n",fib(n));
	return 0;
}

int fib(int n) {
	int a=0,b=1,t;
	while (n--) {
		t = a;
		a = b;
		b = t;
		b = a + b;
	}
	return a;
}
