
"""
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum
to n.

A perfect square is an integer that is the square of an integer; in other
words, it is the product of some integer with itself. For example, 1, 4, 9,
and 16 are perfect squares while 3 and 11 are not.
"""
class Solution:
    """
    Commentary:

    Intuitively, I want to do something where I would calculate the best
    way to reach some value k using perfect squares, where 1 <= k <= n.

    Some notable base cases and examples:
    - n=0 => [] (no possible way to reach 0 using perfect squares)
    - n=1 => [1] (only one possibly way to reach 1 using perfect squares)
    - n=4 => [4] ([1,1,1,1] is too long)
    - n=5 => [1,4] ([1,1,1,1,1] is too long)
    - n=12 => [4,4,4] ([9,1,1,1] is too long)

    Strategy/algorithm:
    - List of lists of squares from indexes 0..n to keep track of best list
      of squares to reach index i, 0 <= i <= n
    - Base case 0 => []
    - Fill in perfect squares from 1..n i.e. squares[sq] = [sq] just the
      square itself (reaches in a single step)
    - For numbers from 1..n, try to extend squares[i] to squares[i+1..n]
      by adding squares to it if possible; if the target squares list doesn't
      exist, then the target squares list is the current squares list plus the
      new square; if the target squares list does exist, then it's the 
      min of cur squares list + 1 or the target squares list
    - Return squares[n]

    Analysis:

    Time complexity:
    - O(n) for calculating best squares for 0..n
    - m=sqrt(n) for attempting to extend lists from some value in n
    - => O(n*sqrt(n))

    Space complexity:
    - O(n) for storing intermediate best squares list from 0..n
    - O(n) for each list
    - O(n^2)
    """
    def numSquares(self, n: int) -> int:
        # lists of minimal set of perfect squares that sum to the index
        squares = [None for x in range(n + 1)]

        # base cases:
        # - squares[0] = [] (can't reach 0 so empty list)
        # - squares[1] = [1]
        squares[0] = []

        # fill in all squares
        for i in range(1, n + 1):
            sq = i ** 2
            if sq > n:
                break
            squares[sq] = [sq]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                sq = j ** 2
                if i + sq > n:
                    break
                else:
                    curSquares = squares[i]
                    targetSquares = squares[i + sq]
                    if targetSquares is None:
                        squares[i + sq] = [*curSquares, sq]
                    elif len(curSquares) + 1 < len(targetSquares):
                        squares[i + sq] = [*curSquares, sq]
            i += 1
        return squares[n]


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()

    s = Solution()
    print(s.numSquares(4))
    print(s.numSquares(12))
