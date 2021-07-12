#include<cstdio>
int main() {
	int N,sum=0,i=1;
	scanf("%d",&N);
	while (1) {
		sum+=i;
		if (i>=100) break;
		i++;
	}
	printf("%d\n",sum);
	return 0;
}
