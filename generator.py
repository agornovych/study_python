a = [1,545,45,88,99,4587,1]
print(a)


def mult(n):
    return n**3


c = list(map(mult, a))
print(c)


b = list(map(lambda x: x**2 , a))
print(b)

def gena(n):
    result = []
    for i in range(n):
        if i%2 ==0:
            result.append(i)
    return result


e = list(filter(gena, ))



