#include<cstdio>
int main() {
	double x,y;
	scanf("%lf%lf",&x,&y);
	if (x<y) {
		printf("%.2lf %.2lf",x,y);
	} else {
		printf("%.2lf %.2lf",y,x);
	}
	return 0;
}
