from typing import List

"""
Given an integer array nums sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most twice. The
relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you
must instead have the result be placed in the first part of the array
nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not
matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,1,2,2,3]

Output: 5, nums = [1,1,2,2,3,_]

Explanation: Your function should return k = 5, with the first five elements of
nums being 1, 1, 2, 2 and 3 respectively.

It does not matter what you leave beyond the returned k (hence they are
underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]

Output: 7, nums = [0,0,1,1,2,3,3,_,_]

Explanation: Your function should return k = 7, with the first seven elements
of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.

It does not matter what you leave beyond the returned k (hence they are
underscores).

Constraints:

- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.removeDuplicates([1,1,1,2,2,3])
        5
        >>> s.removeDuplicates([0,0,1,1,1,1,2,3,3])
        7
        """
        # return self.removeDuplicatesWithState(nums)
        return self.removeDuplicatesInPlace(nums)

    def removeDuplicatesWithState(self, nums: list[int]) -> int:
        """
        How we would do this if we were able to maintain state:
        - start with empty dest list
        - for each element in nums
          - if dest is empty, just push element into dest and set count to 1
          - elif last element in dest is different from cur element,
            push cur element into dest and set count to 1
          - elif count of last element in dest is 1, push cur element
            into dest and set count to 2
          - else discard cur element

        Time: O(n) (iterating through nums at most once)
        Space: O(n) (maintaining result list)
        """
        result = []
        count = 0
        for num in nums:
            if count == 0:
                result.append(num)
                count = 1
            elif result[-1] < num:
                result.append(num)
                count = 1
            elif count == 1:
                result.append(num)
                count = 2
            else:
                pass
        return len(result)

    def removeDuplicatesInPlace(self, nums: list[int]) -> int:
        """
        Mirroring the logic above, but using in-place operations
        rather than creating an output list

        Time: O(n) (still iterating through nums at most once)
        Space: O(1) (aux storage for last index and count)
        """
        lastSlotIndex = 0
        count = 0
        for curIndex in range(len(nums)):
            if count == 0:
                nums[lastSlotIndex] = nums[curIndex]
                lastSlotIndex += 1
                count = 1
            elif nums[lastSlotIndex - 1] < nums[curIndex]:
                nums[lastSlotIndex] = nums[curIndex]
                lastSlotIndex += 1
                count = 1
            elif count == 1:
                nums[lastSlotIndex] = nums[curIndex]
                lastSlotIndex += 1
                count = 2
            else:
                # lastSlotIndex remains the same
                # curIndex will advance in for loop
                # count remains the same
                pass
        # print(nums)
        return lastSlotIndex
                
if __name__ == '__main__':
    import doctest
    doctest.testmod()
