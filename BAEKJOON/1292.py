s,e = map(int,input().split(' '))

sum = 0

arr = []

for i in range(1000):
    for j in range(i):
        arr.append(i)
        if len(arr) >= 1000:
            break

arr.insert(0,0)

for k in range(e-s+1):
    sum += arr[s+k]
    
print(sum)
    