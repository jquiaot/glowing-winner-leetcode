from typing import List, Generator, Optional
import math


"""
An integer has sequential digits if and only if each digit in the number is one
more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that
have sequential digits.

Discussion and strategy:

We can know based on low and high the size of the sequential digits (number of
digits) using int(floor(log10())) + 1.

We'll need a function that generates sequential digits of length n.

Time:
- Feels like O(log10(n)) where n is values for high

Space:
- O(1) no auxilliary storage that depends on n

This solution doesn't appear to be efficient compared to others, possibly
because of the string to int conversion that happens in the loop. If
we mathematically generated the numbers it probably would be more efficient?
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        >>> s = Solution()
        >>> print(s.sequentialDigits(100, 300))
        [123, 234]
        """
        nums = []
        numDigitsStart = int(math.floor(math.log10(low))) + 1
        numDigitsEnd = int(math.floor(math.log10(high))) + 1
        # print(f"numDigits range = {numDigitsStart} - {numDigitsEnd}")
        for numDigits in range(numDigitsStart, numDigitsEnd + 1):
            # print(f"Trying {numDigits}")
            nums.extend(self.generateSequentialDigitIntegers(numDigits, low, high))
        return nums

    def generateSequentialDigitIntegers(self, numDigits: int, \
                                        low: int, \
                                        high: int) -> \
                                        Generator[int, None, None]:
        """
        s = Solution()
        print(list(s.generateSequentialDigitIntegers(2, 10, 20)))
        [12]
        """
        for i in range(1, 10):
            n = self.generateSequentialDigitInteger(numDigits, i)
            # print(f"Generated {n}")
            if n is None:
                break
            if n < low:
                continue
            elif n > high:
                break
            else:
                yield n

    """
    Generate a single sequential digit integer with the specified number of
    digits and having its first digit the specified start digit.
    """
    def generateSequentialDigitInteger(self, numDigits: int, \
                                       startDigit: int) -> \
                                       Optional[int]:
        """
        >>> s = Solution()
        >>> s.generateSequentialDigitInteger(2, 1)
        12
        >>> s.generateSequentialDigitInteger(2, 2)
        23
        >>> s.generateSequentialDigitInteger(2, 7)
        78
        >>> s.generateSequentialDigitInteger(2, 8)
        89
        >>> s.generateSequentialDigitInteger(2, 9)
        >>> s.generateSequentialDigitInteger(4, 1)
        1234
        >>> s.generateSequentialDigitInteger(4, 6)
        6789
        >>> s.generateSequentialDigitInteger(4, 7)
        """
        if startDigit + (numDigits - 1) >= 10:
            # can't make a sequential digit int with this start digit having
            # the specified number of digits
            return None
        return int("0123456789"[startDigit:startDigit + numDigits])
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
