n = int(input())
coin = list(map(int,input().split()))
m = int(input())

dy = [1000] * (m+1)
dy[0] = 0
for i in coin:
    for j in range(i,m+1):
        dy[j] = min(dy[j],dy[j-i]+1)
        
print(dy[m])


