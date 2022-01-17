n = int(input())
na = list(map(int,input().split()))
m = int(input())
ma = list(map(int,input().split()))

for i in range(m):
    if ma[i] in na:
        ma[i] = 1
    else:
        ma[i] = 0
        
for i in ma:
    print(i, end=' ')
    
#메모리초과로 못품...