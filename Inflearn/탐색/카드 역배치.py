arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

inp = []
for i in range(10):
    inp.append(list(map(int,input().split())))


def change(arr):
    # for i in range(len(arr)//2):
    #     arr[i], arr[-1-i] = arr[-1-i],arr[i]
    arr = arr[::-1]
    return arr

for v in inp:
    arr[v[0]-1 : v[1]] = change(arr[v[0]-1 : v[1]])
    
# print(inp)
for i in arr:
    print(i,end=" ")