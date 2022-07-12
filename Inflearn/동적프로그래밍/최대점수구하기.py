# 제한시간 m을 기준으로 생각하며 0~m까지 제한시간동안 풀수있는 최대가치를 갱신한다.

n,m = map(int,input().split())
res = 0
dy = [0] * (m+1)
for _ in range(n):
    s,t = map(int,input().split())
    for j in range(t,m+1):
        dy[j] = max(dy[j],dy[j-t]+s)
# print(dy)
print(dy[m])