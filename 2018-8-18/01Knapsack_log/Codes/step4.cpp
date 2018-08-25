//bottom-up空间复杂度优化
#include <cstdio>
#include <algorithm>
#include <memory.h>
#define MAX_N 2005
#define MAX_S 2005
using namespace std;
int w[MAX_N];
int v[MAX_N];
int f[MAX_S];
int knapsack(int S, int N){
	memset(f, 0, sizeof(f));
	for (int i = 0;i < N;i++){
		for (int c = S;c >= w[i];c--){//根据之前经验，当c小于w[i]时答案是不变的，并且c始终递减，所以可以省略c < w[i]的部分
			f[c] = max(f[c], f[c - w[i]] + v[i]);
		}
	}
	return f[S];
}
int main(){
	int S, N;
	scanf("%d%d", &S, &N);
	for (int i = 0;i < N;i++){
		scanf("%d%d", &w[i], &v[i]);
	}
	printf("%d\n", knapsack(S, N));
}
