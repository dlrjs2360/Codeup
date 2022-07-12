n = int(input())


# 다른 모든 회원과 친구이면 1
# 다른 모든 회원이 친구이거나 친구의 친구이면 2점
# 다른 모든 회원이 친구이거나 친구의 친구, 친구의 친구의 친구이면 3점
# 친구의 친구의 친구의 친구이면 4점
# 친구의 친구의 친구의 친구의 친구이면 5점..

dis = [[100]*(n+1) for _ in range(n+1)]
res = [0]*(n+1)

for i in range(1,n+1):
    dis[i][i] = 0

while(1):
    a,b = map(int,input().split())
    if a == -1:
        break
    dis[a][b] = 1
    dis[b][a] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])

for i in range(1,n+1):
    maxv = 0
    for j in range(1,n+1):
        if dis[i][j] == 0:
            continue
        maxv = max(maxv,dis[i][j])
    res[i] = maxv
# print('------------------------------------')
# for i in range(1,n+1):
#     print(res[i],end= ' ')
# print()
# print('====================================')
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(dis[i][j],end = ' ')
#     print()

resv = min(res[1:n+2])
cnt = 0
ress = []
for i in range(1,n+1):
    if res[i] == resv:
        cnt += 1
        ress.append(i)

print(resv,cnt)
for i in ress:
    print(i,end= ' ')
