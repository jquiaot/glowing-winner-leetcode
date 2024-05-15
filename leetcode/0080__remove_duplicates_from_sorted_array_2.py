from typing import List

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
