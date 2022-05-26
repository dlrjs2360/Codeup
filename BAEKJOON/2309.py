arr = []

for i in range(9):
    n = int(input())
    arr.append(n)

for v in arr:
    sumA = 0
    arr2 = arr.copy()
    arr2.remove(v)
    
    for k in arr2:
        arr3 = arr2.copy()
        arr3.remove(k)
        sumA = sum(arr3)
       
        if sumA == 100:
            
            break
    if sumA == 100:
        break
        
arr3.sort()


for j in arr3:
    print(j)