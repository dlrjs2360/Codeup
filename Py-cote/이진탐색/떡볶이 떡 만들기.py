n,m = map(int,input().split())

a = list(map(int,input().split()))

def summer(a,t):
    if t < m:
        return None
    s = 0
    for i in a:
        if i < t:
            continue
        else:
            s = s + (i - t)
    return s

t = 0

while(True):
    result = summer(a,t)
    if result == m:
        print(t)
        break
    t += 1
# 이 코드는 적어도 m만큼의 떡을 얻을 수 있는 최대의 길이를 구하지 않고 딱 m만큼의 떡을 얻을 수 있는 길이를 구하게 됨.
    
# 이진탐색 --------------------------------------------

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):

    total = 0 
    mid = (start+end)//2

    for x in array:
        if x > mid:  
            total += x - mid   

    if total < m:    
        end = mid - 1

    else:  

        result = mid
        start = mid + 1   

print(result)