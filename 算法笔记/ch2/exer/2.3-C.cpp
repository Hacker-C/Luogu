#include<cstdio>
int main() {
	double a,b,c,t;
	scanf("%lf%lf%lf",&a,&b,&c);
	if (a>b) {
		t = a;
		a = b;
		b = t;
	}
	if (b > c) {
		t = b;
		b = c;
		c = t;
	}
	if (a>b) {
		t = a;
		a = b;
		b = t;
	}
	printf("%.2lf %.2lf %.2lf\n",a,b,c);
	return 0;
}
