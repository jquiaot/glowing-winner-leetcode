from typing import List

class Solution:
    """
    >>> s = Solution()
    >>> s.divideString(s = 'abcdefghi', k = 3, fill = 'x')
    ['abc', 'def', 'ghi']
    >>> s.divideString(s = 'abcdefghij', k = 3, fill = 'x')
    ['abc', 'def', 'ghi', 'jxx']
    >>> s.divideString(s = 'a', k = 1, fill = 'x')
    ['a']
    """
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return self.divideString1(s, k, fill)

    """
    1. Index i into current position in s
    2. Keep track of remaining characters (initial = len(s))
    3. While there are remaining chars
       a. If we have at least k chars, grab slice of s from i to i+k
       b. Otherwise, grab slice of s from i to i+remaining, and pad with fill char
    4. Increment index by k, decrement remaining by k

    Time:
    - n = len(s)
    - Iterate through all chars in s once - O(n)
    - => O(n)

    Space:
    - n = len(s)
    - Maintain variables for current index i and remaining chars
    - => O(1) (not counting return value)
    """
    def divideString1(self, s: str, k: int, fill: str) -> list[str]:
        groups = []
        remaining = len(s)
        i = 0
        while remaining > 0:
            if remaining >= k:
                groups.append(s[i:i + k])
            else:
                groups.append(s[i:i + remaining] + fill * (k - remaining))
            i += k
            remaining -= k
        return groups

if __name__ == '__main__':
    import doctest
    doctest.testmod()
