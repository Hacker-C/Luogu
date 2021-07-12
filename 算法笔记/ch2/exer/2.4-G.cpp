#include<cstdio>
int main() {
	double i=1,sum=0,j=1;
	while (1/i > 10e-7) {
		sum += j*1/i;
		i += 2;
		j *= -1;
	}
	printf("PI=%10.8lf\n",sum*4);
	return 0;
}
