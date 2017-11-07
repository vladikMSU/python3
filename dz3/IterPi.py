# generate the next approximation of PI
# according to the value of cur_val
def createPIgen() :
    cur_val = 0
    i = 0
    sign = 1
    
    while True :
        denom = 2*i+1
        cur_val += sign*(4/denom)
        sign *= -1
        i += 1

        yield cur_val


eps = float(input())

pigen = createPIgen()

i = 1
cur_val = next(pigen)

while True:
    next_val = next(pigen)
    if abs(next_val - cur_val) < eps :
        print(i)
        break;

    cur_val = next_val
    i += 1