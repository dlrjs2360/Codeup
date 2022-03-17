INF = int(1e9)

n,m,c = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x][y] = z

for a in range(n+1):
    for b in range(n+1):
        if(a==b):
            graph[a][b] = 0

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])
            
count = [0] * (n+1)
maxcount = [0] * (n+1)

for a in range(n+1):
    for b in range(n+1):
        if graph[a][b] < INF:
            count[a] = count[a] + 1
            maxcount[a] = max(maxcount[a], graph[a][b])
            
print(count[c] - 1, maxcount[c]) # 시작노드는 제외해야하므로 -1이 필요하다