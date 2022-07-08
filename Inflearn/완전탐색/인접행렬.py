n,m = map(int,input().split())
a = []
for _ in range(m):
    a.append(list(map(int,input().split())))


g = [[0]*(n+1) for _ in range(n+1)]

for x in a:
    g[x[0]][x[1]]= x[2]
for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j],end=' ')
    print()
    


