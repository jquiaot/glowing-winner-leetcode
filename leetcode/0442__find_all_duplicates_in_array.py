from typing import List

"""
Given an integer array nums of length n where all the integers of nums are in
the range [1, n] and each integer appears once or twice, return an array of all
the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra
space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]

Output: [2,3]

Example 2:

Input: nums = [1,1,2]

Output: [1]

Example 3:

Input: nums = [1]

Output: []

Constraints:

* n == nums.length 1 <= n <= 10^5 1 <= nums[i] <= n Each element in nums
* appears once or twice.
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> sorted(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
        [2, 3]
        >>> sorted(s.findDuplicates([1, 1, 2]))
        [1]
        >>> sorted(s.findDuplicates([1]))
        []
        """
        return self.findDuplicates2(nums)

    def findDuplicates1(self, nums: list[int]) -> list[int]:
        """
        Super naive solution -- dict() to keep track of integers and counts,
        return those integers with count = 2

        Time: O(n)
        Space: O(n) (I know, violation of constraints of problem, just trying
        to get a solution out)
        """
        counts = dict()
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        duplicates = []
        for (n, occurrences) in counts.items():
            if occurrences == 2:
                duplicates.append(n)
        return duplicates
    
    def findDuplicates2(self, nums: list[int]) -> list[int]:
        """
        Not considering the space used to store the output, it appears we can
        compare each value in-place using the value to reference whether
        we've seen it before.

        - for each number in nums:
            - its prospective index is (number - 1)
            - if the value at the prospective index is negative, then
              we've seen it before (basically, flip the sign at the
              prospective index as a signal that we've seen that number)
              and so we should add it to the duplicates list
            - otherwise, flip the sign at the prospective index
        
        Time: O(n) to traverse nums and determine whether we've seen it before
        Space: O(1) no extra storage except for the output array, which if it
               were to be counted should be O(n/2) (since we're looking for
               numbers that appear twice, it naturally follows that we would
               see at most half of the values if all appeared twice)
        """
        duplicates = []
        for n in nums:
            prospectiveIndex = abs(n) - 1
            if nums[prospectiveIndex] < 0:
                # we've flipped the value to negative signaling we've seen
                # the value before
                duplicates.append(abs(n))
            else:
                # we need to flip the value to negative, indicating we've
                # now just seen that value
                nums[prospectiveIndex] *= -1
        return duplicates

if __name__ == '__main__':
    import doctest
    doctest.testmod()
