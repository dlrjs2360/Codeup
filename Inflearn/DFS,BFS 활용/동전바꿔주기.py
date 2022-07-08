t = int(input())
k = int(input())
p = []
n = []
cnt = 0
tmp = []
res = []
for i in range(k):
    a,b = map(int,input().split())
    p.append(a)
    n.append(b)

def DFS(i,sum):
    global cnt
    if sum > t or i > k:
        return
    if i == k:
        if sum == t:
            if set(tmp) not in res:
                res.append(set(tmp))
                cnt += 1
    else:
        if n[i] > 0:
            n[i] -= 1
            tmp.append(p[i])
            DFS(i+1,sum+p[i])
            DFS(i,sum+p[i])
            n[i] += 1
            tmp.pop()
        DFS(i+1,sum)
        
DFS(0,0)
print(cnt)
print(res)
