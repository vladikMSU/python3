def createGenerator(v) :
    for i in range(0, len(v)) :
        for j in range(0, len(v)) :
            if v[j] <= v[i]:
                yield v[j]

v = list(map(int, input().split(',')))
N = int(input())

gen = createGenerator(v)

try:
    ans = 1
    for i in range(0, N+1):
        ans = next(gen)
    print (ans)

except StopIteration:
    print ('NO')