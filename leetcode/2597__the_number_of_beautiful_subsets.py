from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.beautifulSubsets([2, 4, 6], 2)
        4
        >>> s.beautifulSubsets([1], 1)
        1
        """
        return self.beautifulSubsetsIter(nums, k)
    
    def beautifulSubsetsIter(self, nums: list[int], k: int) -> int:
        """
        Iteratively generate subsets, accumulating only if they are determined
        to be beautiful.

        Time: O(2^n)
        Space: O(1) (discounting output space)
        """
        beautifulSubsets = [[]]

        for num in nums:
            newSubsets = []
            for subset in beautifulSubsets:
                if self.isBeautifulSubset(subset, num, k):
                    newSubset = subset + [num]
                    newSubsets.append(newSubset)
            beautifulSubsets += newSubsets
        
        return len(beautifulSubsets) - 1 # remove empty subset

    def isBeautifulSubset(self, curSubset: list[int], candidateNum: int, k: int) -> bool:
        """
        Returns true iff no pair created from curSubset and candidateNum is "ugly".
        """
        for n in curSubset:
            if abs(n - candidateNum) == k:
                return False
        # print(f"{curSubset} + {candidateNum} is beautiful")
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
