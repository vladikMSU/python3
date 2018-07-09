seq = set(eval(input()))
dic = {key: False for key in seq}

max_elem = max(seq)

ans = 0

i = 1
sqr_i = i*i
sqrs_sum = sqr_i*3
while sqrs_sum <= max_elem :
    j = i
    sqr_j = j*j
    while sqrs_sum <= max_elem :
        k = j
        while sqrs_sum <= max_elem :
            if sqrs_sum in dic and not dic[sqrs_sum] :
                dic[sqrs_sum] = True
                ans += 1
            k += 1
            sqrs_sum = sqr_i + sqr_j + k*k
        j += 1
        sqr_j = j*j
        sqrs_sum = sqr_i + sqr_j*2
    i += 1
    sqr_i = i*i
    sqrs_sum = sqr_i*3

print (ans)