n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
a.sort(key=lambda x:x[0],reverse=True)
a.insert(0,[0,0,0])

dy = [0] * (n+1)
dy[1] = a[1][1]
res = dy[1]

for i in range(2, n+1):
    maxx = 0
    for j in range(i-1,0,-1):
        if a[j][2] > a[i][2] and dy[j] > maxx:
            maxx = dy[j]
    dy[i] = maxx + a[i][1]
    res = max(res,dy[i])
# print(a)
# print(dy)
print(res)
            