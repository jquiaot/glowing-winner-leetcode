from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        - Two pointers for sliding window start and end
        - Running sum of values in sliding window
        - Current minimum subarray length
        - While the start pointer hasn't reached the end
            - If the running sum is less than target
                - If we can expand the window from the end, do so
                - Otherwise we're done, return the minimum subarray length
            - If the running sum is equal to target
                - Compare current subarray to min subarray length, update as needed
                - Slide start up one
            - Else running sum is greater than target
                - While running sum is greater than target
                    - Slide start up one
        - Return min subarray length

        Time:
        - n = len(nums)
        - O(n) for working start pointer all the way through nums
        - => O(n)

        Space:
        - n = len(nums)
        - O(1) aux space for two pointers and running sum
        - => O(1)

        >>> s = Solution()
        >>> s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
        2
        >>> s.minSubArrayLen(4, [1, 4, 4])
        1
        >>> s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
        0
        """
        lenNums = len(nums)
        start = 0
        end = 0
        runningSum = 0
        curMinLength = lenNums
        foundAtLeastOneSubarray = False
        while start < lenNums:
            if runningSum < target:
                if end < lenNums:
                    runningSum += nums[end]
                    end += 1
                else:
                    break
            else: # runningSum >= target:
                foundAtLeastOneSubarray = True
                curWindowLength = end - start
                if curMinLength > curWindowLength:
                    curMinLength = curWindowLength
                runningSum -= nums[start]
                start += 1
        if foundAtLeastOneSubarray:
            return curMinLength
        else:
            return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
