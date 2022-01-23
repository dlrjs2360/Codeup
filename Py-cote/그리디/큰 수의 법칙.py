# 입력 조건

# 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며 각 자연수는 공백으로 구분

# 둘째줄에 N개의 자연수가 주어짐. 각 자연수는 공백으로 구분. 단, 각각의 자연수는 1이상 10000이하의 수로 주어짐

# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건

# 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력

N,M,K = map(int,input().split())

a = list(map(int,input().split()))

a.sort(reverse=True)

c = 0
s = 0
i = 0

for _ in range(M): # c를 더해서 비교하는 것보단 K를 줄이는 것이 낫다.
    if c <= K-1 :
        s += a[0]
        c += 1
    else :
        s += a[1]
        c = 0
print(s)


###################### 책 소스 코드 ##########################

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력