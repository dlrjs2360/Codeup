n,c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr)

rt = max(arr)
lt = 0
res = 0

def putt(leng):
    pres = arr[0]
    cnt = 1
    for i in arr[1:]:
        if pres+leng <= i:
            pres = i
            cnt += 1
        else :
            continue
    print('cnt: ',cnt)
    return cnt

while lt <= rt:
    mid = (lt+rt) // 2
    print('mid: ',mid, ' (lt,rt): (',lt,rt,')' )
    if putt(mid) <= c:
        res = mid
        rt = mid - 1
    else :
        lt = mid + 1
    
    # if putt(mid) >= c:
    #     res = mid
    #     lt = mid + 1
    # else :
    #     rt = mid - 1
    
        
print(res)