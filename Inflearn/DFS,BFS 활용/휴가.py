
n = int(input())
a = []
a.append([0,0])
for _ in range(n):
    a.append(list(map(int,input().split())))
    
res = 0

def DFS(Day,sum):
    global res
    if Day == n+1:
        res = max(sum, res)
    else:
        if Day+a[Day][0] <= n+1:
            DFS(Day+a[Day][0],sum+a[Day][1])
        DFS(Day+1,sum)
        
DFS(1,0)
print(res)