n = int(input())
m = int(input())

arr = []
for _ in range(m):
    arr.append(list(map(int,input().split())))
    
start, end = map(int,input().split())

temp = 0
distance = [[0] * n for _ in range(n)]

# print(start,end)

for i in arr:
    temp[i[0]][i[1]] = i[2]

def dfs(arr, start, end) :
    global temp
    global result
    
    for i in arr:
        if i[0] == start:
            print("start="+str(start))
            print("end="+str(end))
            print("temp="+ str(temp))
            if i[1] == end:
                temp[start][end] = 
                temp = 0
            else:
                dfs(arr,i[1],end)
                
        
        
dfs(arr,start,end)

print(result)