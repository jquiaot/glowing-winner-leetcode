from typing import List

"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.missingNumber([3, 0, 1])
        2
        >>> s.missingNumber([0, 1])
        2
        >>> s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        8
        """
        return self.missingNumber2(nums)

    def missingNumber1(self, nums: List[int]) -> int:
        """
        Allocate list of len(nums) + 1 elements, put each element of nums in
        list using element value as index, find None element in list.

        Time:
        - n = len(nums)
        - O(n) to iterate through nums and put in nums2
        - O(n) to iterate through nums2 to find None element
        - => O(n)
        Space:
        - n = len(nums)
        - => O(n) to allocate auxilliary space to store nums in indexed order
        """
        nums2 = [None for i in range(len(nums) + 1)]
        for num in nums:
            nums2[num] = num
            
        for i in range(len(nums2)):
            if nums2[i] is None:
                return i

    def missingNumber2(self, nums: List[int]) -> int:
        """
        Exploit the fact that the sum of numbers from 0..n = n*(n+1)/2

        Then missing number should just be n*(n+1)/2 - sum

        Time:
        - n = len(nums)
        - O(n) to iterate through nums to gather sum
        - O(1) to calculate ideal sum, and to calculate difference
          between ideal sum and actual sum
        - => O(n)

        Space:
        - => O(1) to store actual sum
        """
        sum = 0
        n = len(nums)
        for num in nums:
            sum += num
            
        return n*(n+1)//2 - sum

if __name__ == '__main__':
    import doctest
    doctest.testmod()
