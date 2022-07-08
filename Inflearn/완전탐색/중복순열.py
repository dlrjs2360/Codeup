n,m = map(int,input().split())
cnt = 0
res = [0] * m
def DFS(x):
    global res
    global cnt
    if x == m:
        for i in res:
            print(i, end = " ")
        print()
        cnt += 1
    else:
        for i in range(1,n+1):
            res[x] = i
            DFS(x+1)
  
DFS(0)
print(cnt)
