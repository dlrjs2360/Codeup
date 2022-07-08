# 아주 중요한 문제.

def DFS(L,s):
    global cnt
    if L == m:
        for i in res:
            print(i,end=' ')
        cnt += 1
        print()
    else:
        for i in range(s,n+1):
            res[L] = i
            DFS(L+1,i+1)

n,m = map(int,input().split())
res = [0] * (m+1)
cnt = 0
DFS(0,1)
print(cnt)