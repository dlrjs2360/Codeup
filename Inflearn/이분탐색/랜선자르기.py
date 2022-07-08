k, n = map(int,input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

lt = 0
rt = max(arr)
res = 0
def count(len) :
    count = 0
    for v in arr:
        count += v // len
    return count

while(lt<=rt) :
    mid = (lt+rt) // 2
    if count(mid) >= n :
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
    
print(res)



