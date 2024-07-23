from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        - Start with pointers i = 0, j = len(numbers) - 1
        - While i < j:
          - If numbers[i] + numbers[j] == target, we're done
          - If numbers[i] + numbers[j] < target, increase i by 1
          - if numbers[i] + numbers[j] > target, decrease j by 1

        Time:
        - n = len(numbers)
        - O(n) to traverse numbers from each end until some theoretical middle
        - => O(n)

        Space:
        - => O(1) pointers

        >>> s = Solution()
        >>> s.twoSum([2, 7, 11, 15], 9)
        [1, 2]
        >>> s.twoSum([2, 3, 4], 6)
        [1, 3]
        >>> s.twoSum([-1, 0], -1)
        [1, 2]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            the_sum = numbers[i] + numbers[j]
            if the_sum == target:
                return [i + 1, j + 1]
            elif the_sum < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
