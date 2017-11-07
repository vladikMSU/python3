def pargen(n) :
    v = yield 100500
    for i in range(n) :
        v = yield i+v
    yield -100500

gen = pargen(4)
c = next(gen)
print("Start:",c)
while True:
    c = gen.send(c%2)
    print(c)
