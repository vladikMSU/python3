x_center, y_center, radius = eval(input())

x, y = eval(input())
while x != 0 or y != 0 :
    if (x - x_center) ** 2 + (y - y_center) ** 2 > radius ** 2 :
        print('NO')
        break
    x, y = eval(input())

else :
    print('YES')