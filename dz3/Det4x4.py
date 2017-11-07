from itertools import permutations

def parse_tuple(str) :
    return tuple(map(int,str[1:-1].split(',')))

def parse_tuples(str) :
    commas_num = 0
    for i,ch in enumerate(str) :
        if ch == ',' :
            commas_num += 1
            if commas_num == 4 :
                return [ parse_tuple(str[:i]) ] + parse_tuples(str[i+2:])

    return [ parse_tuple(str) ]

def inversions(permutation) :
    invs_num = 0
    for i,x in enumerate(permutation):
        for y in permutation[i+1:] :
            if x > y :
                invs_num += 1

    return invs_num

# lines of 4x4 matrix
lines = parse_tuples(input())

# determinant
det = 0

indexes = [1, 2, 3, 4]
for ind_perm in permutations(indexes) :
    # list of elements from each line with indexes frim ind_perm
    elem_perm = map(lambda tup : tup[1][tup[0]-1], zip(ind_perm,lines))
    
    # initialize with the signature of ind_perm
    prod = (-1)**inversions(ind_perm)
    
    for x in elem_perm :
        prod *= x

    det += prod

print (det)