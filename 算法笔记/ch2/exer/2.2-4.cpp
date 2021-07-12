#include<cstdio>
#include<cmath>
int main() {
	double a,b,c;
	scanf("%lf%lf%lf",&a,&b,&c);
	double d = sqrt(pow(b,2)-4*a*c);
	double r1 = (-b+d)/(2*a);
	double r2 = (-b-d)/(2*a);
	printf("r1=%7.2lf\n",r1);
	printf("r2=%7.2lf",r2);
	return 0;	
}
