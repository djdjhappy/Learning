#from pprint import pprint
def algo(w, v, n, C):
    arr = [[None] * (C + 1) for i in range(n)]
    for i in range(n):
        for c in range(0, C + 1):
            if i == 0:
                arr[i][c] = 0 if w[i] > c else v[i]
            else:
                if w[i] > c:
                    arr[i][c] = arr[i - 1][c]
                else:
                    arr[i][c] = max(arr[i - 1][c], arr[i - 1][c - w[i]] + v[i])
    #pprint(arr)
    return arr[-1][-1]
S, N = map(int, input().rstrip().split())
w = []
v = []
for i in range(N):
    inp = input().rstrip().split()
    w.append(int(inp[0]))
    v.append(int(inp[1]))
print(algo(w, v, N, S))
