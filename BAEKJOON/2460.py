arr = []
Nrr = []

Sum = 0

for i in range(10):
    N = list(map(int,input().split()))
    Nrr.append(N)

for j in Nrr:
    Sum = Sum - j[0] + j[1]
    arr.append(Sum)
    
print(max(arr))