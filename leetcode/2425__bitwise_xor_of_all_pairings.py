from typing import List
from collections import defaultdict

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        >>> s = Solution()
        >>> s.xorAllNums([2, 1, 3], [10, 2, 5, 0])
        13
        >>> s.xorAllNums([1, 2], [3, 4])
        0
        """
        return self.xorAllNums2(nums1, nums2)

    def xorAllNums1(self, nums1: List[int], nums2: List[int]) -> int:
        """
        I guess the brute-force method is to just make pairings of nums1 
        and nums2, and then calculate the XOR of the resultant pairings.

        We can count the number of unique pairings (XOR values from nums1
        and nums2).

        If the count for a particular pairing is even, those pairings would
        cancel out, resulting in 0.

        If the count for a particular pairing is odd, those pairings would
        cancel out except for one of them, resulting in that value.
        """
        xorFrequencies = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                xorFrequencies[n1 ^ n2] += 1
        answer = 0
        for n, freq in xorFrequencies.items():
            if freq % 2 == 1:
                answer ^= n
        return answer

    def xorAllNums2(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Observations:
        
        (a1 ^ b1) ^ (a1 ^ b2) ^ ... (a1 ^ bn)
        = (a1 ^ a1 ^ ... ^ a1) ^ (b1 ^ b2 ^ ... bn)

        So, if nums2 (the b's above) is even, then all a's would cancel out,
        leaving just the XOR of all nums2. Same thing if nums1 is even,
        then all b's would cancel out, leaving just the XOR of all nums1.

        If both nums1 and nums2 are even length, all would cancel out,
        leaving 0.

        If both nums1 and nums2 are odd length, we'd be left just XORing
        all terms from nums1 and nums2 (the duplicates from each would
        cancel out).

        Time:
        - m = len(nums1)
        - n = len(nums2)
        - O(m) to XOR all nums1
        - O(n) to XOR all nums2
        - O(1) to determine what to return based on whether nums1, nums2, or 
          both are odd/even
        - => O(m+n)

        Space:
        - O(1) for space to store XOR of nums1, nums2
        - => O(1)
        """
        xorNums1 = 0
        for n in nums1:
            xorNums1 ^= n

        xorNums2 = 0
        for n in nums2:
            xorNums2 ^= n

        if len(nums1) % 2 == 0:
            if len(nums2) % 2 == 0:
                return 0
            else:
                return xorNums1
        else:
            if len(nums2) % 2 == 0:
                return xorNums2
            else:
                return xorNums1 ^ xorNums2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
