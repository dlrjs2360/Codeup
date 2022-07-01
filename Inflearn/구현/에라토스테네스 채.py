n = int(input())

arr = [0] * (n+1)
count = 0

for i in range(2,n+1):
    if arr[i] == 0:
        count += 1
        for j in range(i,n+1,i):
            arr[j] = 1
            
print(count)

# 소수를 찾아서 소수의 배수들은 모두 제외시키는 방식이다.