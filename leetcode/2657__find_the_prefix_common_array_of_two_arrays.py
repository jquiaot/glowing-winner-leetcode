from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        >>> s = Solution()
        >>> s.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4])
        [0, 2, 3, 4]
        >>> s.findThePrefixCommonArray([2, 3, 1], [3, 1, 2])
        [0, 1, 3]
        >>> s.findThePrefixCommonArray([1], [1])
        [1]
        >>> s.findThePrefixCommonArray([1, 2, 3], [1, 3, 2])
        [1, 1, 3]
        """
        return self.findThePrefixCommonArray1(A, B)

    def findThePrefixCommonArray1(self, A: List[int], B: List[int]) -> List[int]:
        """
        Per hints, keep a frequency array F where F[i] is the number of times the ith number has occurred.

        When F[i] == 2, we increment the count of common elements.
        """
        C = [0 for i in range(len(A))]
        F = [0 for i in range(len(A) + 1)]

        commonCount = 0
        for i in range(len(A)):
            F[A[i]] += 1
            if F[A[i]] == 2:
                commonCount += 1
            F[B[i]] += 1
            if F[B[i]] == 2:
                commonCount += 1
            C[i] = commonCount
        return C

if __name__ == '__main__':
    import doctest
    doctest.testmod()
