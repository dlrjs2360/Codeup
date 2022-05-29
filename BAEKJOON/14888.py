# 재귀함수

# -- 입력값 설정 -------------------------------------

import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

a, b, c, d = map(int, input().split())

# -- 최대 최소 설정 ------------------------------------
max_ans, min_ans = -1e9,1e9
# max_ans, min_ans = -sys.maxsize -1, sys.maxsize

# -- 함수 설정 ------------------------------------------

def solution(num, idx, add, sub, mul, div):
    global max_ans, min_ans
    if idx == N:
        # max함수는 최대를 구하는 것이지만 max_ans를 통해 최소를 제한한다.
        # min함수는 최소를 구하는 것이지만 min_ans를 통해 최대를 제한한다.
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return 
    
    #  각 if문에서 4가지 시작루트를 설정해서 모든 경우의 수를 다 돌리고
    #  global 변수 max_ans와 min_ans를 통해 최대 최소를 구한다.
    if add > 0:
        solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        solution(num * nums[idx], idx + 1, add, sub , mul -1, div)
    if div > 0:
        solution(int(num / nums[idx]), idx + 1, add, sub, mul, div -1)


solution(nums[0], 1, a, b, c, d)
print(max_ans)
print(min_ans)