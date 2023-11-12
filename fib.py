def fib(n):
    if n==2:
        print(0)
        print(1)
    else:
        fib(n-1)
        print(n)
fib(5)
