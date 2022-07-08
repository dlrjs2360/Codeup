n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
res = 0
def DFS(L,sum,time):
    global res
    if time > m:
        return
    if L == n:
        res = max(res,sum)
    else:
        DFS(L+1,sum+a[L][0],time+a[L][1])
        DFS(L+1,sum,time)
DFS(0,0,0)
print(res)