def sortEdges(edges):
    if not edges:
        return edges
    E1, E2 = [], []
    for e in sortEdges(edges[1:]):
        if e[2] <= edges[0][2]:
            E1.append(e)
        else:
            E2.append(e)
    return E1 + [edges[0]] + E2
##print(sortEdges([[1, 2, 4], [1, 2, 1], [1, 2, 2], [1, 2, 3]]))
def solve(edges, n):
    #using Krascal's Algorithm
    E = sortEdges(edges)
    ##print(E)
    groups = [i for i in range(n)]
    cost = 0
    for (u, v, c) in E:
        if not (groups[u] == groups[v]):
            cost += c
            val = groups[u]
            for i in range(n):
                if groups[i] == val:
                    groups[i] = groups[v]
    total = 0
    for e in E:
        total += e[2]
    return total - cost
def main():
    while True:
        m, n = list(map(int, input().rstrip().split()))
        #m:交叉路口总数
        #n:街道总数
        if m == n == 0:
            return
        edges = []
        for _ in range(n):
            edge = list(map(int, input().rstrip().split()))#edge = (x, y, z)
            edges.append(edge)
        ##print("<<<<<", edges)
        solution = solve(edges, n)
        print(solution)
    
main()
