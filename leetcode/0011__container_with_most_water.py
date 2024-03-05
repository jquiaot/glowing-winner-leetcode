from typing import List

"""
You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i,
height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]

Output: 49

Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
container can contain is 49.

Example 2:

Input: height = [1,1]

Output: 1
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Strategy:
        - Starting from both ends, calculate the amount of water.
        - Contract the shorter side, then recalculate.
        - Stop when the pointers meet.

        Time:
        - Let n = len(height) (ha!)
        - => O(n) traverse the list at most once

        Space:
        - Let n = len(height)
        - => O(1) constant space to store pointers and max volume encountered
             so far

        >>> s = Solution()
        >>> s.maxArea([1,8,6,2,5,4,8,3,7])
        49
        >>> s.maxArea([1,1])
        1
        """
        i = 0
        j = len(height) - 1
        volume = min(height[i], height[j]) * (j - i)

        while i < j:
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            volume = max(volume, min(height[i], height[j]) * (j - i))

        return volume

if __name__ == '__main__':
    import doctest
    doctest.testmod()
