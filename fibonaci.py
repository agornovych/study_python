# fibonacci function
import time


def fib():
    n = int(input("How many Fibonacci numbers you want: "))
    result = []
    fib1 = fib2 = 1
    if n == 0:
        print("Incorrect value")
    elif n == 1:
        result.append(fib1)
    else:
        result.append(fib1)
        result.append(fib2)
        for i in range(n - 2):
            fib1, fib2 = fib2, fib1 + fib2
            result.append(fib2)
    return result[-1]


start_time = time.time()

a = fib()
print(a)

end_time = time.time()
delta = end_time-start_time
print(start_time, end_time, delta)