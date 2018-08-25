//top-down
#include <algorithm>
#include <cstdio>
#define MAX_N 2005
using namespace std;
int w[MAX_N];
int v[MAX_N];
int knapsack(int S, int i){
	if (i == 0){
		return (w[i] > S)?0:v[i];//如果超过容量则最大价值为0，否则为首件物品重量
	}
	else{
		if (w[i] > S) return knapsack(S, i - 1);//当前物品超重，最大价值只能是前i - 1件物品的最大价值
		else
			return max(knapsack(S, i - 1), knapsack(S - w[i], i - 1) + v[i]);
	}
}
int main(){
	int S, N;
	scanf("%d%d", &S, &N);
	for (int i = 0;i < N;i++){
		scanf("%d%d", &w[i], &v[i]);
	}
	printf("%d\n", knapsack(S, N - 1));
}
