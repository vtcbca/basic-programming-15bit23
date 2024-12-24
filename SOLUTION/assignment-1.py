def factorial_generator(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

def factorial(n):
    if n == 0:
        return 1
    return list(factorial_generator(n))[-1]