def alphabet_pattern(n):
    for i in range(1, n+1):
        print(*map(chr, chain(range(ord('A'), ord('A') + i), 
                             range(ord('A') + i - 2, ord('A') - 1, -1))))