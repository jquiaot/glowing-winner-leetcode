import sys

def solve(n: int) -> list[int]:
    """
    Since we need to generate all the values generated when
    executing the weird algorithm, we really don't have
    a choice I think in just coding it up as written.

    1. Start with n
    2. Until n == 1
       a. If n is odd, multiply by 3 and add 1
       b. If n is even, divide by 2
    3. Print out all generated numbers.
    """
    values = []
    i = n
    values.append(n)
    while i > 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = i * 3 + 1
        values.append(i)
    return values

if __name__ == '__main__':
    line = sys.stdin.readline()
    n = int(line)
    res = solve(n)
    print(' '.join([str(i) for i in res]))
