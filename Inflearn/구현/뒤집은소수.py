n = int(input())
arr = list(map(int,input().split()))

def is_reverse_prime(num):
    temp = num
    rvs = 0
    
    while(1):
        if temp < 1:
            break;
        dv = temp % 10
        temp = temp // 10
        rvs = rvs * 10 + dv
        
    if rvs == 1:
        return False
    
    for i in range(2,rvs):
        if rvs % i == 0:
            return False
    
    return rvs

for i in arr:
    if is_reverse_prime(i)!= False:
        print(is_reverse_prime(i), end=" ")