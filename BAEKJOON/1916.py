n = int(input())
m = int(input())

arr = []
for _ in range(m):
    arr.append(list(map(int,input().split())))
    
start, end = map(int,input().split())

result = 9999
temp = []

# print(start,end)

def dfs(arr, start, end) :
    global temp
    global result
    
    for i in arr:
        if i[0] == start:
            print("start="+str(start))
            print("end="+str(end))
            temp += i[2]
            print("temp="+ str(temp))
            if i[1] == end:
                result = min(result, temp)
                temp = 0
            else:
                dfs(arr,i[1],end)
                
        
        
dfs(arr,start,end)

print(result)