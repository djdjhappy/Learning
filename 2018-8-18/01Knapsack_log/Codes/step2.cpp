//top-down with memoization
#include <algorithm>
#include <cstdio>
#include <memory.h>
#define MAX_N 2005
#define MAX_S 2005
using namespace std;
int w[MAX_N];
int v[MAX_N];
int cache[MAX_N][MAX_S];//新增的缓存二维数组
int knapsack(int S, int i){
	if (cache[i][S] != -1){//已经计算过
		return cache[i][S];
	}
	int result;
	if (i == 0){
		result = (w[i] > S)?0:v[i];//如果超过容量则最大价值为0，否则为首件物品重量
	}
	else{
		if (w[i] > S) result = knapsack(S, i - 1);//当前物品超重，最大价值只能是前i - 1件物品的最大价值
		else
			result =  max(knapsack(S, i - 1), knapsack(S - w[i], i - 1) + v[i]);
	}
	cache[i][S] = result;//记录答案
	return result;
}
int main(){
	int S, N;
	scanf("%d%d", &S, &N);
	memset(cache, -1, sizeof(cache));//-1标记未计算答案
	for (int i = 0;i < N;i++){
		scanf("%d%d", &w[i], &v[i]);
	}
	printf("%d\n", knapsack(S, N - 1));
}
