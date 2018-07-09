n = eval(input())

for i in range(2,1001) :
    tmp = i * i
    while tmp < n :
        tmp *= i

    if tmp == n :
        print('YES')
        break

else :
    print('NO')
