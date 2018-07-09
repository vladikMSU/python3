def getGen(s, d, m, n) :
    prev, curr = None, s
    while prev != curr :
        yield curr
        prev, curr = curr, (curr//d + m) if not curr % d else (curr + n)

def catgen(fours) :
    for four in fours :
        yield from getGen(*four)

fours = eval(input())

k = int(input())

for i, elem in enumerate(catgen(fours)) :
    if i == k :
        print(elem)
        break

else :
    print('NO')