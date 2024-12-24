def fibonacci(n):
    a, b = 0, 1
    fib = [a]
    for _ in range(n - 1):
        fib.append(b)
        a, b = b, a + b
    return fib