n = int(input())

d = [0] * 100

# (1,1) (2,3) (3,5) (4,11)
# 점화식 : a[i] = a[i-1] + a[i-2] * 2

d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = (d[i-1]+d[i-2] * 2) % 706796
    # 너무 큰 수는 안나오게 하기 위해서 나머지 식 추가
    
print(d[n])