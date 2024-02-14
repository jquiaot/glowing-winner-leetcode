from typing import List

"""
You are given a 0-indexed integer array nums of even length consisting of an
equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows
the given conditions:

1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present
   in nums is preserved.
3. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the
aforementioned conditions.
"""
class Solution:

    """
    >>> s = Solution()
    >>> s.rearrangeArray([-1, 1])
    [1, -1]
    >>> s.rearrangeArray([3, 1, -2, -5, 2, -4])
    [3, -2, 1, -5, 2, -4]
    >>> s.rearrangeArray([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])
    [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
    """
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        return self.rearrangeArray1(nums)

    def rearrangeArray1(self, nums: List[int]) -> List[int]:
        """
        Approach: Use two auxilliary arrays of length len(nums)/2 each to
        store the positive and negative numbers, in the order encountered in
        nums. Then reinsert into nums from positive and negative, alternating
        between the two.

        Time:
        - O(n) traverse through nums first time to divide into pos and neg
        - O(n) traverse through pos and neg to reconstitute nums according
          to rules
        - => O(n)

        Space:
        - => O(n) for pos and neg arrays
        """
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        splitIdx = 0
        numsIdx = 0
        while splitIdx < len(positives):
            nums[numsIdx] = positives[splitIdx]
            nums[numsIdx + 1] = negatives[splitIdx]
            splitIdx += 1
            numsIdx += 2
        return nums

if __name__ == '__main__':
    import doctest
    doctest.testmod()
