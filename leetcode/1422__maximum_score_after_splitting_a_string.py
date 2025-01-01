from typing import List

"""Given a string s of zeros and ones, return the maximum score after splitting
the string into two non-empty substrings (i.e. left substring and right
substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:

Input: s = "011101"
Output: 5 

Explanation: 

All possible ways of splitting s into two non-empty substrings are:

left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5

Explanation: When left = "00" and right = "111", we get the maximum score = 2 +
3 = 5

Example 3:

Input: s = "1111"
Output: 3

Constraints:

- 2 <= s.length <= 500
- The string s consists of characters '0' and '1' only.

"""
class Solution:
    def maxScore(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.maxScore("011101")
        5
        >>> s.maxScore("00111")
        5
        >>> s.maxScore("1111")
        3
        """
        return self.maxScore1(s)

    def maxScore1(self, s: str) -> int:
        """
        - Pointer from 1..len(s)-2
        - Count 0's on left, count 1's on right
        - When advancing pointer, if value on pointer == 0, add to left,
          otherwise subtract from right?
        - Maintain max sum
        """

        maxScore = 0
        leftScore = 0
        rightScore = 0

        i = 1
        leftScore = self.countValues(s, 0, i, '0')
        rightScore = self.countValues(s, i, len(s), '1')
        maxScore = max(maxScore, leftScore + rightScore)

        while i <= len(s) - 2:
            if s[i] == '0':
                leftScore += 1
            else:
                rightScore -= 1
            maxScore = max(maxScore, leftScore + rightScore)
            i += 1
        return maxScore

    def countValues(self, s: str, start: int, end: int, target: str) -> int:
        total = 0
        # print(f"s={s}, start={start}, end={end}, target={target}")
        for i in range(start, end):
            if s[i] == target:
                total += 1
        # print(f"total={total}")
        return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
