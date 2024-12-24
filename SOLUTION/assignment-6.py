from itertools import product
def star_pattern(n):
    for i in range(1, n+1):
        print(*[j for j in product(["*"], repeat=i)])