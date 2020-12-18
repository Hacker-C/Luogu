#include<cstdio>
int arr[210];
int main() {
	int n, x;
	while (scanf("%d", &n)!=EOF) {
		for (int i=0;i<n;i++) {
			scanf("%d", &arr[i]);
		}
		scanf("%d", &x);
		int k;
		for (k=0;k<n;k++) {
			if (x==arr[k]) {
				printf("%d", k);
				break;
			}
		}
		if (k==n) printf("%d", -1);
	}
	return 0;
}
