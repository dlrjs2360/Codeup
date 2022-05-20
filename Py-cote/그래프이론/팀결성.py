
def findTeam(t,x):
    if t[x] != x:
        t[x] = findTeam(t,t[x])
    return t[x]
# 부모노드를 찾아서 반환한다. 

def uninTeam(t,a,b):
    a = findTeam(t,a)
    b = findTeam(t,b)
    if a < b:
        t[b] = a
    else:
        t[a] = b
# 부모노드를 같은 것으로 바꾼다.
# 경로는 문제가 되지 않는다.

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
        