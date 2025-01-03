from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        - Keep a running sum of left and right sides for some i, 0 <= i < len(nums)
        - Increment i and add nums[i] to left sum and subtract nums[i] from right sum, check if valid

        >>> s = Solution()
        >>> s.waysToSplitArray([10, 4, -8, 7])
        2
        >>> s.waysToSplitArray([2, 3, 1, 0])
        2
        """
        countWays = 0
        lSum = 0
        rSum = sum(nums)
        i = 0
        # print(f"nums={nums}")
        while i < len(nums) - 1:
            lSum += nums[i]
            rSum -= nums[i]
            # print(f"i={i}, lSum={lSum}, rSum={rSum}")
            if lSum >= rSum:
                countWays += 1
            i += 1
        return countWays

if __name__ == '__main__':
    import doctest
    doctest.testmod()
