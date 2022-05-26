n,m = map(int,input().split())

def getMax(k):
    arr = []
    for i in range(1,k+1):
        if k % i == 0 :
            arr.append(i)
    return arr

MaxN = getMax(n)
MaxM = getMax(m)

arrG = []

for i in MaxN:
    for j in MaxM:
        if i == j:
            arrG.append(j)

MaxR = max(arrG)

c1 = 1
while 1:
    minN = n * c1
    c2 = 1
    minM = 0
    while minN > minM:
        minM = m * c2
        c2 += 1
    if minN == minM:
            break
    c1 += 1
    
MinR = minN

print(MaxR)
print(MinR)