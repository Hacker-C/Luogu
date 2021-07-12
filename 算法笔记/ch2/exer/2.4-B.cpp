#include<cstdio>
int main() {
	int sum=0,i=1;
	do {
		sum += i;
		i++;
	} while (i<101);
	printf("%d\n",sum);
	return 0;
}
