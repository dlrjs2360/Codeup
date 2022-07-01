n = int(input())
arr = list(map(int,input().split()))
avg = int(sum(arr)/n+0.5) # 문제없이 반올림하는 방법
min = float('inf')
idx = 0
res = 0
for i, v in enumerate(arr):
    mn = abs(avg - v)
    if mn < min:
        min = mn
        idx = i+1
        res = v
    elif mn == min:
        if v > res:
            idx = i+1
            res = v
print(avg, idx)