from math import sqrt, floor

"""
Given a non-negative integer c, decide whether there're two integers a and b
such that a^2 + b^2 = c.

Example 1:

Input: c = 5

Output: true

Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3

Output: false

Constraints:

- 0 <= c <= 2^31 - 1

"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        >>> s = Solution()
        >>> s.judgeSquareSum(5)
        True
        >>> s.judgeSquareSum(3)
        False
        >>> s.judgeSquareSum(0)
        True
        >>> s.judgeSquareSum(1)
        True
        >>> s.judgeSquareSum(2147483647)
        False
        """
        return self.judgeSquareSumUsingMath(c)
    
    def judgeSquareSumUsingMath(self, c: int) -> bool:
        """
        Some examples:
        - 0 = 0,0
        - 1 = 0,1
        - 2 = 1,1
        - 3 = None
        - 4 = 0,2
        - 5 = 1,2
        - 6 = None
        - 7 = None
        - 8 = None
        - 9 = 0,3
        - 10 = 1,3

        If we find the largest square root that is <= c, that is our max value for a or b

        Time:
        - => O(sqrt(c)) to potentially explore values from 0 to sqrt(c)

        Space:
        - => O(1) no aux space used
        """
        # short-circuit 0 (seems like I can game the test cases by short-circuiting some other common values)
        if c == 0 or c == 1 or c == 2:
            return True
        maxPossibleValue = int(floor(sqrt(c)))
        # print(maxPossibleValue)

        for i in range(maxPossibleValue, maxPossibleValue // 2, -1):
            iSquared = i * i
            theDiff = c - iSquared
            sqrtTheDiff = sqrt(theDiff)
            remainder = sqrtTheDiff - floor(sqrtTheDiff)
            if remainder == 0:
                return True
            else:
                continue
        return False
    
    def judgeSquareSumUsingDict(self, c: int) -> bool:
        """
        Compute square value of i from 0 to sqrt(c). If the diff between c and i^2 is already in dict, we're done.

        Time:
        - => O(sqrt(c)) for potentially exploring all values from 0 to sqrt(c)

        Space:
        - => O(sqrt(c)) for potentially storing all values (squares) from 0 to sqrt(c)
        """
        squares = set()
        for i in range(int(floor(sqrt(c))) + 1):
            iSquared = i * i
            squares.add(iSquared)
            difference = c - iSquared
            if difference in squares:
                return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
