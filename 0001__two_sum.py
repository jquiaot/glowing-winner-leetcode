"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # return self.twoSum1(nums, target)
        return self.twoSum2(nums, target)

    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        """
        Naive solution: Starting from first number, try all the other numbers
        following it, until a solution is found. If none found, go to next number.

        Time: O(n^2) - test n elements at most n times
        Space: O(1) - no additional space needed

        >>> s = Solution()
        >>> s.twoSum1([2, 7, 11, 15], 9)
        [0, 1]
        >>> s.twoSum1([3, 2, 4], 6)
        [1, 2]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        """
        1. Create a list of tuples from num: [num, index_of_num]
        2. Sort list
        3. For each number n, use binary search to see if there is another
           number that when added to n will give target; if not, continue

        Time:
        - List of tuples: O(n)
        - Sort: O(n*lg(n))
        - Binary search: O(lg(n)), at most n times
            - => O(n) + O(n*lg(n)) + O(n*lg(n))
            - => O(n*lg(n)) (for sufficiently large n, O(n) goes away)

        Space: O(n) for list of tuples

        >>> s = Solution()
        >>> s.twoSum2([2, 7, 11, 15], 9)
        [0, 1]
        >>> s.twoSum2([3, 2, 4], 6)
        [1, 2]
        """
        tuples = []
        for i in range(len(nums)):
            tuples.append([nums[i], i])

        tuples.sort(key = lambda elt: elt[0])

        for elt in tuples:
            # binary search to find elt
            foundElt = self.binarySearch(tuples, target - elt[0])
            if foundElt is not None:
                return [elt[1], foundElt[1]]
        
        return None

    def binarySearch(self, tuples: list[tuple[int, int]], target: int) -> tuple[int, int]:
        """
        Binary search on tuples.
        """
        bottom = 0
        top = len(tuples) - 1
        mid = (top - bottom) // 2
        while bottom <= top:
            mid = (top + bottom) // 2
            if tuples[mid][0] == target:
                return tuples[mid]
            elif tuples[mid][0] > target:
                top = mid - 1
            else:
                bottom = mid + 1
        return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
