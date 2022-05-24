n = int(input())

k = []
k.append(0) 
k.append(1)


for i in range(2,n+1):
    k.append(k[i-1] + k[i-2]) 
    
print(k[n])