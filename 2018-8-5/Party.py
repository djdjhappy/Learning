while True:
    budget, n = map(int, input().rstrip().split())
    #n:number of parties
    #budget:预算的最多花费
    if budget == 0 and n == 0:
        break
    cost = []
    fun = []
    for _ in range(n):
        inp = input().rstrip().split()
        cost.append(int(inp[0]))
        fun.append(int(inp[1]))
    funSum = [[None] * (budget + 1) for i in range(n)]#总fun值
    feeSum = [[None] * (budget + 1) for i in range(n)]#总费用
    for i in range(n):#i = 0, 1, 2, ..., n - 1
        for b in range(0, budget + 1):
            if i == 0:
                if cost[i] > b:
                    funSum[i][b] = 0
                    feeSum[i][b] = 0
                else:
                    funSum[i][b] = fun[i]
                    feeSum[i][b] = cost[i]
            else:
                if cost[i] > b:
                    funSum[i][b] = funSum[i - 1][b]
                    feeSum[i][b] = feeSum[i - 1][b]
                else:
                    f1 = funSum[i - 1][b]
                    f2 = funSum[i - 1][b - cost[i]] + fun[i]
                    if f1 > f2:
                        funSum[i][b] = f1
                        feeSum[i][b] = feeSum[i - 1][b]
                    else:
                        funSum[i][b] = f2
                        feeSum[i][b] = feeSum[i - 1][b - cost[i]] + cost[i]
    print(feeSum[-1][-1], funSum[-1][-1])
