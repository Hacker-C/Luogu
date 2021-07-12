#include<cstdio>
#include<cmath>
int main() {
	double a,b,c;
	scanf("%lf%lf%lf",&a,&b,&c);
	double deta = pow(b,2)-4*a*c;
	if (deta<0) printf("No real roots!\n");
	else {
		double r1 = (-b+sqrt(deta))/(2*a);
		double r2 = (-b-sqrt(deta))/(2*a);
		printf("r1 = %7.2lf\n", r1);
		printf("r2 = %7.2lf\n", r2);
	}
	return 0;
}
