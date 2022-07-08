import sys


n = int(input())
arr = list(map(int,input().split()))

half = sum(arr) / 2

def DFS(x,sum):
    global half
    
    if x > n-1:
        return
    
    if sum > half:
        return
    elif sum == half:
        print("YES")
        sys.exit(0)
    
    DFS(x+1,sum+arr[x])
    DFS(x+1,sum)
    
DFS(0,0)
print("NO")