#include <cstdio>
#include <algorithm>
using namespace std;
int arr[2005][2005];
int w[2005], v[2005];
int algo(int n, int C){
	for(int i = 0;i < n;i++){
		for(int c = 0;c <= C;c++){
			if (i == 0){
				if (w[i] > c){
					arr[i][c] = 0;
				}
				else{
					arr[i][c] = v[i];
				}
			}
			else{
				if (w[i] > c){
					arr[i][c] = arr[i - 1][c];
				}
				else{
					arr[i][c] = max(arr[i - 1][c], arr[i - 1][c - w[i]] + v[i]);
				}
			}
		}
	}
	// for(int i = 0;i < n;i++){
		// for(int c = 0;c <= C;c++){
			// printf("%d\t", arr[i][c]);
		// }
		// printf("\n");
	// }
	return arr[n - 1][C];
}
int main(){
	int S, N;
	scanf("%d %d", &S, &N);
	for(int i = 0;i < N;i++){
		scanf("%d %d", &w[i], &v[i]);
	}
	printf("%d", algo(N, S));
	return 0;
}