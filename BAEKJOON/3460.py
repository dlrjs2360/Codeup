T = int(input())
N = list(map(int,input().split()))

BN = []

for i in N:
    BN.append(int(bin(i).split('0b')[1]))
    
for i in BN:
    arr = []
    j = 0
    while i >= 1:
        if i % 10 == 1 :
            arr.append(j)
        j += 1
        i = int(i / 10)
    for k in arr:
        print(k, end="")
        print(" ",end="")
    print("")
        
    
