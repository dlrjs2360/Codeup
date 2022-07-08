n = int(input())
a = list(map(int,input().split()))
m = int(input())
res = 2147000000
a.sort(reverse=True)

def DFS(sum,cnt):
    global res
    
    if cnt > res:
        return
    if sum > m:
        return
    elif sum == m:
        res = min(res,cnt)
    else:
        for k in a:
            DFS(sum+k,cnt+1)
            
DFS(0,0)
print(res)