from typing import List

"""
There's a stack of NN inflatable discs, with the iith disc from the top having
an initial radius of RiRi​ inches.

The stack is considered unstable if it includes at least one disc whose radius
is larger than or equal to that of the disc directly under it. In other words,
for the stack to be stable, each disc must have a strictly smaller radius than
that of the disc directly under it.

As long as the stack is unstable, you can repeatedly choose any disc of your
choice and deflate it down to have a radius of your choice which is strictly
smaller than the disc’s prior radius. The new radius must be a positive integer
number of inches.

Determine the minimum number of discs which need to be deflated in order to
make the stack stable, if this is possible at all. If it is impossible to
stabilize the stack, return −1−1 instead.

Discussion:

We have to inspect all discs.

One approach would be:
- For each value x from R from index i=1..(N-1)
  - If x is strictly greater than previous value, continue
  - Otherwise need to try to deflate previous values
    - Keep moving back towards index i, deflating until either
      - Deflating resulting in disc size = 0 => return -1
      - Current disc is already greater than previous disc => break
    - Count number of deflations

Optimization: Work backwards, since the last disc has to be strictly greater
than all the others.

Optimization 2: If size diff between last disc and first disc is greater than
N - 1, can't possibly deflate other discs to fit. (not implemented here)

Time:
- O(n) to visit all discs
- O(1) to deflate next disc if needed
- => O(n)

Space:
- => O(1) to track number of deflations
"""
def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    """
    >>> getMinimumDeflatedDiscCount(5, [2, 5, 3, 6, 5])
    3
    >>> getMinimumDeflatedDiscCount(3, [100, 100, 100])
    2
    >>> getMinimumDeflatedDiscCount(4, [6, 5, 4, 3])
    -1
    """
    numDeflations = 0
    for i in range(N - 1, 0, -1):
        if R[i] > R[i - 1]:
            # this disc is strictly greater than previous, so continue
            continue
        else:
            # this disc is not strictly greater than prev, so try to deflate prev
            if R[i] == 1:
                # can't deflate previous disc
                return -1
            else:
                R[i - 1] = R[i] - 1
                numDeflations += 1
    return numDeflations

if __name__ == '__main__':
    import doctest
    doctest.testmod()
