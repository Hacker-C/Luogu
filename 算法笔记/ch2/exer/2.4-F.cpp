#include<cstdio>
int main() {
	for (int i=1;i<=4;i++) {
		for (int j=i;j<=5*i;j+=i) {
			printf("%3d",j);
		}
		printf("\n");
	}
	return 0;
}
