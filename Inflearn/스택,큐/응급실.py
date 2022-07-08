from collections import deque

n,m = map(int,input().split())
arr = list(map(int,input().split()))

Q = deque([(idx,val) for idx,val in enumerate(arr)])
cnt = 0

while 1:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m :
            break
print(cnt)