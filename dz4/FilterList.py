lst = list(map(int, input().split(',')))

m, n = map(int, input().split(','))

del lst[0::m]

lst = [elem for elem in lst if elem % n != 0]

print(lst)

"""
ans = []
i = 0
for elem in lst :
    if i % m != 0 and elem % n != 0 :
        ans.append(elem)

    i += 1;

print (ans)
"""