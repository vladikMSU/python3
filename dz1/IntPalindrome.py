number = eval(input())

num_cont, pow_of_ten = number, 0
while num_cont // 10 :
    pow_of_ten += 1
    num_cont //= 10

#print (pow_of_ten)

while number :
    if number // 10 ** pow_of_ten != number % 10 :
        print ('NO')
        break
    number %= 10 ** pow_of_ten
    number //= 10
    pow_of_ten -= 2

else :
    print ('YES')