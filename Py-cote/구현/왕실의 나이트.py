j = input()
row = int(j[1])
column = int(ord(j[0])) - int(ord('a')) + 1
print(row, column)

step = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result = 0

for i in step:
    nextrow = row + i[1]
    nextcolumn = column + i[0]
    if 0 < nextrow <=8 and 0 < nextcolumn <=8:
        result += 1
        
print(result)
 