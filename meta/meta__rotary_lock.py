from typing import List

import math

"""
You're trying to open a lock. The lock comes with a wheel which has the
integers from 11 to NN arranged in a circle in order around it (with integers
11 and NN adjacent to one another). The wheel is initially pointing at 11.

For example, the following depicts the lock for N=10N=10 (as is presented in
the second sample case).

It takes 11 second to rotate the wheel by 11 unit to an adjacent integer in
either direction, and it takes no time to select an integer once the wheel is
pointing at it.

The lock will open if you enter a certain code. The code consists of a sequence
of MM integers, the iith of which is CiCi​. Determine the minimum number of
seconds required to select all MM of the code's integers in order.

Please take care to write a solution which runs within the time limit.


Example moves:

Given N = 8

1-2 = 1
1-3 = 2
1-4 = 3
1-5 = min(2345, 8765) = 4
1-6 = min(23456, 876) = 3
1-7 = min(234567, 87) = 2
1-8 = min(2345678, 8) = 1

Given N = 7
1-2 = 1
1-3 = 2
1-4 = min(234, 7654) = 3
1-5 = min(2345, 765) = 3
1-6 = min(23456, 76) = 2
1-7 = min(234567, 7) = 1

So, can we say max difference should be floor(N/2) ?

What is fastest way then, given absolute difference in numbers?
- if x-y <= floor(N/2), use it
- if x-y > floor(N/2), then should be N-(x-y)

Time:
- O(n) to get through C
- O(1) for each calculation
- => O(n)

Space:
- => O(1) to keep track of time, prev, and maxDiff
"""
def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    """
    >>> getMinCodeEntryTime(3, 3, [1, 2, 3])
    2
    >>> getMinCodeEntryTime(10, 4, [9, 4, 4, 8])
    11
    """
    time = 0
    prev = 1
    maxDiff = N // 2
    for i in range(0, M):
        diff = abs(C[i] - prev)
        calcTime = 0
        if diff <= maxDiff:
            calcTime = diff
        else:
            calcTime = N - diff
        # print(f"From {prev} to {C[i]} = {calcTime}")
        time += calcTime
        prev = C[i]
    return time
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
