c,n = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
result = 0
total = sum(arr)
def DFS(i,sum,tsum):
    
    global result
    global total
    
    if (sum + total - tsum < result) or (sum > c):
        return

    if i == n :
        if sum > result:
            result = sum
    else:
        DFS(i+1,sum+arr[i],tsum+arr[i])
        DFS(i+1,sum,tsum + arr[i])
    
DFS(0,0,0)

print(result)