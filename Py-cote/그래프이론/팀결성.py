
def findTeam(t,x):
    if t[x] != x:
        t[x] = findTeam(t,t[x])
    return t[x]

def uninTeam(t,a,b):
    a = findTeam(t,a)
    b = findTeam(t,b)
    if a < b:
        t[b] = a
    else:
        t[a] = b

n,m = map(int,input().split())

t = [0] * (n+1)

for i in range(0,n+1):
    t[i] = i

for i in range(m):
    
    k, a, b = map(int,input().split())
    
    if k == 0:
        uninTeam(t,a,b)
    elif k == 1:
        if findTeam(t,a) == findTeam(t,b):
            print("Yes")
        else:
            print("No")
        