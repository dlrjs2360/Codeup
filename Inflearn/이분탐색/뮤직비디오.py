n,m = map(int,input().split())
mus = list(map(int,input().split()))

def inDVD(len):
    cnt = 1
    k = len
    for i in mus:
        if k >= i:
            k = k - i
        else:
            cnt += 1
            k = len - i
            print('-------')
        print('들어온 값: ',i,' 남은 길이: ',k,' 카운팅: ',cnt)
        
    return cnt


lt = 1
rt = sum(mus)
maxx = max(mus)
res = 0
while(lt <= rt) :
    mid = (lt+rt) // 2
    v = inDVD(mid)
    if mid >= maxx and v <= m:
        res = mid
        rt = mid - 1
        print('mid: ', mid, ' cnt: ',v)
        print('---------------------------------------------')
    else:
        print('mid: ', mid, ' cnt: ',v)
        lt = mid + 1
        
print(res)