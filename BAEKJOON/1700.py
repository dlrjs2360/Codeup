n,k = map(int,input().split())
arr = list(map(int,input().split()))

stack = []
count = 0

for i in arr:
    if len(stack) == n:
        break
    
    if i not in stack:
        stack.append(i)
        count += 1
        # print(stack)
    
k2 = k - count

print(stack)
# 세개씩 묶어낼려고 함
# 생각해야하는 경우
# 1. temp에 담을 3개의 원소가 부족한 경우
# 2. temp에 같은 원소가 담겨서 여러번 안바꿔도 되는 경우
# 3. temp에 담길 원소와 이미 stack중에 같은 것이 있는 경우
# 4. 다음3개중에 바꿔야할 원소가 1개, 2개인데 다다음턴에 사용할 원소이 현재 #     스택에 있는 경우 - 이미 있는 코드중에 뺼 것들을 정한다

    
# arr에서 3개씩 가져와서 비교해야 한다.

# 아직 내가 도전할 수준이 아닌가보다... 흑흑