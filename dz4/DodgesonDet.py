def swappedLines(mx) :
    for i in range(1,len(mx)) :
        if mx[i][0] != 0 :
            mx[0], mx[i] = mx[i], mx[0]
            return True

    return False


def minor(mx,i,j) :
    sign = (-1) ** (i+j)
    return sign * (mx[0][0]*mx[i+1][j+1] - mx[0][j+1]*mx[i+1][0]) 

def det(A, n) :
    if n == 2:
        return minor(A,0,0)

    # needed for the case when lines were swapped
    sign = 1

    if A[0][0] == 0 :
        if not swappedLines(A) :
            return 0
        sign = -1

    # condensate A
    B = []
    for i in range(n-1) :
        line = []
        for j in range(n-1) :
            line.append(minor(A,i,j))
        B.append(line)

    return sign * det(B,n-1) // A[0][0]**(n-2)


# MAIN

line = list(eval(input()))

n = len(line)

matrix = []
matrix.append(line)
for i in range(n-1) :
    matrix.append(list(eval(input())))

print(det(matrix,n))


#import numpy
#print('{0:.2f}'.format(numpy.linalg.det(numpy.array(matrix))))