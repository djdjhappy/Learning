#include <cstdio>
using namespace std;
int cost[105], fun[105];
int funSum[105][505], feeSum[105][505];
int main(){
	while (1){
		int budget, n;//budget <= 500, n <= 100;
		scanf("%d %d", &budget, &n);
		if (budget == 0 && n == 0){
			break;
		}
		for (int k = 0;k < n;k++){
			scanf("%d %d", &cost[k], &fun[k]);
		}
		for (int i = 0;i < n;i++){
			for (int b = 0;b <= budget;b++){
				if (i == 0){
					if (cost[i] > b){
						funSum[i][b] = 0;
						feeSum[i][b] = 0;
					}
					else{
						funSum[i][b] = fun[i];
						feeSum[i][b] = cost[i];
					}
				}
				else{
					if (cost[i] > b){
						funSum[i][b] = funSum[i - 1][b];
						feeSum[i][b] = feeSum[i - 1][b];
					}
					else{
						int f1 = funSum[i - 1][b];
						int f2 = funSum[i - 1][b - cost[i]] + fun[i];
						if (f1 > f2){
							funSum[i][b] = f1;
							feeSum[i][b] = feeSum[i - 1][b];
						}
						else{
							funSum[i][b] = f2;
							feeSum[i][b] = feeSum[i - 1][b - cost[i]] + cost[i];
						}
					}
				}
			}
		}
		printf("%d %d\n", feeSum[n - 1][budget], funSum[n - 1][budget]);
	}
	return 0;
}