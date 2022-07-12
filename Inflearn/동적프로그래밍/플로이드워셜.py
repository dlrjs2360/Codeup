n,m = map(int,input().split())
dis = [[500] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dis[i][i] = 0
    
for _ in range(m):
    a,b,c = map(int,input().split())
    dis[a][b] = c
    
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            dis[a][b] = min(dis[a][b], dis[a][i]+dis[i][b])
            
print('-------------------------------')
for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j] == 500:
            print('M',end = ' ')
        else:
            print(dis[i][j],end = ' ')
    print()
        