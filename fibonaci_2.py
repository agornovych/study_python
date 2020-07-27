def fibo(n):
    result=[1,1]
    cur = next = 1
    if n==1:
        return 1
    else:
        i = 2
        while i in range (2, n):
            cur, next = next, cur + next
            i+=1
            result.append(next)
        return result

n = int(input("How many Fibonacci numbers you want: "))
a = fibo(n)
print(f'Fibonacci from start to {n} is', a)
print(f'Value of Fibbonachi number {n} is', a[-1])

