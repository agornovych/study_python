def fibon(n):
    if n == 0:
        print("Incorrect input")
    elif n <= 2:
        return 1
    else:
        return fibon(n-1) + fibon(n-2)


n = int(input("How many Fibonacci numbers you want: "))
print(fibon(n))