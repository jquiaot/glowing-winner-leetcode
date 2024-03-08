from typing import List

"""
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all
have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the
array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]

Output: 4

Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum
frequency in the array.

So the number of elements in the array with maximum frequency is 4.

Example 2:


Input: nums = [1,2,3,4,5]

Output: 5

Explanation: All elements of the array have a frequency of 1 which is the
maximum.

So the number of elements in the array with maximum frequency is 5.
"""
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.maxFrequencyElements([1,2,2,3,1,4])
        4
        >>> s.maxFrequencyElements([1,2,3,4,5])
        5
        """
        return self.maxFrequencyElements1(nums)
    
    def maxFrequencyElements1(self, nums: list[int]) -> int:
        """
        Two passes:
        1. Build dict from element to frequency
        2. Sort dict by values descending, and return the number of elements with the same top value

        Time:
        - n = len(nums)
        - O(n) to populate frequencies dict
        - O(1) to insert/update frequency count
        - O(n*lg(n)) sort elements by frequencies in descending order
        - O(n) to traverse entries and count number with max frequency
        - => O(n*lg(n))
        Space:
        - n = len(nums)
        - O(n) for frequencies dict
        - O(n) for sorted entries list
        - => O(n)
        """
        frequencies = {}
        for n in nums:
            if n not in frequencies:
                frequencies[n] = 1
            else:
                frequencies[n] += 1
        
        elementsSortedByFrequency = sorted(frequencies.items(), reverse = True, key = lambda e: e[1])
        maxFrequency = elementsSortedByFrequency[0][1]
        countElements = 0
        for entry in elementsSortedByFrequency:
            if entry[1] == maxFrequency:
                countElements += 1
            else:
                break
        return countElements * maxFrequency

if __name__ == '__main__':
    import doctest
    doctest.testmod()
