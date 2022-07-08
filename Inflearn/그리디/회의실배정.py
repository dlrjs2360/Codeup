n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[1])
ep = 0
cnt = 0

for conv in arr:
    if conv[0] >= ep:
        ep = conv[1]
        cnt += 1
    
print(cnt)