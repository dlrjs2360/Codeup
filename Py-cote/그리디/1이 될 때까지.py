n,k = map(int,input().split())
c = 0
while(n != 1):
    if n%k == 0:
        n = n // k
    else:
        n = n - 1
    c += 1
    
print(c)