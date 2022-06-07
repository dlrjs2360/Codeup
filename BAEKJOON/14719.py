h,w = map(int,input().split())

arr = list(map(int,input().split()))

block = [[0] * h for _ in range(w)]

result = 0

maxindex = 0

def rm3(block,j,k):
    if block[j][k] == 3:
        block[j][k] = 0
        rm3(block,j-1,k)
    else :
        return


for i in range(len(block)):
    for j in range(len(block[i])):
        if j+1 <= arr[i]:
            block[i][j] = 1
            

for i in range(len(block)-1):
    
    for k in range(len(block[i])):
        
        if block[i][k] == 0 and i > 0:
            if block[i-1][k] == 1 or block[i-1][k] == 3 :
                block[i][k] = 3
                maxindex = k
                
        if block[i+1][k] == 0 and i == len(block)-2:
            rm3(block,i,k)
        
result = 0
for k in block:
    result += k.count(3)

print(result)
                
                
# 모범답안
# h, w = map(int, input().split())
# world = list(map(int, input().split()))

# ans = 0
# for i in range(1, w - 1):
#     left_max = max(world[:i])
#     right_max = max(world[i+1:])

#     compare = min(left_max, right_max)

#     if world[i] < compare:
#         ans += compare - world[i]

# print(ans)