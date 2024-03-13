"""
Given a positive integer n, find the pivot integer x such that:

- The sum of all elements between 1 and x inclusively equals the sum of all
  elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is
guaranteed that there will be at most one pivot index for the given input.

Example 1:

Input: n = 8

Output: 6

Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 =
21.

Example 2:

Input: n = 1

Output: 1

Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:

Input: n = 4

Output: -1

Explanation: It can be proved that no such integer exist.

Constraints:

    1 <= n <= 1000
"""
class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        >>> s = Solution()
        >>> s.pivotInteger(8)
        6
        >>> s.pivotInteger(1)
        1
        >>> s.pivotInteger(4)
        -1
        """
        return self.pivotInteger2(n)

    def pivotInteger1(self, n: int) -> int:
        """
        Sum of all values from 1..n = (n*(n+1))/2

        Sum of all values from 1..k and k..n = (n*(n+1))/2 + k

        Starting from end, keep subtracting from sum, and adding to the end
        sum, values from the end

        When to stop?

        - If off by k, then that is pivot

        - If off by more than k, then keep subtracting

        - If off by less than k, then there's no way to make sums equal, so
          return -1

        Time:
        - => O(n) to keep subtracting from the sum to find pivot or
             discover no possible pivot
        Space:
        - => O(1) to maintain front and end/back sums and pivot
        """
        frontSum = (n * (n + 1)) // 2
        endSum = 0
        pivot = n

        while True:
            # print(f"{frontSum} - {endSum} - {pivot}")
            if frontSum - endSum > pivot:
                frontSum -= pivot
                endSum += pivot
                pivot -= 1
            elif frontSum - endSum == pivot:
                return pivot
            else:
                return -1

    def pivotInteger2(self, n: int) -> int:
        """
        Two-pointer solution:
        - Maintain two pointers, to front and end
        - Maintain sums for each end
        - While pointers do not overlap
          - If values are unequal, add to smaller end's total and advance
            that end's value

        Time:
        - => O(n) traverse values from 1..n at most once
        Space:

        - => O(1) for maintaining current values from each and, and current
             sums from each end
        """
        frontValue = 1
        endValue = n

        frontSum = 0
        endSum = 0

        while frontValue < endValue:
            if frontSum < endSum:
                frontSum += frontValue
                frontValue += 1
            elif frontSum > endSum:
                endSum += endValue
                endValue -= 1
            else:
                frontSum += frontValue
                frontValue += 1
                endSum += endValue
                endValue -= 1
        if frontSum == endSum:
            return frontValue
        else:
            return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
