"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # return self.twoSum1(nums, target)
        # return self.twoSum2(nums, target)
        return self.twoSumWithDict(nums, target)

    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        """
        Naive solution: Starting from first number, try all the other numbers
        following it, until a solution is found. If none found, go to next number.

        Time: O(n^2) - test n elements at most n times
        Space: O(1) - no additional space needed

        >>> s = Solution()
        >>> sorted(s.twoSum1([2, 7, 11, 15], 9))
        [0, 1]
        >>> sorted(s.twoSum1([3, 2, 4], 6))
        [1, 2]
        >>> sorted(s.twoSum1([3, 3], 6))
        [0, 1]
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
        >>> sorted(s.twoSum2([2, 7, 11, 15], 9))
        [0, 1]
        >>> sorted(s.twoSum2([3, 2, 4], 6))
        [1, 2]
        >>> sorted(s.twoSum2([3, 3], 6))
        [0, 1]
        """
        tuples = []
        for i in range(len(nums)):
            tuples.append([nums[i], i])

        tuples.sort(key = lambda elt: elt[0])

        for elt in tuples:
            # binary search to find elt
            foundElt = self.binarySearch(tuples, [target - elt[0], elt[1]])
            if foundElt is not None:
                return [elt[1], foundElt[1]]
        
        return None

    def binarySearch(self, tuples: list[tuple[int, int]], targetTuple: tuple[int, int]) -> tuple[int, int]:
        """
        Binary search on tuples. Assumes tuples is sorted on the first element.
        """
        bottom = 0
        top = len(tuples) - 1
        mid = (top - bottom) // 2
        while bottom <= top:
            mid = (top + bottom) // 2
            if tuples[mid][0] == targetTuple[0]:
                break
            elif tuples[mid][0] > targetTuple[0]:
                top = mid - 1
            else:
                bottom = mid + 1

        if tuples[mid][0] == targetTuple[0]:
            # test indexes
            if tuples[mid][1] != targetTuple[1]:
                return tuples[mid]
            elif mid > 0 and tuples[mid - 1][0] == targetTuple[0]:
                return tuples[mid - 1]
            elif mid < len(tuples) - 2 and tuples[mid + 1][0] == targetTuple[0]:
                return tuples[mid + 1]
        else:
            return None

    def twoSumWithDict(self, nums: list[int], target: int) -> list[int]:
        """
        Create a dictionary mapping from value to its corresponding
        index in nums. For each value in nums, look up in dictionary
        the balance (value that is the difference of target and the
        ith value in nums). If it exists, return the pair of indices.

        Time:
        - let n = len(nums)
        - O(n) to generate dict
        - O(n) to iterate through nums, and for each iteration O(1) 
          dict lookup to check for its counterpart
        - => O(n)

        Space:
        - let n = len(nums)
        - O(n) dict mapping value to its index
        => O(n)
        """
        m = dict()
        for i in range(len(nums)):
            m[nums[i]] = i
        
        for i in range(len(nums)):
            balance = target - nums[i]
            if balance in m and m[balance] != i:
                return [i, m[balance]]
        return [-1, -1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

