from typing import List

"""
Given two integer arrays nums1 and nums2, return an array of their
intersection. Each element in the result must be unique and you may return the
result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]

Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]

Output: [9,4]

Explanation: [4,9] is also accepted.
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> sorted(list(s.intersection([1, 2, 2, 1], [2, 2])))
        [2]
        >>> sorted(list(s.intersection([4, 9, 5], [9, 4, 9, 8, 4])))
        [4, 9]
        """
        return self.intersection1(nums1, nums2)
    
    def intersection1(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Built-ins way - convert to sets, find set intersection, convert to list

        Time:
        - n = len(nums1)
        - m = len(nums2)
        - O(n + m) convert nums1 and nums2 lists to set
        - O(n + m) intersection
        - O(n + m) convert to list
        - => O(n + m)

        Space:
        - => O(n + m) for the sets
        """
        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
