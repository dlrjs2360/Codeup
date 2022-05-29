n = int(input())

a = list(map(int,input().split(" ")))

def isDecimal(k):
    if k == 1 :
        return False
    else :
        for i in range(2,k):
            if k % i == 0:
                return False
        return True

count = 0

for j in a:
    if isDecimal(j):
        count += 1

print(count)