from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        >>> s = Solution()
        >>> a = [1, 2, 3, 4, 5, 6, 7]
        >>> s.rotate(a, 3)
        >>> a == [5, 6, 7, 1, 2, 3, 4]
        True
        """
        return self.rotate2(nums, k)

    def rotate1(self, nums: list[int], k: int) -> None:
        """
        Using array slices
        """
        actualK = k % len(nums)
        sliceIndex = len(nums) - actualK
        nums[:] = [*nums[sliceIndex:], *nums[0:sliceIndex]]

    def rotate2(self, nums: list[int], k: int) -> None:
        """
        Brute-force rotate
        """
        for i in range(k):
            for j in range(len(nums) - 1, 0, -1):
                tmp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = tmp
            # print(nums)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
