
# 중복되는 값들을 배열에 저장한다?
# k값에 따라 중복되지 않아도 읽을 수 있어야 한다.
# k가 5보다 anta와 tica를 읽을 수 있는 최소 개수 5가 되지 않으면 0을 출력한다.

n, k = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(input().split('')))

result = 0

if k < 5:
    result = 0
    
print(result)
print(arr)