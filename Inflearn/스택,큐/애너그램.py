a = list(input())
b = list(input())


# 일반 리스트
# for x in a:
    # if x in b:
    #     b.remove(x)
    # else :
    #     print('NO')
    #     break

# if len(b) == 0:
#     print('YES')
# else:
#     print('NO')



# 딕셔너리 해쉬
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x,0) + 1 # x의 값이 있다면 그 값에 1을 더하고 없다면 0에다 1을 더한다.
for x in b:
    str2[x] = str2.get(x,0) + 1
    
for i in str1.keys():
    if i in str2.keys():
        if str1[i]!= str2[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YES')