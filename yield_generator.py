def gen_num(n):
    for i in range(1, n+1):
        yield 2**i


a = gen_num(1000)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

