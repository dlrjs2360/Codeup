k = int(input())
a = list(map(int,input().split()))
S = sum(a)
res = set()

def DFS(L,sum):
    global res
    if L == k:
        if 0<sum<=S:
            res.add(sum)
        
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum-a[L])
        DFS(L+1,sum)

DFS(0,0)
print(S-len(res))