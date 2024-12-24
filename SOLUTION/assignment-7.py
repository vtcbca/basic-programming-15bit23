from itertools import combinations
def triangle(n):
    for i in range(1, n+1):
        print(*combinations(range(1, i+1), i))