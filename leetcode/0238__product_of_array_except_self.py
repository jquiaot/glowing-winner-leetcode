from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.productExceptSelf([1, 2, 3, 4])
        [24, 12, 8, 6]
        >>> s.productExceptSelf([-1, 1, 0, -3, 3])
        [0, 0, 9, 0, 0]
        """
        return self.productExceptSelfPrefixSuffix(nums)
    
    def productExceptSelfNaive(self, nums: list[int]) -> list[int]:
        """
        Just calculate it out.

        Time: O(n^2)
        Space: O(n) for products result (O(1) if you don't count output space)
        """
        products = []
        for i in range(len(nums)):
            p = 1
            for j in range(len(nums)):
                if i != j:
                    p *= nums[j]
            products.append(p)
        return products

    def productExceptSelfPrefixSuffix(self, nums: list[int]) -> list[int]:
        """
        Use prefix and suffix products to calculate the product of values before ith value and
        product of values after ith value.

        Time:
        - O(n) calculate prefix products
        - O(n) calculate suffix products
        - O(n) calculate final products
        - => O(n)

        Space:
        - O(n) prefix products
        - O(n) suffix products
        - => O(n) space for both
        """
        # prefix
        prefixProducts = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            prefixProducts[i] = prefixProducts[i - 1] * nums[i - 1]
        # suffix
        suffixProducts = [1 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            suffixProducts[i] = suffixProducts[i + 1] * nums[i + 1]
        # put it all together now
        products = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            products[i] = prefixProducts[i] * suffixProducts[i]
        return products

if __name__ == '__main__':
    import doctest
    doctest.testmod()
