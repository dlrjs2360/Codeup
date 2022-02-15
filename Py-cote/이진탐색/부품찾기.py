# 이진탐색(재귀함수) -----------------------------------------------
n = int(input())

a1 = list(map(int,input().split()))

n = int(input())

a2 = list(map(int,input().split()))

def binary_search(a,t,start,end):
    if start>end:
        return None
    mid = (start + end) // 2
    if a[mid] == t:
        return mid
    elif a[mid] > t:
        return binary_search(a,t,start,mid-1)
    else:
        return binary_search(a,t,mid+1,end)

a3 = []
for i in a2:
    result = binary_search(a1,i,0,n)
    if result == None:
        a3.append('no')
    else:
        a3.append('yes')
print(a3)


# 계수정렬----------------------------------------------------

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
# 집합자료형--------------------------------------------------

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')