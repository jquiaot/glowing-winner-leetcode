from typing import List

"""
Given an array of integers nums and an integer k, return the number of
contiguous subarrays where the product of all the elements in the subarray is
strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100

Output: 8

Explanation: The 8 subarrays that have product less than 100 are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

Note that [10, 5, 2] is not included as the product of 100 is not strictly less
than k.

Example 2:

Input: nums = [1,2,3], k = 0

Output: 0

Constraints:

* 1 <= nums.length <= 3 * 10^4 1 <= nums[i] <= 1000 0 <= k <= 10^6

"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        >>> s = Solution()
        >>> s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
        8
        >>> s.numSubarrayProductLessThanK([1, 2, 3], 0)
        0
        >>> s.numSubarrayProductLessThanK([57,44,92,28,66,60,37,33,52,38,29,76,8,75,22], 18)
        1
        """
        return self.numSubarrayProductLessThanK2(nums, k)

    def numSubarrayProductLessThanK1(self, nums: list[int], k: int) -> int:
        """
        Intuition: Given an array of m elements whose product is less
        than some value k, the number of subarrays whos product is
        still less than that value k and starting with the first element
        should be m.

        Using the above, we can figure out a sliding window algorithm
        to calculate the number of
        
        """
        # count of number of subarrays with product < k
        count = 0
        # head index of sliding window
        head = 0
        # tail index of sliding window
        tail = 0
        # current product
        product = 1

        n = len(nums)

        while head < n:
            # adjustment - if we're somehow not accumulating values
            # into the window to the point where the tail pointer is less than
            # the head pointer, we need to reset the tail pointer
            if tail < head:
                tail = head
                product = 1
            # expansion - keep extending tail of window until either
            # we reach the end of nums or the product exceeds k
            while tail < n:
                newProduct = product * nums[tail]
                if newProduct < k:
                    product = newProduct
                    tail += 1
                else:
                    break
            # print(f"Window at {head} - {tail}")
            # calculate size of window
            count += (tail - head)
            # remove head from product
            product //= nums[head]
            # advance head
            head += 1
        return count

    def numSubarrayProductLessThanK2(self, nums: list[int], k: int) -> int:
        """
        Calculate from tail pointer.

        If k is exceeded or head passes tail, we need to remove from
        product values from head and advance head pointer.

        At each tail position, calculate the number of subarrays possible
        from head to tail.
        """
        count = 0
        head = 0
        tail = 0
        product = 1
        for tail in range(len(nums)):
            # accumulate tail
            product *= nums[tail]
            # contract from head if our constraints are violated - product
            # exceeds k or head points past tail
            while product >= k and head <= tail:
                product //= nums[head]
                head += 1
            count += (tail - head) + 1
        return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
