//bottom-up
#include <cstdio>
#include <algorithm>
#define MAX_N 2005
#define MAX_S 2005
using namespace std;
int w[MAX_N];
int v[MAX_N];
int f[MAX_S][MAX_N];
int knapsack(int S, int N){
	for (int i = 0;i < N;i++){//i = 0, 1, ..., N - 1
		for (int c = 0;c <= S;c++){//c = 0, 1, ..., S
			if (i == 0){
				f[c][i] = (w[i] > c)?0:v[i];
			}
			else{
				if (w[i] > c){
					f[c][i] = f[c][i - 1];
				}
				else{
					f[c][i] = max(f[c][i - 1], f[c - w[i]][i - 1] + v[i]);
				}
			}
		}
	}
	return f[S][N - 1];
}
int main(){
	int S, N;
	scanf("%d%d", &S, &N);
	for (int i = 0;i < N;i++){
		scanf("%d%d", &w[i], &v[i]);
	}
	printf("%d\n", knapsack(S, N));
}
