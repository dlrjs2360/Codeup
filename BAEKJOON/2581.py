m = int(input())
n = int(input())

def isDeciman(k):
    if k == 1:
        return False
    
    for j in range(2,k):
        if k % j == 0:
            return False
    return True

arr = []
for i in range(m,n+1):
    if isDeciman(i):
        arr.append(i)

if arr == []:
    print(-1)
    
else:
    print(sum(arr))
    print(min(arr))
