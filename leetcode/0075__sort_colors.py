from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        >>> s = Solution()
        >>> a = [2, 0, 2, 1, 1, 0]
        >>> s.sortColors(a)
        >>> print(a)
        [0, 0, 1, 1, 2, 2]
        >>> a = [2, 0, 1]
        >>> s.sortColors(a)
        >>> print(a)
        [0, 1, 2]
        """
        self.sortColors1(nums)
    
    def sortColors1(self, nums: list[int]) -> None:
        """
        Strategy: Since we know that the values in nums is limited to 0, 1, or 2,
        we can simply count the occurrences of each value and then repopulate
        nums based on the counts.

        Time:
        - n = len(nums)
        - O(n) to count occurrences
        - O(n) to repopulate nums based on occurrences
        - => O(n)

        Space:
        - n = len(nums)
        - O(1) occurrences storage (since finite number of possible values)
        - => O(1)
        """
        occurrences = {}
        for num in nums:
            if num not in occurrences:
                occurrences[num] = 1
            else:
                occurrences[num] += 1

        i = 0
        for num in [0, 1, 2]:
            if num in occurrences:
                for j in range(occurrences[num]):
                    nums[i] = num
                    i += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
