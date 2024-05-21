from typing import List, Generator

"""

Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any
order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> s.subsets([1, 2, 3])
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        """
        # return self.subsetsUsingGenerator(nums)
        return self.subsetsIterative(nums)

    def subsetsUsingGenerator(self, nums: list[int]) -> list[list[int]]:
        return list(self.generateSubsets(nums))

    def generateSubsets(self, nums: list[int]) -> Generator[list[int], None, None]:
        """
        Generate subsets using a recursive generator function.

        How does it work?
        - for each element, recursively yield subsets for the sublist following that element
        - concatenate these recursively-generated subsets to the current element

        Time: O(2^n)
        Space: O(n) stack space?
        """
        # first yield the empty set
        yield []
        # for each element
        for i in range(len(nums)):
            # recursively generate subsets from the next onwards, and concat with the current element
            for rest in self.generateSubsets(nums[i + 1:]):
                yield [nums[i]] + rest

    def subsetsIterative(self, nums: list[int]) -> list[list[int]]:
        """
        Iteratively generate subsets, buillding on previous subsets.

        Time: O(2^n) (power or 2 time to build powerset
        Space: O(1) if we don't count output space?
        """
        results = []

        # start with empty subset
        results.append([])

        # for each number in nums, build up a new list of subsets
        # that is the current list of subsets with the current num
        # appended to them; add these new subsets to the results
        for num in nums:
            newResults = []
            for result in results:
                newResults.append(result + [num]) # list concat
            # add these new results to existing
            results += newResults # or results.extend(newResults)

        return results

if __name__ == '__main__':
    import doctest
    doctest.testmod()
