from collections import deque
Max = 10000
ch = [0] * (Max+1)
dis = [0] * (Max+1)
s,e = map(int,input().split())
dq = deque()
ch[s] = 1
dq.append(s)

while dq:
    now = dq.popleft()
    if now == e:
        break
    for next in (now-1,now+1,now+5):
        if 0 < next < Max:
            if ch[next] == 0:
                dq.append(next)
                dis[next] = dis[now] + 1
                ch[next] = 1
        
# print(dis)
print(dis[e])