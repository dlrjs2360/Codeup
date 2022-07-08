n,m = map(int,input().split())
a = []
cnt = 0
for _ in range(m):
    a.append(list(map(int,input().split())))
    
    g = [[0]*(n+1) for _ in range(n+1)]

for x in a:
    g[x[0]][x[1]] = 1
ch = [0] * (n+1)
def DFS(s):
    global cnt
    if s == 5:
        print(path)
        cnt += 1
         
    else:
        for i in range(1,n+1):
            if g[s][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0
                
path = []
path.append(1)
ch[1] = 1
DFS(1)
print(cnt)

