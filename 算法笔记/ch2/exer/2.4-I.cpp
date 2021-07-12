#include<cstdio>
int main() {
	int top=2,bottom=1,temp;
	double sum=0.0;
	for (int i=0;i<20;i++) {
		sum += (double)top/bottom;
		temp = top + bottom;
		bottom = top;
		top = temp;
	}
	printf("%.6lf",sum);
	return 0;
} 
