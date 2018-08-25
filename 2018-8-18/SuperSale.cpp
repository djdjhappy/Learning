#include <cstdio>
#include <memory.h>
#include <algorithm>
#define MAX_N 1005
#define MAX_G 105
#define MAX_MW 35
using namespace std;
int P[MAX_N];//price
int W[MAX_N];//weight
int MW[MAX_G];
int f[MAX_MW];//一维数组，长度为背包最大容积
int algo(int N, int G){
	int result = 0;
	for (int g = 0;g < G;g++){
		memset(f, 0, sizeof(f));
		int C = MW[g];
		for (int i = 0;i < N;i++){
			for (int c = C;c >= W[i];c--){
				f[c] = max(f[c], f[c - W[i]] + P[i]);
			}
		}
		result += f[C];
	}
	return result;
}
int main(){
	int T;
	scanf("%d", &T);
	while (T--){
		int N, G;
		scanf("%d", &N);
		for (int i = 0;i < N;i++){
			scanf("%d%d", &P[i], &W[i]);
		}
		scanf("%d", &G);
		for (int j = 0;j < G;j++){
			scanf("%d", &MW[j]);
		}
		printf("%d\n", algo(N, G));
	}
}
