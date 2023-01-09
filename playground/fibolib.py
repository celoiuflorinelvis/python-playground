
def fibo3(a, b, n):
    if n > 0:
        return fibo3(b, a + b, n - 1)
    else:
        return a

def fibo(n):
    return fibo3(0, 1, n)

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
