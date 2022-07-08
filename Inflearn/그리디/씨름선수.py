n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(x[0],x[1]),reverse=True)

largest = 0
cnt = 0

for ps in arr:
    if ps[1] > largest:
        cnt += 1
        largest = ps[1]
        
print(cnt)