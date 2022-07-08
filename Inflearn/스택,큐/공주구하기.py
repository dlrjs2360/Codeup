from collections import deque

n,k = map(int,input().split())

dq = list(range(1,n+1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()
    # print(dq)
        
print(dq.pop())